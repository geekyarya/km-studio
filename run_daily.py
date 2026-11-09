"""Runs every hour on GitHub Actions. Publishes every item whose time slot has passed today
and whose images exist. State is kept in state/posted.json (committed back to the repo).

DRY_RUN=true (or no Instagram secrets) -> builds the media but does not post.
"""
import datetime as dt
import json
import os
import pathlib
import sys
import time

import subprocess

import news
import reel_maker
from make_plans import CONFIG, today_ist

ROOT = pathlib.Path(__file__).parent
STATE = ROOT / "state" / "posted.json"
HEADLINES = ROOT / "state" / "used_headlines.json"


def git_publish(path: pathlib.Path, msg: str) -> None:
    """Commit + push one file so Instagram can download it from its public raw URL."""
    rel = str(path.relative_to(ROOT))
    subprocess.run(["git", "add", rel], cwd=ROOT, check=True)
    subprocess.run(["git", "commit", "-q", "-m", msg], cwd=ROOT)  # may be already committed
    subprocess.run(["git", "pull", "-q", "--rebase"], cwd=ROOT, check=True)
    subprocess.run(["git", "push", "-q"], cwd=ROOT, check=True)


def with_headline(item: dict, used: list) -> tuple[str | None, str]:
    """Returns (on-screen hook, caption) - using a fresh real headline for news-type topics."""
    if "news_query" in item and item["news_query"] is not None:
        h = news.pick(item["news_query"], used)
        if h:
            used.append(h[0])
            caption = f"{h[0]}\n\n{item['reaction']}\n\nSource: {h[1]}\n\n{item['tags']}"
            return news.shorten(h[0]), caption
    return item["hook"], item["caption"]


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

    used = json.loads(HEADLINES.read_text()) if HEADLINES.exists() else []
    dry = os.getenv("DRY_RUN", "").lower() == "true" or not os.getenv("IG_ACCESS_TOKEN")
    if not dry:
        import instagram
    now_hm = now_ist().strftime("%H:%M")
    OUT.mkdir(exist_ok=True)
    errors = 0

    post_now = int(os.getenv("POST_NOW", "0") or 0)  # manual "post now" from the Actions tab
    max_per_run = post_now or int(os.getenv("MAX_PER_RUN", "2"))  # never dump a backlog all at once
    published = 0
    for item in plan["items"]:
        key = item["id"]
        if key in done or (item["slot"] > now_hm and not post_now):
            continue
        if published >= max_per_run:
            print(f"{key}: waiting for next run (max {max_per_run} per hour)")
            continue
        files = [ROOT / im["file"] for im in item["images"]]
        if not all(f.exists() for f in files):
            print(f"{key}: images missing, skipping")
            continue
        try:
            hook, caption = with_headline(item, used)
            if item["type"] == "reel":
                video = ROOT / item["images"][0]["file"].rsplit("/", 1)[0] / f"{key}.mp4"
                reel_maker.make_reel([str(f) for f in files], hook, str(video), CONFIG["seconds_per_image"])
                if dry:
                    media_id = "dry-run"
                else:
                    git_publish(video, f"reel {day} {key}")
                    time.sleep(10)  # let raw.githubusercontent.com serve the new file
                    media_id = instagram.post_reel_url(raw_url(str(video.relative_to(ROOT))), caption)
            else:
                # Instagram downloads photos from a public URL, so the 4:5 crop must already be
                # pushed to GitHub. Colab makes it; if missing, make + publish it now.
                rel = f"{item['images'][0]['file'][:-4]}_ig.jpg"
                if not (ROOT / rel).exists():
                    reel_maker.make_post_image(str(files[0]), str(ROOT / rel))
                    if not dry:
                        git_publish(ROOT / rel, f"post image {day} {key}")
                        time.sleep(10)
                media_id = "dry-run" if dry else instagram.post_photo(raw_url(rel), caption)
            done[key] = {"media_id": media_id, "at": now_ist().isoformat(timespec="minutes")}
            published += 1
            print(f"{key}: {'built (dry run)' if dry else 'posted'} -> {media_id}")
        except Exception as e:  # keep going, retry next hour
            errors += 1
            detail = getattr(getattr(e, "response", None), "text", "")
            print(f"{key}: FAILED {e} {detail[:500]}")

    if not dry:
        STATE.parent.mkdir(exist_ok=True)
        STATE.write_text(json.dumps(state, indent=2))
        HEADLINES.write_text(json.dumps(used[-300:], indent=1, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
