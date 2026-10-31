"""Creates daily content plans (plans/YYYY-MM-DD.json) from the offline content bank.

Usage: python make_plans.py [--days 7] [--from YYYY-MM-DD]
Existing plan files are never overwritten, so you can hand-edit any day.
"""
import argparse
import datetime as dt
import json
import pathlib
import random

import content_bank as bank
import persona

ROOT = pathlib.Path(__file__).parent
PLANS = ROOT / "plans"
CONFIG = json.loads((ROOT / "config.json").read_text())


def today_ist() -> dt.date:
    now = dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=CONFIG["timezone_offset_minutes"])
    return now.date()


def volume_for(day: dt.date) -> tuple[int, int]:
    n = (day - dt.date.fromisoformat(CONFIG["start_date"])).days
    reels, posts = 0, 0
    for step in CONFIG["ramp"]:
        if n >= step["from_day"]:
            reels, posts = step["reels"], step["posts"]
    return reels, posts


def recent_combos(day: dt.date, lookback: int = 45) -> set[tuple[str, str]]:
    used = set()
    for i in range(1, lookback + 1):
        f = PLANS / f"{day - dt.timedelta(days=i)}.json"
        if f.exists():
            for item in json.loads(f.read_text())["items"]:
                used.add((item["outfit"], item["location"]))
    return used


def build_prompt(outfit: str, location: str, pose: str) -> str:
    return f"{persona.LOOK}, wearing {outfit}, {location}, {pose}, {persona.QUALITY}"


def make_item(rng, kind, slot, pillar_key, used, day, idx, festival=None, n_images=1):
    p = bank.PILLARS[pillar_key]
    for _ in range(50):
        outfit, location = rng.choice(p["outfits"]), rng.choice(p["locations"])
        if (outfit, location) not in used:
            break
    if festival:
        location = festival
    used.add((outfit, location))
    poses = rng.sample(p["poses"], k=min(n_images, len(p["poses"])))
    while len(poses) < n_images:
        poses.append(rng.choice(p["poses"]))

    caption = rng.choice(p["captions"])
    sign = rng.choice(bank.SIGN_OFFS)
    tags = rng.sample(p["tags"], k=min(8, len(p["tags"]))) + bank.ALWAYS_TAGS
    item_id = f"{kind}{idx}"
    return {
        "id": item_id,
        "type": kind,
        "slot": slot,
        "pillar": pillar_key,
        "outfit": outfit,
        "location": location,
        "hook": rng.choice(p["hooks"]) if kind == "reel" else None,
        "caption": f"{caption}\n{sign}".strip() + "\n\n" + " ".join(tags),
        "images": [
            {
                "file": f"media/{day}/{item_id}_{n}.jpg",
                "prompt": build_prompt(outfit, location, pose),
                "seed": rng.randint(1, 2**31 - 1),
            }
            for n, pose in enumerate(poses)
        ],
    }


def plan_day(day: dt.date) -> dict:
    rng = random.Random(f"kiara-{day}")
    reels, posts = volume_for(day)
    used = recent_combos(day)
    pillars = list(bank.PILLARS)
    rng.shuffle(pillars)
    festival = bank.MOVABLE_FESTIVALS.get(str(day)) or bank.FESTIVALS.get(day.strftime("%m-%d"))

    items = []
    for i in range(reels):
        items.append(make_item(rng, "reel", CONFIG["reel_slots"][i], pillars[i % len(pillars)], used, day, i,
                               festival if i == 0 else None, CONFIG["images_per_reel"]))
    for i in range(posts):
        pk = pillars[(i + 2) % len(pillars)]
        items.append(make_item(rng, "post", CONFIG["post_slots"][i], pk, used, day, i,
                               festival if i == 0 else None))
    return {"date": str(day), "festival": festival, "items": sorted(items, key=lambda x: x["slot"])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--from", dest="start", default=None)
    args = ap.parse_args()
    start = dt.date.fromisoformat(args.start) if args.start else today_ist()
    PLANS.mkdir(exist_ok=True)
    for i in range(args.days):
        day = start + dt.timedelta(days=i)
        f = PLANS / f"{day}.json"
        if f.exists():
            print(f"{day}: exists, kept")
            continue
        plan = plan_day(day)
        f.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
        r = sum(x["type"] == "reel" for x in plan["items"])
        print(f"{day}: {r} reels, {len(plan['items']) - r} posts" + (f"  🎉 {plan['festival']}" if plan["festival"] else ""))


if __name__ == "__main__":
    main()
