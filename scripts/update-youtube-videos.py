#!/usr/bin/env python3

import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


PLAYLIST_ID = "PLNg09XqZv0dFzHP1LxYb7tIsK_Pk94mK_"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?playlist_id={PLAYLIST_ID}"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "docs" / "videos.json"

ATOM = "http://www.w3.org/2005/Atom"
YOUTUBE = "http://www.youtube.com/xml/schemas/2015"


def fetch_feed() -> bytes:
    request = urllib.request.Request(
        FEED_URL,
        headers={"User-Agent": "amd-strix-halo-gfx1151-toolboxes-feed-updater/1.0"},
    )

    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                if response.status != 200:
                    raise RuntimeError(f"YouTube returned HTTP {response.status}")
                return response.read()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2**attempt)

    raise RuntimeError("YouTube feed request failed")


def parse_feed(xml: bytes) -> dict:
    root = ET.fromstring(xml)
    videos = []

    for entry in root.findall(f"{{{ATOM}}}entry"):
        video_id = entry.findtext(f"{{{YOUTUBE}}}videoId")
        title = entry.findtext(f"{{{ATOM}}}title")

        if not video_id or not title:
            raise ValueError("YouTube feed entry is missing a video ID or title")
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id) is None:
            raise ValueError(f"YouTube feed contains an invalid video ID: {video_id}")

        videos.append(
            {
                "id": video_id,
                "title": title,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "thumbnail": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
            }
        )

    if not videos:
        raise ValueError("YouTube feed did not contain any videos")

    return {
        "playlistId": PLAYLIST_ID,
        "title": root.findtext(f"{{{ATOM}}}title", default="YouTube tutorials"),
        "videos": videos,
    }


def main() -> int:
    try:
        data = parse_feed(fetch_feed())
    except Exception as error:
        print(f"Failed to update YouTube videos: {error}", file=sys.stderr)
        return 1

    rendered = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else None

    if current == rendered:
        print("YouTube videos are already up to date.")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"Updated {OUTPUT_PATH.relative_to(OUTPUT_PATH.parents[1])} with {len(data['videos'])} videos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
