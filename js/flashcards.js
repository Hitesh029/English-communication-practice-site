// js/flashcards.js — Spaced Repetition Flashcard System
// Exposes window.Flashcards as a global

(function () {
  'use strict';

  window.Flashcards = {
    STORAGE_KEY: 'ecm-flashcards',
    state: {
      cards: [],
      currentIndex: 0,
      isFlipped: false,
      known: [],
      unknown: [],
      dayNum: 1,
      masteredCount: 0,
      reviewMode: false
    },
    touchStartX: 0,
    touchStartY: 0,

    init(dayNum, cards) {
      this.state.dayNum = dayNum;
      this.state.cards = cards || [];
      this.state.currentIndex = 0;
      this.state.isFlipped = false;
      this.state.known = [];
      this.state.unknown = [];
      this.loadSRSData();
      this.render();
      this.bindKeyboard();
      this.bindTouch();
    },

    loadSRSData() {
      try {
        const saved = localStorage.getItem(`${this.STORAGE_KEY}-${this.state.dayNum}`);
        if (saved) {
          const data = JSON.parse(saved);
          this.state.masteredCount = data.masteredCount || 0;
        }
      } catch (e) {}
    },

    saveSRSData() {
      try {
        localStorage.setItem(`${this.STORAGE_KEY}-${this.state.dayNum}`, JSON.stringify({
          masteredCount: this.state.masteredCount,
          knownCards: this.state.known,
          lastStudied: new Date().toISOString()
        }));
      } catch (e) {}
    },

    render() {
      const container = document.getElementById('flashcard-container');
      if (!container) return;

      const { cards, currentIndex, known, unknown } = this.state;
      if (cards.length === 0) {
        container.innerHTML = '<p class="text-muted text-center">No flashcards available for this day yet.</p>';
        return;
      }

      if (currentIndex >= cards.length) {
        this.showSummary();
        return;
      }

      const card = cards[currentIndex];
      const progress = Math.round(((currentIndex) / cards.length) * 100);

      container.innerHTML = `
        <div class="fc-wrapper">
          <div class="fc-meta">
            <span class="fc-counter">${currentIndex + 1} / ${cards.length}</span>
            <span class="fc-known"><i class="fas fa-check-circle" style="color:#22c55e"></i> ${known.length} Known</span>
            <span class="fc-unknown"><i class="fas fa-times-circle" style="color:#ef4444"></i> ${unknown.length} Review</span>
          </div>
          <div class="fc-progress-bar-wrap">
            <div class="fc-progress-bar" style="width:${progress}%"></div>
          </div>
          <div class="card-flip-container${this.state.isFlipped ? ' flipped' : ''}" 
               id="fc-card" 
               onclick="window.Flashcards.flipCard()"
               role="button" tabindex="0" aria-label="Flashcard, click to flip">
            <div class="card-front">
              <div class="fc-tag">Word ${currentIndex + 1}</div>
              <h2 class="fc-word">${card.word || card.front || ''}</h2>
              ${card.ipa ? `<div class="fc-ipa">${card.ipa}</div>` : ''}
              ${card.pos ? `<span class="fc-pos-badge">${card.pos}</span>` : ''}
              <div class="fc-flip-hint"><i class="fas fa-sync-alt"></i> Click to reveal meaning</div>
            </div>
            <div class="card-back">
              <div class="fc-meaning">${card.meaning || card.back || ''}</div>
              ${card.synonyms ? `<div class="fc-synonyms"><strong>Synonyms:</strong> ${Array.isArray(card.synonyms) ? card.synonyms.join(', ') : card.synonyms}</div>` : ''}
              ${card.example_interview ? `<div class="fc-example"><i class="fas fa-briefcase"></i> ${card.example_interview}</div>` : ''}
            </div>
          </div>
          <div class="fc-actions${!this.state.isFlipped ? ' hidden' : ''}">
            <button class="fc-btn fc-btn--unknown ripple" onclick="window.Flashcards.markUnknown()">
              <i class="fas fa-times"></i> Need Review
            </button>
            <button class="fc-btn fc-btn--skip ripple" onclick="window.Flashcards.nextCard()">
              <i class="fas fa-arrow-right"></i> Skip
            </button>
            <button class="fc-btn fc-btn--known ripple" onclick="window.Flashcards.markKnown()">
              <i class="fas fa-check"></i> Got It!
            </button>
          </div>
          <div class="fc-keyboard-hint" style="text-align:center;opacity:.4;font-size:.7rem;margin-top:.5rem">
            Space=flip &nbsp;→=known &nbsp;←=review
          </div>
        </div>
      `;
    },

    flipCard() {
      this.state.isFlipped = !this.state.isFlipped;
      const card = document.getElementById('fc-card');
      if (card) card.classList.toggle('flipped', this.state.isFlipped);
      const actions = document.querySelector('.fc-actions');
      if (actions) actions.classList.toggle('hidden', !this.state.isFlipped);
    },

    nextCard() {
      this.state.currentIndex++;
      this.state.isFlipped = false;
      this.render();
    },

    markKnown() {
      const card = this.state.cards[this.state.currentIndex];
      this.state.known.push(card.word || card.front);
      this.state.masteredCount = Math.max(this.state.masteredCount, this.state.known.length);
      this.saveSRSData();
      this.nextCard();
    },

    markUnknown() {
      const card = this.state.cards[this.state.currentIndex];
      this.state.unknown.push(card.word || card.front);
      this.nextCard();
    },

    prevCard() {
      if (this.state.currentIndex > 0) {
        this.state.currentIndex--;
        this.state.isFlipped = false;
        this.render();
      }
    },

    showSummary() {
      const container = document.getElementById('flashcard-container');
      if (!container) return;
      const { known, unknown, cards } = this.state;
      const pct = Math.round((known.length / cards.length) * 100);

      container.innerHTML = `
        <div class="fc-summary">
          <div class="fc-summary-score">${pct}%</div>
          <h3>Session Complete!</h3>
          <p>You knew <strong>${known.length}</strong> out of <strong>${cards.length}</strong> cards.</p>
          ${unknown.length > 0 ? `
            <div class="fc-review-list">
              <h4>Words to Review (${unknown.length}):</h4>
              <div class="fc-review-tags">
                ${unknown.map(w => `<span class="fc-tag-chip">${w}</span>`).join('')}
              </div>
            </div>
          ` : '<p style="color:#22c55e">🎉 Perfect session! All words known!</p>'}
          <div class="fc-summary-actions">
            <button class="btn btn-secondary ripple" onclick="window.Flashcards.restartReview()">
              <i class="fas fa-redo"></i> Review Missed
            </button>
            <button class="btn btn-primary ripple" onclick="window.Flashcards.restartAll()">
              <i class="fas fa-sync"></i> Restart All
            </button>
          </div>
        </div>
      `;
    },

    restartAll() {
      this.state.currentIndex = 0;
      this.state.isFlipped = false;
      this.state.known = [];
      this.state.unknown = [];
      this.render();
    },

    restartReview() {
      const reviewWords = new Set(this.state.unknown);
      if (reviewWords.size === 0) { this.restartAll(); return; }
      this.state.cards = this.state.cards.filter(c => reviewWords.has(c.word || c.front));
      this.state.currentIndex = 0;
      this.state.isFlipped = false;
      this.state.known = [];
      this.state.unknown = [];
      this.state.reviewMode = true;
      this.render();
    },

    getReviewCards() {
      return this.state.unknown;
    },

    bindKeyboard() {
      document.addEventListener('keydown', (e) => {
        if (!document.getElementById('flashcard-container')) return;
        if (e.key === ' ') { e.preventDefault(); this.flipCard(); }
        if (e.key === 'ArrowRight') { e.preventDefault(); this.state.isFlipped ? this.markKnown() : this.nextCard(); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); this.state.isFlipped ? this.markUnknown() : this.prevCard(); }
      });
    },

    bindTouch() {
      document.addEventListener('touchstart', (e) => {
        this.touchStartX = e.touches[0].clientX;
        this.touchStartY = e.touches[0].clientY;
      }, { passive: true });

      document.addEventListener('touchend', (e) => {
        if (!document.getElementById('fc-card')) return;
        const dx = e.changedTouches[0].clientX - this.touchStartX;
        const dy = Math.abs(e.changedTouches[0].clientY - this.touchStartY);
        if (Math.abs(dx) > 60 && dy < 60) {
          if (dx > 0) { this.state.isFlipped ? this.markKnown() : this.nextCard(); }
          else { this.state.isFlipped ? this.markUnknown() : this.prevCard(); }
        }
      }, { passive: true });
    },

    // Load from data/vocabulary.json and initialize
    loadFromData(dayNum) {
      fetch('../data/vocabulary.json')
        .then(r => r.json())
        .then(data => {
          const cards = (data.days && data.days[dayNum]) || [];
          this.init(dayNum, cards);
        })
        .catch(() => {
          const container = document.getElementById('flashcard-container');
          if (container) container.innerHTML = '<p class="text-muted">Could not load vocabulary cards.</p>';
        });
    }
  };
})();
