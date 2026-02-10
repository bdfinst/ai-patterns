// Force cache busting on navigation
document.addEventListener('DOMContentLoaded', function() {
  // Add timestamp to all internal links to bust cache
  const timestamp = Date.now();

  // Override fetch to add cache-busting parameter
  const originalFetch = window.fetch;
  window.fetch = function(url, options) {
    if (typeof url === 'string' && url.includes(window.location.origin)) {
      const separator = url.includes('?') ? '&' : '?';
      url = url + separator + '_=' + timestamp;
    }
    return originalFetch(url, options);
  };

  // For Material's instant loading, add cache control
  if (typeof app !== 'undefined' && app.nav) {
    app.nav.addCacheBuster = true;
  }
});
