// Initialize Mermaid diagrams
console.log('Mermaid init script loaded');

function initMermaid() {
  console.log('Checking for mermaid library...');

  if (typeof mermaid === 'undefined') {
    console.warn('Mermaid library not found, will retry');
    setTimeout(initMermaid, 500);
    return;
  }

  console.log('Mermaid library found, version:', mermaid.version);

  try {
    // Initialize mermaid
    mermaid.initialize({ startOnLoad: true });
    mermaid.contentLoaded();

    // Find and render diagrams
    const diagrams = document.querySelectorAll('.mermaid');
    console.log('Found', diagrams.length, 'mermaid diagram(s)');

    if (diagrams.length > 0) {
      mermaid.run();
      console.log('✓ Mermaid diagrams rendered successfully');
    }
  } catch (e) {
    console.error('✗ Error rendering mermaid diagrams:', e);
  }
}

// Wait for DOM to be ready
if (document.readyState === 'loading') {
  console.log('DOM loading, waiting for DOMContentLoaded...');
  document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded fired');
    setTimeout(initMermaid, 100);
  });
} else {
  console.log('DOM already loaded');
  setTimeout(initMermaid, 100);
}

// Re-run on dynamic page updates (Material theme navigation.instant)
document.addEventListener('page:load', function() {
  console.log('Page:load event fired, re-rendering mermaid...');
  initMermaid();
});
