// js/app.js — Core Application Controller
// Exposes window.App, window.State, window.Utils as globals (no module bundler needed)

(function () {
  'use strict';

  window.State = {
    currentUser: { name: 'Student', xp: 0 },
    settings: { soundEnabled: true, notifications: true, theme: 'dark' },
    progress: {}
  };

  window.Utils = {
    debounce(func, wait) {
      let timeout;
      return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
      };
    },
    formatTime(seconds) {
      const mins = Math.floor(seconds / 60);
      const secs = seconds % 60;
      return `${mins}:${secs.toString().padStart(2, '0')}`;
    },
    showToast(message, type = 'success', duration = 3000) {
      const existing = document.querySelector('.ecm-toast');
      if (existing) existing.remove();
      const toast = document.createElement('div');
      toast.className = `ecm-toast ecm-toast--${type}`;
      toast.innerHTML = `<i class="fas fa-${type === 'success' ? 'check-circle' : 'info-circle'}"></i> ${message}`;
      toast.style.cssText = `
        position:fixed;bottom:2rem;right:2rem;z-index:9999;
        background:${type === 'success' ? 'var(--color-success, #22c55e)' : 'var(--color-primary, #6366f1)'};
        color:#fff;padding:.75rem 1.5rem;border-radius:.75rem;font-weight:600;
        box-shadow:0 4px 20px rgba(0,0,0,.3);display:flex;align-items:center;gap:.5rem;
        animation:slideInRight .3s ease;
      `;
      document.body.appendChild(toast);
      setTimeout(() => {
        toast.style.animation = 'fadeOut .3s ease forwards';
        setTimeout(() => toast.remove(), 300);
      }, duration);
    },
    confetti() {
      const colors = ['#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#22c55e', '#3b82f6'];
      for (let i = 0; i < 120; i++) {
        setTimeout(() => {
          const el = document.createElement('div');
          el.style.cssText = `
            position:fixed;top:-10px;left:${Math.random()*100}vw;width:8px;height:8px;
            background:${colors[Math.floor(Math.random()*colors.length)]};border-radius:50%;
            z-index:9999;pointer-events:none;animation:confettiFall ${1+Math.random()*2}s linear forwards;
          `;
          document.body.appendChild(el);
          setTimeout(() => el.remove(), 3000);
        }, i * 20);
      }
    }
  };

  window.App = {
    init() {
      this.initTheme();
      this.initScrollProgress();
      this.initBackToTop();
      this.initIntersectionObserver();
      this.initRippleEffect();
      this.initCountUp();
      this.initKeyboardShortcuts();
      this.initMobileNav();
      this.initSearchModal();
      this.initTopbarScrollEffect();
      console.log('%c📚 ECM Course Loaded', 'color:#6366f1;font-weight:bold;font-size:14px;');
    },

    initTheme() {
      const saved = localStorage.getItem('ecm-theme') || 'dark';
      document.documentElement.setAttribute('data-theme', saved);
    },

    initScrollProgress() {
      const bar = document.getElementById('scroll-progress');
      if (!bar) return;
      const update = () => {
        const total = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const pct = total > 0 ? (window.scrollY / total) * 100 : 0;
        bar.style.width = pct + '%';
      };
      window.addEventListener('scroll', update, { passive: true });
    },

    initBackToTop() {
      const btn = document.getElementById('back-to-top');
      if (!btn) return;
      window.addEventListener('scroll', () => {
        btn.classList.toggle('visible', window.scrollY > 400);
      }, { passive: true });
      btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    },

    initTopbarScrollEffect() {
      const topbar = document.querySelector('.topbar');
      if (!topbar) return;
      window.addEventListener('scroll', () => {
        topbar.classList.toggle('scrolled', window.scrollY > 50);
      }, { passive: true });
    },

    initIntersectionObserver() {
      const io = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            e.target.classList.add('active');
            io.unobserve(e.target);
          }
        });
      }, { threshold: 0.1 });
      document.querySelectorAll('.reveal').forEach(el => io.observe(el));
    },

    initRippleEffect() {
      document.addEventListener('click', (e) => {
        const btn = e.target.closest('.ripple');
        if (!btn) return;
        const rect = btn.getBoundingClientRect();
        const ripple = document.createElement('span');
        ripple.className = 'ripple-effect';
        ripple.style.cssText = `left:${e.clientX-rect.left}px;top:${e.clientY-rect.top}px;`;
        btn.appendChild(ripple);
        setTimeout(() => ripple.remove(), 700);
      });
    },

    initCountUp() {
      const io = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (!e.isIntersecting) return;
          const el = e.target;
          const target = +el.getAttribute('data-target');
          let count = 0;
          const step = Math.ceil(target / 80);
          const tick = setInterval(() => {
            count = Math.min(count + step, target);
            el.textContent = count.toLocaleString();
            if (count >= target) clearInterval(tick);
          }, 16);
          io.unobserve(el);
        });
      });
      document.querySelectorAll('.count-up').forEach(el => io.observe(el));
    },

    initKeyboardShortcuts() {
      document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
          e.preventDefault();
          const modal = document.getElementById('search-modal');
          if (modal) {
            modal.classList.toggle('active');
            if (modal.classList.contains('active')) {
              // Build search index immediately when opening
              if (window.Search && !window.Search.built) window.Search.buildIndex();
              const inp = modal.querySelector('input');
              if (inp) setTimeout(() => inp.focus(), 100);
            }
          }
        }
        if (e.key === 'Escape') {
          // Close search modal
          const searchModal = document.getElementById('search-modal');
          if (searchModal) searchModal.classList.remove('active');
          // Close any other modals
          document.querySelectorAll('.modal.active').forEach(m => m.classList.remove('active'));
          // Close mobile nav
          const mobileNav = document.getElementById('mobile-nav');
          if (mobileNav) mobileNav.classList.remove('open');
        }
      });
    },

    initMobileNav() {
      // Accept both id and class selectors for robustness
      const toggle = document.getElementById('mobile-menu-toggle') || document.querySelector('.mobile-menu-toggle');
      const nav = document.getElementById('mobile-nav');
      if (!toggle || !nav) return;
      toggle.addEventListener('click', () => {
        nav.classList.toggle('open');
        toggle.setAttribute('aria-expanded', nav.classList.contains('open'));
      });
      nav.addEventListener('click', (e) => {
        if (e.target.tagName === 'A') nav.classList.remove('open');
      });
    },

    initSearchModal() {
      const modal = document.getElementById('search-modal');
      if (!modal) return;

      // Bind all search-toggle buttons (by class) + the main search-toggle button (by id)
      const openSearch = () => {
        modal.classList.add('active');
        // Build search index on first open
        if (window.Search && !window.Search.built) window.Search.buildIndex();
        const inp = modal.querySelector('input');
        if (inp) setTimeout(() => inp.focus(), 80);
      };

      document.querySelectorAll('.search-toggle, #search-toggle').forEach(btn => {
        btn.addEventListener('click', openSearch);
      });

      // Close on backdrop click
      modal.addEventListener('click', (e) => {
        if (e.target === modal) modal.classList.remove('active');
      });

      // Close button (also handled via onclick in HTML, this is a redundant safety)
      const closeBtn = document.getElementById('search-close');
      if (closeBtn) closeBtn.addEventListener('click', () => modal.classList.remove('active'));
    }
  };

  // Inject global CSS keyframes if not present
  if (!document.getElementById('ecm-app-styles')) {
    const style = document.createElement('style');
    style.id = 'ecm-app-styles';
    style.textContent = `
      @keyframes slideInRight { from{transform:translateX(100px);opacity:0} to{transform:translateX(0);opacity:1} }
      @keyframes fadeOut { to{opacity:0;transform:translateY(10px)} }
      @keyframes confettiFall { to{transform:translateY(110vh) rotate(720deg);opacity:0} }
      .ripple-effect{position:absolute;border-radius:50%;background:rgba(255,255,255,.3);width:100px;height:100px;margin-top:-50px;margin-left:-50px;animation:ripple .7s linear;pointer-events:none;}
      @keyframes ripple{to{transform:scale(4);opacity:0}}
      #back-to-top{display:none;} #back-to-top.visible{display:flex;}
      .topbar.scrolled{background:rgba(15,14,26,.98)!important;box-shadow:0 2px 20px rgba(0,0,0,.3);}
      .ecm-toast{animation:slideInRight .3s ease;}
    `;
    document.head.appendChild(style);
  }

  document.addEventListener('DOMContentLoaded', () => App.init());
})();
