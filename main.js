// Mobile navigation toggle
const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.nav-links');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
}

// Animate bar charts when they scroll into view
const fills = document.querySelectorAll('.bar-fill[data-width]');
const grow = el => { el.style.width = el.dataset.width; };
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { grow(e.target); io.unobserve(e.target); } });
  }, { threshold: 0.3 });
  fills.forEach(f => io.observe(f));
} else {
  fills.forEach(grow);
}

// Footer year
const y = document.getElementById('year');
if (y) y.textContent = new Date().getFullYear();
