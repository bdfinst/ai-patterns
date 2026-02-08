// Initialize Mermaid after page loads
document.addEventListener('DOMContentLoaded', function() {
  if (typeof mermaid !== 'undefined') {
    mermaid.contentLoaded();
    mermaid.run();
  }
});

// Also re-run on page updates (for navigation.instant feature)
if (typeof document !== 'undefined') {
  document.addEventListener('page:load', function() {
    if (typeof mermaid !== 'undefined') {
      mermaid.run();
    }
  });
}
