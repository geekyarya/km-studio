"""Free live headlines from Google News RSS (no API key)."""
import random
import urllib.parse
import xml.etree.ElementTree as ET

import requests

# Kiara is a fun persona - skip tragedies and crime.
SKIP_WORDS = ["killed", "dead", "death", "dies", "died", "murder", "rape", "attack", "blast", "accident",
              "suicide", "crash", "injured", "arrest", "terror", "riot", "assault", "funeral", "rip ",
              # low-value headlines
              "live score", "live updates", "live:", "streaming", "where to watch", "commentary", "playing xi",
              "playing 11", "scorecard", "| cricinfo", "weather forecast", "toss time"]


def fetch(query: str | None) -> list[tuple[str, str]]:
    """Returns [(headline, publisher), ...]."""
    if query is None:
        return []
    base = "https://news.google.com/rss"
    url = (f"{base}/search?q={urllib.parse.quote(query)}&" if query else f"{base}?") + "hl=en-IN&gl=IN&ceid=IN:en"
    try:
        root = ET.fromstring(requests.get(url, timeout=20).content)
    except Exception as e:
        print("news fetch failed:", e)
        return []
    out = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        if " - " in title:
            title, publisher = title.rsplit(" - ", 1)
        else:
            publisher = (item.findtext("source") or "").strip()
        if title and not any(w in title.lower() for w in SKIP_WORDS):
            out.append((title.strip(), publisher.strip()))
    return out


def pick(query: str | None, used: list[str]) -> tuple[str, str] | None:
    fresh = [h for h in fetch(query)[:25] if h[0] not in used]
    return random.choice(fresh[:10]) if fresh else None


def shorten(text: str, limit: int = 70) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(",:;-") + "…"
