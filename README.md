# AI Patterns

The current patterns I use for delivering software with AI agents.

## 📚 View the Documentation

This repository is configured as a **GitHub Pages static documentation site** using MkDocs.

### Quick Setup (3 steps)

See **[GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)** for quick instructions to enable GitHub Pages.

Once enabled, visit: `https://your-username.github.io/ai-patterns/`

### Full Setup Guide

For detailed setup instructions, troubleshooting, and customization, see the [GitHub Pages Setup Guide](docs/setup.md) (also available in the published docs).

## 📖 Content

- **[Automated Code Review with AI Agents](docs/agentic-code-review.md)** - A hybrid approach combining deterministic rules-based tooling with context-aware AI agents to automate code review

## 🛠️ Local Development

To preview documentation locally:

```bash
pip install -r requirements.txt
mkdocs serve
```

Then visit `http://localhost:8000/ai-patterns/`

## 📝 Adding New Documentation

1. Create a new `.md` file in the `docs/` folder
2. Update `mkdocs.yml` to add it to the navigation
3. Push to `master` - site automatically rebuilds!

## 🚀 Instant Deployment

Once GitHub Pages is enabled:
- Push markdown files to `master` branch in `/docs` folder
- GitHub Pages automatically serves them - updates instantly!
- GitHub Actions validates the build configuration (optional)

No build or deployment step needed!
