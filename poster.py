"""Publishes a Reel through the Instagram Graph API (business/creator account)."""
import os
import time

import requests

API = "https://graph.facebook.com/v21.0"


def post_reel(video_url: str, caption: str) -> str:
    ig_user = os.environ["IG_USER_ID"]
    token = os.environ["IG_ACCESS_TOKEN"]

    container = requests.post(
        f"{API}/{ig_user}/media",
        data={"media_type": "REELS", "video_url": video_url, "caption": caption, "access_token": token},
        timeout=60,
    )
    container.raise_for_status()
    creation_id = container.json()["id"]

    for _ in range(40):  # wait up to ~10 min for Instagram to process the video
        status = requests.get(
            f"{API}/{creation_id}", params={"fields": "status_code", "access_token": token}, timeout=30
        ).json().get("status_code")
        if status == "FINISHED":
            break
        if status == "ERROR":
            raise RuntimeError("Instagram failed to process the video")
        time.sleep(15)
    else:
        raise TimeoutError("Instagram video processing timed out")

    published = requests.post(
        f"{API}/{ig_user}/media_publish",
        data={"creation_id": creation_id, "access_token": token},
        timeout=60,
    )
    published.raise_for_status()
    return published.json()["id"]
