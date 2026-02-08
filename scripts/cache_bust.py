#!/usr/bin/env python3
"""
Cache busting script: adds a query parameter with build timestamp to all
CSS, JS, and HTML assets to force browsers to fetch fresh versions.
"""

import os
import re
from datetime import datetime
from pathlib import Path


def get_build_hash():
    """Generate a cache bust hash based on current timestamp."""
    return datetime.now().strftime("%Y%m%d%H%M%S")


def add_cache_bust_to_files(site_dir):
    """Add cache busting query parameter to CSS, JS, and HTML files."""
    build_hash = get_build_hash()
    query_param = f"?v={build_hash}"

    print(f"🚀 Cache busting with hash: {build_hash}")

    site_path = Path(site_dir)

    # Process all HTML files
    for html_file in site_path.rglob("*.html"):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add cache bust to CSS links
        content = re.sub(
            r'(<link[^>]+href=["\'])([^"\']+\.css)(["\'])',
            rf'\1\2{query_param}\3',
            content
        )

        # Add cache bust to JavaScript includes
        content = re.sub(
            r'(<script[^>]+src=["\'])([^"\']+\.js)(["\'])',
            rf'\1\2{query_param}\3',
            content
        )

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"✅ Cache busting applied to {len(list(site_path.rglob('*.html')))} HTML files")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        site_dir = sys.argv[1]
    else:
        site_dir = "site"

    add_cache_bust_to_files(site_dir)
