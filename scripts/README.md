# Scripts

This directory contains utility scripts for the AI Patterns documentation site.

## validate_dependencies.py

Validates that the MkDocs configuration is correct and all dependencies are properly synchronized.

**What it checks:**
- All MkDocs plugins have corresponding packages in `requirements.txt`
- All CSV files referenced in markdown exist in `docs/data/`
- The MkDocs site builds successfully without errors

**Usage:**
```bash
python scripts/validate_dependencies.py
```

**Exit codes:**
- `0` - All validations passed
- `1` - One or more validations failed

**When to run:**
- Before committing changes to `mkdocs.yml` or `requirements.txt`
- After adding new plugins or CSV data files
- When troubleshooting build failures

**Automatic execution:**
- Runs automatically in GitHub Actions on every push/PR
- Can be configured as a pre-commit hook (see `.pre-commit-config.yaml`)

## cache_bust.py

Adds cache-busting query parameters to static assets to ensure users get the latest version after deployments.

**Usage:**
```bash
python scripts/cache_bust.py site
```

This script is automatically run by the GitHub Actions workflow after building the site.
