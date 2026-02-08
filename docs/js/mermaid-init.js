// Initialize Mermaid when available
function initMermaid() {
  if (typeof mermaid !== 'undefined') {
    console.log('Initializing Mermaid...');
    try {
      mermaid.contentLoaded();
      mermaid.run();
      console.log('Mermaid initialized successfully');
    } catch (e) {
      console.error('Mermaid initialization error:', e);
    }
  } else {
    console.warn('Mermaid library not loaded yet, retrying...');
    setTimeout(initMermaid, 500);
  }
}

// Initialize on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMermaid);
} else {
  initMermaid();
}

// Re-run on page updates (for navigation.instant feature)
document.addEventListener('page:load', function() {
  console.log('Page loaded, reinitializing Mermaid...');
  initMermaid();
});
