// Load mermaid library dynamically
// Script runs at end of body, DOM is already parsed
var mermaidScript = document.createElement('script');
mermaidScript.src = 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js';
mermaidScript.onload = function() {
  mermaid.initialize({ startOnLoad: false });
  renderMermaid();
};
document.head.appendChild(mermaidScript);

function renderMermaid() {
  // Convert <pre class="mermaid"><code>...</code></pre> to <div class="mermaid">...</div>
  var elements = document.querySelectorAll('pre.mermaid code');
  if (elements.length === 0) return;

  elements.forEach(function(el) {
    var pre = el.parentElement;
    var div = document.createElement('div');
    div.className = 'mermaid';
    div.textContent = el.textContent;
    pre.parentElement.replaceChild(div, pre);
  });

  mermaid.run();
}

// Re-render on Material theme instant navigation
var defined = false;
var observer = new MutationObserver(function(mutations) {
  if (typeof mermaid === 'undefined') return;
  // Only act if new pre.mermaid elements appear
  var found = document.querySelector('pre.mermaid code');
  if (found) renderMermaid();
});
observer.observe(document.body, { childList: true, subtree: true });
