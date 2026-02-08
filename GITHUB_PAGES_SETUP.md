# Quick GitHub Pages Setup - 2 Steps

This repository is configured to serve documentation directly from the `docs/` folder.

## Step 1: Enable GitHub Pages in Settings

1. Go to your repository **Settings**
2. Find **Pages** in the left sidebar (under "Code and automation")
3. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select **master**
   - **Folder**: Select **/docs** ← Important!
4. Click **Save**

## Step 2: Visit Your Site

Your site is now live at:

```
https://your-username.github.io/ai-patterns/
```

---

## How It Works

GitHub Pages directly serves markdown files from the `/docs` folder:
- ✓ Push markdown to `docs/` folder on master branch
- ✓ GitHub Pages automatically serves them
- ✓ Updates instantly when you push
- ✓ No build or deployment step needed!

---

## Updating Your Documentation

1. Edit markdown files in the `docs/` folder
2. Commit and push to master
3. Site updates instantly (no delay!)

---

## Need Help?

See [`docs/setup.md`](docs/setup.md) for:
- Detailed step-by-step instructions
- Troubleshooting tips
- Custom domain setup
- Advanced configuration options

---

## What's Already Set Up

✓ Documentation structure (docs/ folder with index.md and content)
✓ GitHub Actions workflow for validation (.github/workflows/deploy.yml)
✓ MkDocs configuration (mkdocs.yml) - useful for local preview
✓ Material Design theme (nice look when used with mkdocs serve)

All you need to do is enable Pages in GitHub settings!
