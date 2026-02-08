# Quick GitHub Pages Setup - 3 Steps

This repository is already configured for GitHub Pages deployment. Just enable it in GitHub:

## Step 1: Enable GitHub Pages in Settings

1. Go to your repository **Settings**
2. Find **Pages** in the left sidebar (under "Code and automation")
3. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select **gh-pages** from the dropdown
   - **Folder**: Keep as **/ (root)**
4. Click **Save**

## Step 2: Wait for Deployment

1. Go to the **Actions** tab
2. Watch for the "Deploy to GitHub Pages" workflow to complete (1-2 minutes)
3. Look for a ✓ check mark

## Step 3: Visit Your Site

Once the workflow succeeds, your site is live at:

```
https://your-username.github.io/ai-patterns/
```

---

## How It Works

The GitHub Actions workflow (`.github/workflows/deploy.yml`) automatically:
- ✓ Runs on every push to `master`
- ✓ Builds documentation with MkDocs
- ✓ Deploys to GitHub Pages (gh-pages branch)
- ✓ Takes 1-2 minutes

**No manual deployment needed!**

---

## Updating Your Documentation

1. Edit markdown files in the `docs/` folder
2. Commit and push to master
3. Workflow automatically rebuilds and deploys (1-2 minutes)

---

## Need Help?

See [`docs/setup.md`](docs/setup.md) for:
- Detailed step-by-step instructions
- Screenshots
- Troubleshooting tips
- Custom domain setup
- Advanced configuration options

---

## What's Already Set Up

✓ MkDocs configuration (mkdocs.yml)
✓ Documentation structure (docs/ folder)
✓ GitHub Actions workflow (.github/workflows/deploy.yml)
✓ Material Design theme
✓ Search functionality
✓ Mermaid diagram support

All you need to do is enable Pages in GitHub settings!
