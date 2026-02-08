# GitHub Pages Setup Guide

This guide walks you through configuring GitHub Pages to deploy your AI Patterns documentation site.

## Prerequisites

- Repository pushed to GitHub (completed ✓)
- GitHub Actions workflow in place (completed ✓)

## Step 1: Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/your-username/ai-patterns
2. Click the **Settings** tab
3. Scroll down to the **Pages** section in the left sidebar (under "Code and automation")

## Step 2: Configure the Deployment Source

In the **Pages** settings:

1. Under **"Build and deployment"** section:
   - **Source**: Select **Deploy from a branch** (this is the default)
   - **Branch**: Select **gh-pages** from the dropdown
   - **Folder**: Keep as **/ (root)** (the default)

2. Click **Save**

### Why gh-pages?

The GitHub Actions workflow automatically pushes built content to the `gh-pages` branch. This separates your source code (master branch) from your deployed site (gh-pages branch).

## Step 3: Wait for Deployment

1. Go to the **Actions** tab in your repository
2. You should see a workflow run:
   - First run: "Deploy to GitHub Pages"
   - It will build your docs and deploy them
   - Look for a ✓ (check mark) to indicate success

The deployment typically takes 1-2 minutes.

## Step 4: Access Your Site

Once the workflow completes successfully:

1. Return to **Settings → Pages**
2. You'll see a message like: "Your site is live at `https://your-username.github.io/ai-patterns/`"
3. Click the link to view your published documentation

## Verifying the Setup

Your site should display:
- **Home page** with links to patterns
- **Automated Code Review** page with the full documentation
- **Search functionality** in the top right
- **Table of contents** navigation
- **Responsive design** that works on mobile and desktop

## Custom Domain (Optional)

If you want to use a custom domain:

1. In **Settings → Pages**
2. Under **Custom domain**, enter your domain (e.g., `patterns.yourdomain.com`)
3. Follow GitHub's DNS configuration instructions
4. A `CNAME` file will be automatically created in your gh-pages branch

## Troubleshooting

### Site Not Showing Up

- **Check Actions workflow**: Go to Actions tab → ensure "Deploy to GitHub Pages" ran successfully
- **Wait longer**: GitHub Pages can take 2-3 minutes to become available
- **Clear cache**: Try accessing in an incognito/private browser window
- **Verify branch**: Ensure gh-pages branch exists in your repository

### Build Errors

If the Actions workflow fails:

1. Click the failed workflow run
2. Scroll down to see the error output
3. Common issues:
   - Missing dependencies: Check `requirements.txt` contains all needed packages
   - YAML syntax errors: Verify `.github/workflows/deploy.yml` formatting
   - Python version issues: Workflow uses Python 3.11

### Changes Not Appearing

1. Ensure you pushed to the `master` branch (workflow only deploys on master pushes)
2. Check Actions tab to confirm workflow ran
3. Hard refresh your browser (Ctrl+Shift+R or Cmd+Shift+R)
4. Check that changes are in the `docs/` folder (not just at repo root)

## Automatic Deployments

Once enabled, the workflow automatically:

✓ Runs when you push to `master`
✓ Builds your documentation with MkDocs
✓ Deploys to GitHub Pages (gh-pages branch)
✓ Takes 1-2 minutes from push to live site

No manual deployment steps needed!

## Updating Documentation

To update your site:

1. Edit markdown files in the `docs/` folder
2. Commit changes: `git add docs/ && git commit -m "Update docs"`
3. Push to master: `git push`
4. GitHub Actions automatically rebuilds and deploys (1-2 minutes)

## Advanced Configuration

### Add More Pages

1. Create new markdown file in `docs/` folder (e.g., `docs/best-practices.md`)
2. Update `mkdocs.yml` navigation section:
   ```yaml
   nav:
     - Home: index.md
     - Automated Code Review: agentic-code-review.md
     - Best Practices: best-practices.md
   ```
3. Commit and push
4. Site automatically rebuilds

### Customize Theme

Edit `mkdocs.yml` to change colors, fonts, and theme settings:

```yaml
theme:
  name: material
  palette:
    - scheme: default
      primary: blue      # Change primary color
      accent: cyan       # Change accent color
```

See [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/) for all options.

## FAQ

**Q: Do I need to create the gh-pages branch manually?**
A: No, GitHub Actions creates it automatically on first deployment.

**Q: Can I still push to master without deploying?**
A: Not with the current workflow. Every master push triggers a deployment. To change this, modify the `on` trigger in `.github/workflows/deploy.yml`.

**Q: How do I unpublish the site?**
A: In Settings → Pages, set Source to "None" (this doesn't delete the gh-pages branch, just stops serving it).

**Q: What if I have GitHub Pages already enabled for a different purpose?**
A: You only need one Pages site per repository. The workflow deploys to the same place.

**Q: Can I preview changes before they go live?**
A: Yes! Run `mkdocs serve` locally to preview at `http://localhost:8000/ai-patterns/`

## Success Checklist

- [ ] Navigated to Settings → Pages
- [ ] Source set to "Deploy from a branch"
- [ ] Branch set to "gh-pages"
- [ ] Workflow completed successfully (check Actions tab)
- [ ] Site is accessible at `https://your-username.github.io/ai-patterns/`
- [ ] All pages load correctly
- [ ] Search works
- [ ] Navigation works on mobile

## Next Steps

Your documentation site is now live! Consider:

- Adding a link to the GitHub Pages URL in your repository README
- Sharing the documentation with your team
- Adding more patterns and best practices over time
- Customizing the theme to match your brand (optional)

For more information, see:
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
