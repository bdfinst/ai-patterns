// Material theme compatible mermaid initialization
// Uses document$ observable to work with navigation.instant
document.addEventListener('DOMContentLoaded', function() {
  // Load mermaid dynamically
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js';
  script.onload = function() {
    mermaid.initialize({ startOnLoad: false });
    renderMermaid();
  };
  document.head.appendChild(script);
});

function renderMermaid() {
  var elements = document.querySelectorAll('pre.mermaid code');
  if (elements.length === 0) return;

  elements.forEach(function(el, i) {
    var parent = el.parentElement;
    var container = document.createElement('div');
    container.className = 'mermaid';
    container.textContent = el.textContent;
    parent.parentElement.replaceChild(container, parent);
  });

  mermaid.run();
}

// Handle Material theme instant navigation
var defined = false;
var observer = new MutationObserver(function() {
  if (typeof mermaid !== 'undefined' && !defined) {
    defined = true;
  }
  if (defined) {
    renderMermaid();
  }
});

observer.observe(document.body, { childList: true, subtree: true });
