/* Theme toggle shared by every page. The choice is remembered per browser when storage is available. */
(function () {
  const root = document.documentElement;
  const sysDark = window.matchMedia('(prefers-color-scheme: dark)');
  let saved = null;
  try { saved = localStorage.getItem('theme'); } catch (e) {}
  if (saved) root.dataset.theme = saved;
  const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : sysDark.matches;
  function wire() {
    const btn = document.getElementById('theme');
    if (!btn) return;
    const label = () => { btn.textContent = isDark() ? 'Switch to light' : 'Switch to dark'; };
    label();
    btn.addEventListener('click', () => {
      root.dataset.theme = isDark() ? 'light' : 'dark';
      try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
      label(); window.dispatchEvent(new Event('themechange'));
    });
    sysDark.addEventListener('change', () => { label(); window.dispatchEvent(new Event('themechange')); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire); else wire();
})();
