"""
Submit site URLs to IndexNow (used by Bing, DuckDuckGo, Yandex) so they get
crawled quickly after a content update, instead of waiting for the next
scheduled crawl.

Run this any time after pushing a real content change:
    python _scripts/submit_indexnow.py
"""
import json
import urllib.request

HOST = "zqi180252-oss.github.io"
KEY = "2b5986994a333771c40a8ab44cc43676"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

URLS = [
    f"https://{HOST}/",
    f"https://{HOST}/publications/",
    f"https://{HOST}/Professional_activities/",
    f"https://{HOST}/teaching/",
    f"https://{HOST}/beyond-research/",
]

payload = json.dumps({
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": URLS,
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=payload,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)

with urllib.request.urlopen(req) as resp:
    print("Status:", resp.status)
    print(resp.read().decode())
