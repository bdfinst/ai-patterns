# Mermaid Rendering Debugging Guide

## Local Testing

✅ **Mermaid is properly configured locally!**

To test locally before deploying:
```bash
source venv/bin/activate
mkdocs serve
```

Then visit: http://localhost:8000/ai-patterns/

The flowchart under "A Two-Phase Review Architecture" should render with boxes and connections.

## Deployed Site Debugging

If mermaid isn't rendering on the deployed site, follow these steps:

### 1. Check Browser Console for Errors
- Visit: https://bryanfinster.github.io/ai-patterns/agentic-code-review/
- Open DevTools: Press `F12` or Right-click → Inspect
- Go to **Console** tab
- Look for any red error messages
- Common issues:
  - `CORS errors` - CDN might be blocked
  - `Uncaught ReferenceError: mermaid is not defined` - Script didn't load

### 2. Check Network Tab
- In DevTools, go to **Network** tab
- Reload the page
- Look for `mermaid.min.js` - is it:
  - ✅ Loaded? (Status 200)
  - ❌ Failed? (Status 403, 404)
  - ❌ Blocked? (Shows BLOCKED status)

### 3. Check HTML Source
- Right-click → View Page Source
- Search for `<div class="mermaid">` - should contain the flowchart code
- Search for `mermaid.min.js` - should see the script tag
- If missing, the built site wasn't deployed correctly

### 4. Clear Cache
- Hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- Or clear browser cache entirely
- Cache busting should handle this, but manual clear can help

## Common Issues and Fixes

### Issue: Script loads but diagram doesn't render
- **Cause**: Mermaid script loads after diagram elements
- **Fix**: Check if `defer` attribute is on script tag
- Current config uses CDN which should work

### Issue: "Failed to load mermaid.min.js"
- **Cause**: CDN is unreachable or blocked
- **Fix**: Download mermaid locally instead of using CDN
  - Add to requirements.txt: `mkdocs-material` (includes mermaid support)
  - Update mkdocs.yml to use local mermaid if available

### Issue: Content Security Policy blocks inline code
- **Cause**: Deployed site has strict CSP headers
- **Fix**: Check if server is sending CSP headers that block `cdn.jsdelivr.net`

## Validation Command

Run locally after building:
```bash
python scripts/validate_mermaid.py site
```

This checks:
- ✅ Mermaid script is in HTML
- ✅ Diagrams are in HTML
- ✅ Cache busting parameters are applied
- ⚠️  Potential CSP issues

## Next Steps

1. Check the deployed site with DevTools (steps 1-2 above)
2. Report what errors you see in the Console
3. Verify if mermaid.min.js loads in the Network tab
4. Share the actual error messages for more specific fixes
