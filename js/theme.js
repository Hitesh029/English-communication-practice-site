// js/theme.js — Dark / Light Mode Manager
// Exposes window.Theme as a global

(function () {
  'use strict';

  window.Theme = {
    STORAGE_KEY: 'ecm-theme',
    current: 'dark',

    init() {
      // Load saved theme or use system preference
      const saved = localStorage.getItem(this.STORAGE_KEY);
      if (saved) {
        this.current = saved;
      } else {
        const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        this.current = prefersDark ? 'dark' : 'light';
      }
      this.apply(this.current, false);
      this.bindToggleButtons();

      // Listen for system preference changes
      if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
          if (!localStorage.getItem(this.STORAGE_KEY)) {
            this.apply(e.matches ? 'dark' : 'light', true);
          }
        });
      }
    },

    toggle() {
      this.apply(this.current === 'dark' ? 'light' : 'dark', true);
    },

    apply(theme, animate = true) {
      this.current = theme;
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem(this.STORAGE_KEY, theme);

      // Update all toggle button icons
      document.querySelectorAll('.theme-toggle').forEach(btn => {
        const icon = btn.querySelector('i');
        if (icon) {
          if (animate) {
            icon.style.transform = 'rotate(360deg) scale(0)';
            icon.style.transition = 'transform 0.3s ease';
            setTimeout(() => {
              icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
              icon.style.transform = 'rotate(0deg) scale(1)';
            }, 150);
          } else {
            icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
          }
        }
      });

      // Broadcast event for other components to react
      window.dispatchEvent(new CustomEvent('ecm-theme-change', { detail: { theme } }));
    },

    bindToggleButtons() {
      document.querySelectorAll('.theme-toggle').forEach(btn => {
        // Set initial icon
        const icon = btn.querySelector('i');
        if (icon) {
          icon.className = this.current === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
        }
        btn.addEventListener('click', () => this.toggle());
      });
    }
  };

  // Apply theme immediately to avoid FOUC (Flash of Unstyled Content)
  // Run before DOMContentLoaded
  (function applyEarlyTheme() {
    const saved = localStorage.getItem('ecm-theme') ||
      (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', saved);
  })();

  document.addEventListener('DOMContentLoaded', () => window.Theme.init());
})();
