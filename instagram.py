"""Instagram content publishing (free).
Default: Facebook Graph API with a business-portfolio System User token
(instagram_basic + instagram_content_publish). Set IG_API_HOST=graph.instagram.com
to use an Instagram-Login token instead.
Reels are uploaded directly from the file; photos are fetched by Instagram from their
public GitHub raw URL."""
import os
import pathlib
import time

import requests

VERSION = "v21.0"
GRAPH = f"https://{os.getenv('IG_API_HOST', 'graph.facebook.com')}/{VERSION}"


def _creds():
    return os.environ["IG_USER_ID"], os.environ["IG_ACCESS_TOKEN"]


def _wait_and_publish(creation_id: str) -> str:
    ig_user, token = _creds()
    for _ in range(40):
        r = requests.get(f"{GRAPH}/{creation_id}", params={"fields": "status_code", "access_token": token}, timeout=30)
        status = r.json().get("status_code")
        if status == "FINISHED":
            break
        if status in ("ERROR", "EXPIRED"):
            raise RuntimeError(f"Instagram processing failed: {r.json()}")
        time.sleep(15)
    else:
        raise TimeoutError("Instagram processing timed out")
    r = requests.post(f"{GRAPH}/{ig_user}/media_publish",
                      data={"creation_id": creation_id, "access_token": token}, timeout=60)
    r.raise_for_status()
    return r.json()["id"]


def post_reel(video_path: str, caption: str) -> str:
    ig_user, token = _creds()
    r = requests.post(f"{GRAPH}/{ig_user}/media", data={
        "media_type": "REELS", "upload_type": "resumable", "caption": caption,
        "share_to_feed": "true", "access_token": token}, timeout=60)
    r.raise_for_status()
    creation_id = r.json()["id"]

    data = pathlib.Path(video_path).read_bytes()
    up = requests.post(
        f"https://rupload.facebook.com/ig-api-upload/{VERSION}/{creation_id}",
        headers={"Authorization": f"OAuth {token}", "offset": "0", "file_size": str(len(data))},
        data=data, timeout=300)
    up.raise_for_status()
    return _wait_and_publish(creation_id)


def post_photo(image_url: str, caption: str) -> str:
    ig_user, token = _creds()
    r = requests.post(f"{GRAPH}/{ig_user}/media",
                      data={"image_url": image_url, "caption": caption, "access_token": token}, timeout=60)
    r.raise_for_status()
    return _wait_and_publish(r.json()["id"])
