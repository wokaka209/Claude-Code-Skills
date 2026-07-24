#!/usr/bin/env python3
"""Search AWS icon definitions bundled with the skill.

Examples:
    python scripts/find_aws_icon.py lambda
    python scripts/find_aws_icon.py vpc
    python scripts/find_aws_icon.py security --limit 5
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


STYLE_TEMPLATES = {
    "resourceIcon": "shape=mxgraph.aws4.resourceIcon;resIcon={icon};",
    "productIcon": "shape=mxgraph.aws4.productIcon;prIcon={icon};",
    "group": "shape=mxgraph.aws4.group;grIcon={icon};",
}


def load_icons() -> list[dict[str, str]]:
    reference = Path(__file__).resolve().parent.parent / "references" / "aws-icons.md"
    content = reference.read_text(encoding="utf-8")
    pattern = re.compile(
        r"\|\s*([^|]+?)\s*\|\s*(mxgraph\.aws4\.[^|]+?)\s*\|\s*(resourceIcon|productIcon|group)\s*\|"
    )
    items = []
    for match in pattern.finditer(content):
        name, icon, style_key = match.groups()
        items.append(
            {
                "name": name.strip(),
                "icon": icon.strip(),
                "style_key": style_key.strip(),
            }
        )
    return items


def search_icons(query: str, limit: int) -> list[dict[str, str]]:
    normalized = query.lower().replace(" ", "")
    results = []
    for item in load_icons():
        haystacks = (
            item["name"].lower().replace(" ", ""),
            item["icon"].lower(),
            item["style_key"].lower(),
        )
        if any(normalized in haystack for haystack in haystacks):
            item = dict(item)
            item["style"] = STYLE_TEMPLATES[item["style_key"]].format(icon=item["icon"])
            results.append(item)

    results.sort(
        key=lambda item: (
            item["name"].lower() != query.lower(),
            item["icon"].lower() != query.lower(),
            len(item["name"]),
        )
    )
    return results[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Search bundled AWS icon references")
    parser.add_argument("query", help="Service name, icon key, or group name")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    results = search_icons(args.query, args.limit)
    if not results:
        print(f"No AWS icons found for query: {args.query}", file=sys.stderr)
        return 1

    if args.as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    print(f"Found {len(results)} result(s) for '{args.query}':")
    print()
    for result in results:
        print(f"Name: {result['name']}")
        print(f"Icon: {result['icon']}")
        print(f"Style key: {result['style_key']}")
        print(f"Style: {result['style']}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
