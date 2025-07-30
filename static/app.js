// app.js — injects new inline HTML into #js-content
document.addEventListener('DOMContentLoaded', () => {
  const target = document.getElementById('js-content');

  // New inline HTML content
  target.innerHTML = `
    <h2>Dynamic Content Loaded</h2>
    <p>
      This section was updated by <code>app.js</code> on
      <time datetime="${new Date().toISOString()}">
        ${new Date().toLocaleString()}
      </time>.
    </p>
    <ul>
      <li>Feature A: Fast and responsive</li>
      <li>Feature B: Easy to customize</li>
      <li>Feature C: Lightweight footprint</li>
    </ul>
    <button id="action-btn">Click Me</button>
  `;

  // Example interactivity
  document.getElementById('action-btn').addEventListener('click', () => {
    alert('You clicked the dynamic button!');
  });
});