"""Daily pipeline: plan -> image -> video -> (post or queue for review).

AUTO_POST=true  -> publishes to Instagram automatically
AUTO_POST unset -> saves everything to output/<date>/ for you to review and post
"""
import datetime
import json
import os
import pathlib
import sys

import requests

import generator
import planner

ROOT = pathlib.Path(__file__).parent
HISTORY = ROOT / "history.json"


def main(plan_only: bool = False) -> None:
    history = json.loads(HISTORY.read_text()) if HISTORY.exists() else []
    today = datetime.date.today().isoformat()
    out = ROOT / "output" / today
    out.mkdir(parents=True, exist_ok=True)

    print("Planning today's post...")
    plan = planner.plan_today(history)
    caption = f"{plan['caption']}\n\n{' '.join(plan['hashtags'])}"
    print(json.dumps(plan, indent=2, ensure_ascii=False))

    record = {"date": today, "pillar": plan["pillar"], "title": plan["title"], "plan": plan}

    if not plan_only:
        print("Generating image...")
        record["image_url"] = generator.make_image(plan)
        print("Animating video...")
        record["video_url"] = generator.make_video(plan, record["image_url"])
        (out / "video.mp4").write_bytes(requests.get(record["video_url"], timeout=120).content)

        if os.getenv("AUTO_POST", "").lower() == "true":
            import poster
            print("Posting to Instagram...")
            record["instagram_media_id"] = poster.post_reel(record["video_url"], caption)
            record["status"] = "posted"
        else:
            record["status"] = "ready_for_review"

    (out / "caption.txt").write_text(caption, encoding="utf-8")
    (out / "plan.json").write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    history.append({k: record[k] for k in ("date", "pillar", "title")})
    HISTORY.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Done -> {out}  status={record.get('status', 'plan_only')}")


if __name__ == "__main__":
    main(plan_only="--plan-only" in sys.argv)
