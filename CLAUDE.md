# Claude Code Configuration

This file contains instructions and validations for Claude Code when working on this project.

## Project Structure

This is an MkDocs-based documentation site deployed to GitHub Pages via GitHub Actions.

**Key Files:**
- `mkdocs.yml` - MkDocs configuration with plugins and theme settings
- `requirements.txt` - Python dependencies for CI/CD and local development
- `docs/` - Documentation source files (Markdown)
- `docs/data/` - CSV files for data tables
- `.github/workflows/deploy.yml` - GitHub Actions workflow for building and deploying

## Dependency Management Rules

### 🚨 CRITICAL: Plugin Synchronization

**BLOCKING REQUIREMENT:** When adding or modifying MkDocs plugins or Python dependencies:

1. **Always update both locations:**
   - Add plugin to `mkdocs.yml` under `plugins:` section
   - Add plugin package to `requirements.txt` with pinned version

2. **Validation checklist before committing:**
   ```bash
   # Run this validation script:
   python scripts/validate_dependencies.py
   ```

3. **Test locally before pushing:**
   ```bash
   # Install dependencies
   pip install -r requirements.txt

   # Build the site
   mkdocs build

   # Verify no errors
   echo $?  # Should output: 0
   ```

### Common Mistakes to Avoid

❌ **DON'T:** Install plugins locally without updating requirements.txt
❌ **DON'T:** Add plugins to mkdocs.yml without adding to requirements.txt
❌ **DON'T:** Assume CI environment has packages from your local venv

✅ **DO:** Always pin versions in requirements.txt (e.g., `package==1.2.3`)
✅ **DO:** Test the build in a fresh virtual environment before pushing
✅ **DO:** Run validation scripts before committing

## MkDocs Plugins

Current plugins in use:
- `search` - Built-in search functionality
- `git-revision-date` - Shows last modification date (requires: mkdocs-git-revision-date-plugin)
- `table-reader` - Imports CSV/Excel files as tables (requires: mkdocs-table-reader-plugin)

### Adding New Plugins

When adding a new MkDocs plugin, follow this checklist:

1. [ ] Research the plugin package name on PyPI
2. [ ] Install locally: `pip install <plugin-package>`
3. [ ] Add to `mkdocs.yml` under `plugins:` section
4. [ ] Add to `requirements.txt` with pinned version: `<plugin-package>==X.Y.Z`
5. [ ] Test build locally: `mkdocs build`
6. [ ] Run validation: `python scripts/validate_dependencies.py`
7. [ ] Commit both `mkdocs.yml` AND `requirements.txt` together

## DataTables Configuration

The site uses jQuery DataTables for sortable, filterable, exportable tables.

**Files:**
- `docs/js/datatables-init.js` - Initializes DataTables on all tables
- `docs/css/datatables-custom.css` - Custom styling for tables and buttons

**External dependencies (loaded via CDN in mkdocs.yml):**
- jQuery 3.7.1
- DataTables 1.13.7
- DataTables Buttons extension 2.4.2
- JSZip (for Excel export)
- pdfmake (for PDF export)

These are loaded from CDN and don't require entries in requirements.txt.

## CSV Data Tables

Tables are maintained as CSV files in `docs/data/` and imported using the table-reader plugin:

```markdown
{{ read_csv('data/filename.csv') }}
```

**Rules:**
- CSV files must be in `docs/data/` directory
- Use underscores in filenames, not hyphens (e.g., `defect_cause_catalog.csv`)
- CSV files should have headers in the first row
- DataTables JavaScript automatically adds sorting/filtering/export to all tables

## Pre-Commit Validation

Before committing changes that affect dependencies or configuration:

```bash
# Run validation
python scripts/validate_dependencies.py

# If validation fails, fix the issues before committing
```

The validation script checks:
- All plugins in mkdocs.yml have corresponding packages in requirements.txt
- All CSV files referenced in markdown exist in docs/data/
- MkDocs build succeeds without errors

## GitHub Actions Workflow

The `.github/workflows/deploy.yml` workflow:
1. Checks out the repository
2. Sets up Python 3.11
3. Installs dependencies from `requirements.txt`
4. Builds the site with `mkdocs build`
5. Runs cache busting script
6. Deploys to GitHub Pages (on push to master)

**If the build fails in CI:**
- Check that all plugins in `mkdocs.yml` are in `requirements.txt`
- Verify the plugin package names are correct (MkDocs plugin name ≠ PyPI package name)
- Check that the versions are compatible with Python 3.11

## Common Plugin Name Mappings

| MkDocs Plugin Name | PyPI Package Name |
|-------------------|-------------------|
| `search` | Built-in, no package needed |
| `git-revision-date` | `mkdocs-git-revision-date-plugin` |
| `table-reader` | `mkdocs-table-reader-plugin` |
| `material` | `mkdocs-material` (theme, not plugin) |

## Troubleshooting

### Build fails with "ModuleNotFoundError: No module named 'X'"
- Add the missing package to `requirements.txt`
- Install locally: `pip install <package>`
- Test: `mkdocs build`

### Build fails with "Error: Plugin 'X' not installed"
- Check plugin name in `mkdocs.yml` matches the package documentation
- Verify the package is in `requirements.txt`
- Check package name on PyPI (may differ from plugin name)

### CSV tables not rendering
- Verify CSV file exists in `docs/data/`
- Check filename in markdown matches actual filename (case-sensitive)
- Ensure `table-reader` plugin is in `mkdocs.yml` AND `mkdocs-table-reader-plugin` is in `requirements.txt`

### DataTables not working (tables not sortable/filterable)
- Check browser console for JavaScript errors
- Verify all JavaScript files are loaded in correct order in `mkdocs.yml`
- Ensure jQuery is loaded before DataTables
- Check that `datatables-init.js` is loaded last (after all libraries)
