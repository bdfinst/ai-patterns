#!/usr/bin/env python3
"""
Validate that mermaid diagrams are properly configured in the built site.
"""

import re
from pathlib import Path


def validate_mermaid(site_dir="site"):
    """Check mermaid configuration in built HTML files."""
    site_path = Path(site_dir)

    print("🔍 Validating Mermaid Configuration\n")
    print("=" * 50)

    issues = []
    html_files = list(site_path.rglob("*.html"))

    if not html_files:
        print("❌ No HTML files found in site directory!")
        return False

    print(f"✅ Found {len(html_files)} HTML files to check\n")

    # Check for mermaid script
    mermaid_script_found = False
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'mermaid.min.js' in content:
            mermaid_script_found = True
            print(f"✅ Mermaid script found in: {html_file.name}")
            break

    if not mermaid_script_found:
        issues.append("❌ Mermaid JavaScript library not found in any HTML file!")

    print()

    # Check for mermaid diagrams
    mermaid_diagrams_found = False
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'class="mermaid"' in content or '<pre><code class="language-mermaid">' in content:
            mermaid_diagrams_found = True

            # Count diagrams
            diagram_count = content.count('class="mermaid"') + content.count('language-mermaid')
            print(f"✅ Found {diagram_count} mermaid diagram(s) in: {html_file.name}")

            # Show snippet
            match = re.search(r'(<div[^>]*class="mermaid"[^>]*>.*?</div>)', content, re.DOTALL)
            if match:
                snippet = match.group(1)[:200]
                print(f"   Snippet: {snippet}...")

    if not mermaid_diagrams_found:
        issues.append("⚠️  No mermaid diagrams found in any HTML file!")

    print()

    # Check for CSS/JS loading issues
    print("Checking asset loading:\n")

    sample_html = html_files[0]
    with open(sample_html, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if mermaid script has cache bust param
    if 'mermaid.min.js?v=' in content:
        print("✅ Mermaid script has cache busting parameter")
    elif 'mermaid.min.js' in content:
        print("⚠️  Mermaid script found but no cache busting parameter")

    # Check for CSP issues
    if 'Content-Security-Policy' in content:
        print("⚠️  Content-Security-Policy found - may block inline scripts")
        issues.append("Check CSP headers in deployed site")

    print("\n" + "=" * 50)

    if issues:
        print("\n⚠️  ISSUES FOUND:")
        for issue in issues:
            print(f"  {issue}")
        return False
    else:
        print("\n✅ All mermaid checks passed!")
        return True


if __name__ == "__main__":
    import sys

    site_dir = sys.argv[1] if len(sys.argv) > 1 else "site"
    success = validate_mermaid(site_dir)
    sys.exit(0 if success else 1)
