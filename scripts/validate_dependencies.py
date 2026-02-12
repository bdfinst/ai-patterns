#!/usr/bin/env python3
"""
Validate that all MkDocs plugins have corresponding packages in requirements.txt
and all CSV files referenced in markdown exist.
"""

import sys
import yaml
import re
from pathlib import Path

# Color codes for output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def error(msg):
    print(f"{RED}✗ ERROR:{RESET} {msg}")

def success(msg):
    print(f"{GREEN}✓ SUCCESS:{RESET} {msg}")

def warning(msg):
    print(f"{YELLOW}⚠ WARNING:{RESET} {msg}")

def info(msg):
    print(f"{BOLD}INFO:{RESET} {msg}")

# Plugin name to package name mapping
PLUGIN_PACKAGE_MAP = {
    'search': None,  # Built-in, no package needed
    'git-revision-date': 'mkdocs-git-revision-date-plugin',
    'table-reader': 'mkdocs-table-reader-plugin',
}

def load_requirements():
    """Load packages from requirements.txt"""
    req_file = Path('requirements.txt')
    if not req_file.exists():
        error("requirements.txt not found")
        return None

    packages = {}
    with open(req_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # Parse package==version format
                match = re.match(r'^([a-zA-Z0-9\-_]+)==(.+)$', line)
                if match:
                    packages[match.group(1)] = match.group(2)
                else:
                    warning(f"Could not parse requirement: {line}")

    return packages

def load_mkdocs_config():
    """Load MkDocs configuration"""
    config_file = Path('mkdocs.yml')
    if not config_file.exists():
        error("mkdocs.yml not found")
        return None

    # Create a custom YAML loader that ignores unknown tags (like !python/name:)
    class IgnoreUnknownTagsLoader(yaml.SafeLoader):
        def ignore_unknown(self, node):
            return None

    IgnoreUnknownTagsLoader.add_constructor(None, IgnoreUnknownTagsLoader.ignore_unknown)

    with open(config_file) as f:
        return yaml.load(f, Loader=IgnoreUnknownTagsLoader)

def check_plugins():
    """Check that all plugins have corresponding packages"""
    info("Checking MkDocs plugins...")

    config = load_mkdocs_config()
    if config is None:
        return False

    requirements = load_requirements()
    if requirements is None:
        return False

    plugins = config.get('plugins', [])
    if not plugins:
        warning("No plugins configured in mkdocs.yml")
        return True

    all_ok = True

    for plugin in plugins:
        # Handle both string and dict plugin configs
        plugin_name = plugin if isinstance(plugin, str) else list(plugin.keys())[0]

        # Check if plugin needs a package
        if plugin_name in PLUGIN_PACKAGE_MAP:
            required_package = PLUGIN_PACKAGE_MAP[plugin_name]

            if required_package is None:
                success(f"Plugin '{plugin_name}' is built-in")
            elif required_package in requirements:
                success(f"Plugin '{plugin_name}' → package '{required_package}' ({requirements[required_package]})")
            else:
                error(f"Plugin '{plugin_name}' requires package '{required_package}' but it's not in requirements.txt")
                all_ok = False
        else:
            warning(f"Plugin '{plugin_name}' not in known plugin mapping - cannot verify package")

    return all_ok

def check_csv_files():
    """Check that all CSV files referenced in markdown exist"""
    info("\nChecking CSV file references...")

    docs_dir = Path('docs')
    if not docs_dir.exists():
        error("docs/ directory not found")
        return False

    all_ok = True
    csv_pattern = re.compile(r'\{\{\s*read_csv\([\'"]([^\'"]+)[\'"]\)\s*\}\}')

    # Find all markdown files
    md_files = list(docs_dir.rglob('*.md'))

    if not md_files:
        warning("No markdown files found in docs/")
        return True

    references_found = False

    for md_file in md_files:
        with open(md_file) as f:
            content = f.read()
            matches = csv_pattern.findall(content)

            for csv_path in matches:
                references_found = True
                # CSV path is relative to docs/
                full_path = docs_dir / csv_path

                if full_path.exists():
                    success(f"CSV file exists: {csv_path}")
                else:
                    error(f"CSV file not found: {csv_path} (referenced in {md_file.relative_to(docs_dir)})")
                    all_ok = False

    if not references_found:
        info("No CSV file references found in markdown files")

    return all_ok

def check_mkdocs_build():
    """Check that MkDocs can build the site"""
    info("\nTesting MkDocs build...")

    import subprocess

    try:
        result = subprocess.run(
            ['mkdocs', 'build', '--strict'],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            success("MkDocs build succeeded")
            return True
        else:
            error("MkDocs build failed:")
            print(result.stderr)
            return False
    except subprocess.TimeoutExpired:
        error("MkDocs build timed out")
        return False
    except FileNotFoundError:
        warning("mkdocs command not found - skipping build test")
        return True

def main():
    print(f"\n{BOLD}=== MkDocs Dependency Validation ==={RESET}\n")

    # Change to project root
    project_root = Path(__file__).parent.parent
    import os
    os.chdir(project_root)

    checks = [
        ("Plugin dependencies", check_plugins),
        ("CSV file references", check_csv_files),
        ("MkDocs build", check_mkdocs_build),
    ]

    results = {}
    for name, check_func in checks:
        results[name] = check_func()

    # Summary
    print(f"\n{BOLD}=== Summary ==={RESET}")
    all_passed = all(results.values())

    for name, passed in results.items():
        status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
        print(f"  {status} - {name}")

    if all_passed:
        print(f"\n{GREEN}{BOLD}✓ All validations passed!{RESET}\n")
        return 0
    else:
        print(f"\n{RED}{BOLD}✗ Some validations failed. Please fix the issues above.{RESET}\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
