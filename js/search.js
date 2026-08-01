// js/search.js — Full-Text Search
// Exposes window.Search as a global

(function () {
  'use strict';

  window.Search = {
    index: [],
    built: false,

    RESULT_GROUPS: ['Vocabulary', 'Idiom', 'Phrasal Verb', 'Grammar', 'Lesson'],

    init() {
      this.bindInput();
    },

    async buildIndex() {
      if (this.built) return;
      try {
        const [vocabRes, idiomRes, phrasalRes, grammarRes] = await Promise.all([
          fetch('../data/vocabulary.json').then(r => r.json()).catch(() => null),
          fetch('../data/idioms.json').then(r => r.json()).catch(() => null),
          fetch('../data/phrasal.json').then(r => r.json()).catch(() => null),
          fetch('../data/grammar.json').then(r => r.json()).catch(() => null)
        ]);

        // Index vocabulary
        if (vocabRes && vocabRes.days) {
          Object.entries(vocabRes.days).forEach(([day, words]) => {
            words.forEach(w => {
              this.index.push({
                type: 'Vocabulary',
                title: w.word,
                detail: w.meaning,
                tags: [w.pos, ...(w.synonyms || [])].filter(Boolean).join(', '),
                link: `../lessons/day${day.padStart(2,'0')}.html#module-vocab`,
                day: parseInt(day)
              });
            });
          });
        }

        // Index idioms
        if (idiomRes && idiomRes.days) {
          Object.entries(idiomRes.days).forEach(([day, idioms]) => {
            idioms.forEach(item => {
              this.index.push({
                type: 'Idiom',
                title: item.idiom,
                detail: item.meaning,
                tags: item.example_daily || '',
                link: `../lessons/day${day.padStart(2,'0')}.html#module-idioms`,
                day: parseInt(day)
              });
            });
          });
        }

        // Index phrasal verbs
        if (phrasalRes && phrasalRes.days) {
          Object.entries(phrasalRes.days).forEach(([day, verbs]) => {
            verbs.forEach(v => {
              this.index.push({
                type: 'Phrasal Verb',
                title: v.verb,
                detail: v.meaning,
                tags: v.usage || '',
                link: `../lessons/day${day.padStart(2,'0')}.html#module-phrasal`,
                day: parseInt(day)
              });
            });
          });
        }

        // Index grammar topics
        if (grammarRes && grammarRes.days) {
          Object.entries(grammarRes.days).forEach(([day, grammar]) => {
            this.index.push({
              type: 'Grammar',
              title: grammar.topic,
              detail: grammar.definition,
              tags: (grammar.rules || []).join('; '),
              link: `../lessons/day${day.padStart(2,'0')}.html#module-grammar`,
              day: parseInt(day)
            });
          });
        }

        // Add lesson entries
        const lessonTitles = {
          1: 'Foundations of Professional Identity & Self-Introduction',
          2: 'Professional Background & Past Projects',
          3: 'Describing Strengths & Core Capabilities',
          4: 'Explaining Technical Architectures & Workflows',
          5: 'Effective Problem Solving Communication',
          6: 'Team Collaboration & Conflict Resolution',
          7: 'Week 1 Review & Diagnostic Speech Test',
          8: 'Professional Email Etiquette & Business Writing',
          9: 'Navigating Sprint Meetings & Daily Standups',
          10: 'Delivering Impactful Technical Demos & Presentations',
          11: 'STAR Method for Behavioral Interview Questions',
          12: 'Answering Difficult HR Interview Questions',
          13: 'LinkedIn Profile & Portfolio Communication',
          14: 'Mid-Course Assessment & Communication Audit',
          15: 'Data Structures & Algorithms Communication',
          16: 'System Design Communication',
          17: 'Database Management & SQL Logic',
          18: 'Web Development, APIs & Cloud Architecture',
          19: 'AI, Machine Learning & Modern Tech Stack',
          20: 'OOP, Code Review & Design Patterns',
          21: 'Group Discussion Dynamics & Consensus Building',
          22: 'Executive Presence & Corporate Leadership Pitching',
          23: 'Cross-Functional Client Meetings & Requirement Gathering',
          24: 'Salary Negotiation & Corporate Offer Evaluation',
          25: 'Public Speaking & Storytelling for Tech Leaders',
          26: 'Crisis Communication & Production Downtime Retrospectives',
          27: 'Global Remote Work & Intercultural Communication',
          28: 'Executive Polish: Body Language & Vocal Variety',
          29: 'Full HR Mock Interview Simulation',
          30: 'Graduation: 30-Day Course Completion'
        };

        for (let d = 1; d <= 30; d++) {
          this.index.push({
            type: 'Lesson',
            title: `Day ${d}: ${lessonTitles[d] || ''}`,
            detail: `30-day course lesson ${d}`,
            tags: '',
            link: `../lessons/day${String(d).padStart(2,'0')}.html`,
            day: d
          });
        }

        this.built = true;
      } catch (e) {
        console.warn('ECM Search: Failed to build index', e);
      }
    },

    search(query) {
      if (!query || query.length < 2) return [];
      const q = query.toLowerCase().trim();
      const results = this.index.filter(item => {
        return (item.title && item.title.toLowerCase().includes(q)) ||
               (item.detail && item.detail.toLowerCase().includes(q)) ||
               (item.tags && item.tags.toLowerCase().includes(q));
      });
      // Sort: exact title match first, then by day
      results.sort((a, b) => {
        const aExact = a.title.toLowerCase().startsWith(q) ? -1 : 0;
        const bExact = b.title.toLowerCase().startsWith(q) ? -1 : 0;
        return aExact - bExact || a.day - b.day;
      });
      return results.slice(0, 30);
    },

    highlightMatch(text, query) {
      if (!text || !query) return text || '';
      const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      return text.replace(new RegExp(`(${escaped})`, 'gi'), '<mark>$1</mark>');
    },

    renderResults(results, query, container) {
      if (!container) return;
      if (!results || results.length === 0) {
        container.innerHTML = `<div class="search-empty"><i class="fas fa-search"></i><p>No results for "<strong>${query}</strong>"</p></div>`;
        return;
      }

      // Group by type
      const grouped = {};
      results.forEach(r => {
        if (!grouped[r.type]) grouped[r.type] = [];
        grouped[r.type].push(r);
      });

      let html = `<div class="search-results-count">${results.length} result${results.length !== 1 ? 's' : ''} for "<strong>${query}</strong>"</div>`;
      Object.entries(grouped).forEach(([type, items]) => {
        html += `<div class="search-group"><div class="search-group-label">${type}</div>`;
        items.slice(0, 5).forEach(item => {
          html += `
            <a href="${item.link}" class="search-result-item">
              <div class="sri-title">${this.highlightMatch(item.title, query)}</div>
              ${item.detail ? `<div class="sri-detail">${this.highlightMatch(item.detail.substring(0, 80), query)}...</div>` : ''}
              <div class="sri-meta">Day ${item.day}</div>
            </a>
          `;
        });
        html += '</div>';
      });

      container.innerHTML = html;
    },

    bindInput() {
      const modal = document.getElementById('search-modal');
      if (!modal) return;

      const input = modal.querySelector('input[type="text"], input[type="search"]');
      const resultsContainer = modal.querySelector('.search-results') || (() => {
        const div = document.createElement('div');
        div.className = 'search-results';
        modal.querySelector('.search-modal-inner')?.appendChild(div) || modal.appendChild(div);
        return div;
      })();

      if (!input) return;

      const debouncedSearch = this.debounce(async (query) => {
        if (!this.built) await this.buildIndex();
        const results = this.search(query);
        this.renderResults(results, query, resultsContainer);
      }, 200);

      input.addEventListener('input', (e) => {
        const q = e.target.value.trim();
        if (q.length < 2) {
          resultsContainer.innerHTML = '';
          return;
        }
        debouncedSearch(q);
      });

      // Keyboard navigation in results
      input.addEventListener('keydown', (e) => {
        const items = resultsContainer.querySelectorAll('.search-result-item');
        const focused = resultsContainer.querySelector('.search-result-item:focus');
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          if (!focused) items[0]?.focus();
          else {
            const next = [...items].indexOf(focused) + 1;
            items[next]?.focus();
          }
        }
        if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (focused) {
            const prev = [...items].indexOf(focused) - 1;
            if (prev >= 0) items[prev]?.focus(); else input.focus();
          }
        }
        if (e.key === 'Enter' && focused) focused.click();
      });

      // Build index when modal opens
      modal.addEventListener('transitionend', () => {
        if (modal.classList.contains('active') && !this.built) {
          this.buildIndex();
        }
      });
    },

    debounce(fn, ms) {
      let timer;
      return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), ms);
      };
    }
  };

  document.addEventListener('DOMContentLoaded', () => window.Search.init());
})();
