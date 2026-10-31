"""Runs every hour on GitHub Actions. Publishes every item whose time slot has passed today
and whose images exist. State is kept in state/posted.json (committed back to the repo).

DRY_RUN=true (or no Instagram secrets) -> builds the media but does not post.
"""
import datetime as dt
import json
import os
import pathlib
import sys

import reel_maker
from make_plans import CONFIG, today_ist

ROOT = pathlib.Path(__file__).parent
STATE = ROOT / "state" / "posted.json"
OUT = ROOT / "output"


def now_ist() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=CONFIG["timezone_offset_minutes"])


def raw_url(rel_path: str) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "OWNER/REPO")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{rel_path}"


def main() -> int:
    day = today_ist()
    plan_file = ROOT / "plans" / f"{day}.json"
    if not plan_file.exists():
        print(f"No plan for {day}. Run the weekly Colab notebook.")
        return 0
    plan = json.loads(plan_file.read_text())
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    done = state.setdefault(str(day), {})

    dry = os.getenv("DRY_RUN", "").lower() == "true" or not os.getenv("IG_ACCESS_TOKEN")
    if not dry:
        import instagram
    now_hm = now_ist().strftime("%H:%M")
    OUT.mkdir(exist_ok=True)
    errors = 0

    max_per_run = int(os.getenv("MAX_PER_RUN", "2"))  # never dump a backlog all at once
    published = 0
    for item in plan["items"]:
        key = item["id"]
        if key in done or item["slot"] > now_hm:
            continue
        if published >= max_per_run:
            print(f"{key}: waiting for next run (max {max_per_run} per hour)")
            continue
        files = [ROOT / im["file"] for im in item["images"]]
        if not all(f.exists() for f in files):
            print(f"{key}: images missing, skipping")
            continue
        try:
            if item["type"] == "reel":
                video = OUT / f"{day}_{key}.mp4"
                reel_maker.make_reel([str(f) for f in files], item["hook"], str(video), CONFIG["seconds_per_image"])
                media_id = "dry-run" if dry else instagram.post_reel(str(video), item["caption"])
            else:
                # Instagram downloads photos from a public URL, so the 4:5 crop must already be
                # pushed to GitHub. Colab makes it; if missing, make it now and post next hour.
                rel = f"{item['images'][0]['file'][:-4]}_ig.jpg"
                if not (ROOT / rel).exists():
                    reel_maker.make_post_image(str(files[0]), str(ROOT / rel))
                    print(f"{key}: made 4:5 crop, will post on next run after it is pushed")
                    continue
                media_id = "dry-run" if dry else instagram.post_photo(raw_url(rel), item["caption"])
            done[key] = {"media_id": media_id, "at": now_ist().isoformat(timespec="minutes")}
            published += 1
            print(f"{key}: {'built (dry run)' if dry else 'posted'} -> {media_id}")
        except Exception as e:  # keep going, retry next hour
            errors += 1
            print(f"{key}: FAILED {e}")

    if not dry:
        STATE.parent.mkdir(exist_ok=True)
        STATE.write_text(json.dumps(state, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
