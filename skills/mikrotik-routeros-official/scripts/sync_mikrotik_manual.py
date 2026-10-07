#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

BASE = "https://manual.mikrotik.com"
INDEX_URL = f"{BASE}/llms.txt"
ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"
STATE = REFS / "_sync-state.json"
MANIFEST = REFS / "_manifest.md"
HEADERS = {
    "User-Agent": "mikrotik-routeros-hermes-skill/1.1",
    "Accept": "text/markdown,text/plain;q=0.9,*/*;q=0.5",
}

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def safe(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", s.strip())
    return s.strip(".- ") or "page"

def out_path(url: str) -> Path:
    p = urlparse(url).path.strip("/")
    if p.endswith(".md"):
        p = p[:-3]
    if not p:
        p = "introduction"
    return Path(*[safe(x) for x in p.split("/") if x]).with_suffix(".md")

def discover(text: str):
    seen = set()
    pages = []
    for title, url in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", text):
        url = html.unescape(url).rstrip(".,")
        if "manual.mikrotik.com" not in url:
            continue
        if url.endswith(("/llms.txt", "/llms-full.txt")):
            continue
        if url not in seen:
            seen.add(url)
            pages.append((title.strip(), url))
    return pages

def markdown_url(url: str) -> str:
    p = urlparse(url).path
    if p.startswith("/docs/") and not p.endswith(".md"):
        return f"{BASE}{p}.md"
    return url

def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index_sha256": "", "pages": {}}

def save_state(state):
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n",
                     encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clean", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    REFS.mkdir(parents=True, exist_ok=True)
    state = load_state()

    if args.clean:
        for p in REFS.rglob("*"):
            if p.is_file() and p.name not in {".gitkeep"}:
                p.unlink()
        state = {"index_sha256": "", "pages": {}}

    session = requests.Session()
    session.headers.update(HEADERS)

    r = session.get(INDEX_URL, timeout=60)
    r.raise_for_status()
    index_text = r.text
    index_hash = sha256(index_text)

    pages = discover(index_text)
    if args.limit:
        pages = pages[:args.limit]

    desired = {}
    changed = []
    failed = []

    for title, source in pages:
        url = markdown_url(source)
        destination = REFS / out_path(url)
        destination.parent.mkdir(parents=True, exist_ok=True)

        old = state["pages"].get(source, {})
        old_hash = old.get("sha256", "")

        try:
            response = session.get(url, timeout=60)
            response.raise_for_status()
            content = response.text.strip()
            if not content:
                raise RuntimeError("empty response")

            digest = sha256(content)
            desired[source] = {
                "title": title,
                "markdown_url": url,
                "path": str(destination.relative_to(REFS)),
                "sha256": digest,
            }

            if digest != old_hash or not destination.exists():
                destination.write_text(content + "\n", encoding="utf-8")
                changed.append(str(destination.relative_to(REFS)))
                print("UPDATED", destination.relative_to(REFS))
            else:
                print("UNCHANGED", destination.relative_to(REFS))

        except Exception as exc:
            failed.append((title, url, str(exc)))
            print("FAILED", url, exc, file=sys.stderr)

        time.sleep(0.08)

    # Remove pages no longer in llms.txt.
    removed = []
    for source, meta in state["pages"].items():
        if source not in desired:
            path = REFS / meta.get("path", "")
            if path.exists() and path.is_file():
                path.unlink()
                removed.append(str(path.relative_to(REFS)))
                print("REMOVED", path.relative_to(REFS))

    state = {
        "index_sha256": index_hash,
        "pages": desired,
    }
    save_state(state)

    lines = [
        "# MikroTik RouterOS Official Manual — Sync Manifest",
        "",
        f"Source: {INDEX_URL}",
        f"Index SHA-256: `{index_hash}`",
        f"Pages in current index: {len(desired)}",
        f"Pages changed/written: {len(changed)}",
        f"Pages removed: {len(removed)}",
        f"Pages failed: {len(failed)}",
        "",
    ]

    for source, meta in sorted(desired.items(), key=lambda x: x[1]["path"]):
        lines.append(
            f"- [{meta['title']}]({meta['path']}) "
            f"`{meta['sha256'][:12]}`"
        )

    if removed:
        lines += ["", "## Removed pages", ""]
        lines += [f"- `{x}`" for x in removed]

    if failed:
        lines += ["", "## Failed pages", ""]
        lines += [f"- {title}: {url} — {err}" for title, url, err in failed]

    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")

    summary = {
        "index_changed": state["index_sha256"] != index_hash,
        "pages": len(desired),
        "changed": len(changed),
        "removed": len(removed),
        "failed": len(failed),
    }
    Path(REFS / "_sync-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )

    print("\nSYNC SUMMARY")
    print(json.dumps(summary, indent=2))
    return 1 if failed and not desired else 0

if __name__ == "__main__":
    raise SystemExit(main())
