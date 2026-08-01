// js/quiz.js — Complete Quiz Engine
// Exposes window.Quiz as a global

(function () {
  'use strict';

  window.Quiz = {
    state: {
      questions: [],
      currentIndex: 0,
      score: 0,
      startTime: null,
      answered: [],
      dayNum: 1,
      type: 'vocabulary'
    },

    init(containerId, questions, options = {}) {
      const container = document.getElementById(containerId);
      if (!container || !questions || questions.length === 0) return;

      this.state = {
        questions,
        currentIndex: 0,
        score: 0,
        startTime: Date.now(),
        answered: [],
        dayNum: options.day || 1,
        type: options.type || 'vocabulary',
        container,
        onComplete: options.onComplete || null
      };

      this.render();
    },

    render() {
      const { questions, currentIndex, score, container } = this.state;
      if (currentIndex >= questions.length) {
        this.showResults();
        return;
      }

      const q = questions[currentIndex];
      const progress = Math.round(((currentIndex) / questions.length) * 100);

      container.innerHTML = `
        <div class="quiz-wrapper">
          <div class="quiz-header">
            <div class="quiz-progress-wrap">
              <div class="quiz-progress-bar" style="width:${progress}%"></div>
            </div>
            <div class="quiz-meta">
              <span class="quiz-counter">Question ${currentIndex + 1} of ${questions.length}</span>
              <span class="quiz-score">Score: ${score}</span>
            </div>
          </div>
          <div class="quiz-question-card">
            <p class="quiz-question-text">${q.question}</p>
            <div class="quiz-options" id="quiz-options-${currentIndex}">
              ${q.options.map((opt, i) => `
                <button class="quiz-option ripple" data-index="${i}" 
                  onclick="window.Quiz.checkAnswer(${i})">
                  <span class="quiz-opt-letter">${'ABCD'[i]}</span>
                  <span class="quiz-opt-text">${opt}</span>
                </button>
              `).join('')}
            </div>
            <div class="quiz-explanation" id="quiz-explanation" style="display:none;"></div>
          </div>
          <div class="quiz-keyboard-hint" style="font-size:.75rem;opacity:.5;margin-top:.5rem;text-align:center;">
            Press 1, 2, 3, or 4 to answer
          </div>
        </div>
      `;

      // Keyboard shortcuts
      this._keyHandler = (e) => {
        if (['1','2','3','4'].includes(e.key)) {
          const idx = parseInt(e.key) - 1;
          if (idx < q.options.length) this.checkAnswer(idx);
        }
      };
      document.addEventListener('keydown', this._keyHandler);
    },

    checkAnswer(selectedIndex) {
      if (this._keyHandler) {
        document.removeEventListener('keydown', this._keyHandler);
        this._keyHandler = null;
      }

      const { questions, currentIndex } = this.state;
      const q = questions[currentIndex];
      const isCorrect = selectedIndex === q.correct;

      if (isCorrect) this.state.score++;
      this.state.answered.push({ question: q.question, selected: selectedIndex, correct: q.correct, isCorrect });

      // Show feedback on buttons
      const options = document.querySelectorAll('.quiz-option');
      options.forEach((btn, i) => {
        btn.disabled = true;
        btn.onclick = null;
        if (i === q.correct) {
          btn.classList.add('correct');
          btn.innerHTML = `<span class="quiz-opt-letter">✓</span><span class="quiz-opt-text">${q.options[i]}</span>`;
        } else if (i === selectedIndex && !isCorrect) {
          btn.classList.add('incorrect');
          btn.innerHTML = `<span class="quiz-opt-letter">✗</span><span class="quiz-opt-text">${q.options[i]}</span>`;
        }
      });

      // Show explanation
      const explanationEl = document.getElementById('quiz-explanation');
      if (explanationEl) {
        explanationEl.style.display = 'block';
        explanationEl.innerHTML = `
          <div class="explanation-inner ${isCorrect ? 'correct' : 'incorrect'}">
            <i class="fas fa-${isCorrect ? 'check-circle' : 'times-circle'}"></i>
            <strong>${isCorrect ? 'Correct!' : 'Not quite.'}</strong>
            ${q.explanation ? `<p>${q.explanation}</p>` : ''}
          </div>
          <button class="btn-next ripple" onclick="window.Quiz.nextQuestion()" style="margin-top:1rem">
            ${this.state.currentIndex + 1 < questions.length ? 'Next Question →' : 'See Results →'}
          </button>
        `;
      }
    },

    nextQuestion() {
      this.state.currentIndex++;
      this.render();
    },

    showResults() {
      const { questions, score, startTime, answered, container } = this.state;
      const total = questions.length;
      const pct = Math.round((score / total) * 100);
      const timeTaken = Math.round((Date.now() - startTime) / 1000);
      const grade = pct >= 90 ? '🏆 Excellent!' : pct >= 70 ? '✅ Good Job!' : pct >= 50 ? '⚠️ Keep Practicing' : '❌ Review Needed';

      container.innerHTML = `
        <div class="quiz-results">
          <div class="results-grade">${grade}</div>
          <div class="results-score-circle">
            <div class="score-number">${pct}%</div>
            <div class="score-label">${score} / ${total} correct</div>
          </div>
          <div class="results-stats">
            <div class="stat-pill"><i class="fas fa-clock"></i> ${window.Utils ? window.Utils.formatTime(timeTaken) : timeTaken + 's'}</div>
            <div class="stat-pill ${pct >= 70 ? 'good' : 'needs-work'}">
              <i class="fas fa-${pct >= 70 ? 'star' : 'redo'}"></i> ${grade}
            </div>
          </div>
          <div class="results-review">
            <h4>Review</h4>
            ${answered.map((a, i) => `
              <div class="review-item ${a.isCorrect ? 'correct' : 'incorrect'}">
                <i class="fas fa-${a.isCorrect ? 'check' : 'times'}"></i>
                <span>Q${i+1}: ${questions[i].question.substring(0, 60)}...</span>
              </div>
            `).join('')}
          </div>
          <button class="btn btn-primary ripple" onclick="window.Quiz.resetQuiz()" style="margin-top:1.5rem">
            <i class="fas fa-redo"></i> Retake Quiz
          </button>
        </div>
      `;

      // Record score
      if (window.Progress) {
        window.Progress.recordQuizScore(this.state.dayNum, pct);
      }

      if (this.state.onComplete) {
        this.state.onComplete({ score, total, pct, timeTaken });
      }
    },

    resetQuiz() {
      this.state.currentIndex = 0;
      this.state.score = 0;
      this.state.answered = [];
      this.state.startTime = Date.now();
      this.render();
    },

    // Load questions from data/quizzes.json and initialize a quiz
    loadAndInit(containerId, type, dayNum, onComplete) {
      fetch('../data/quizzes.json')
        .then(r => r.json())
        .then(data => {
          const questions = (data[type] && data[type][dayNum]) || [];
          if (questions.length === 0) {
            const el = document.getElementById(containerId);
            if (el) el.innerHTML = '<p class="text-muted">Quiz questions for this day coming soon.</p>';
            return;
          }
          this.init(containerId, questions, { day: dayNum, type, onComplete });
        })
        .catch(() => {
          const el = document.getElementById(containerId);
          if (el) el.innerHTML = '<p class="text-muted">Could not load quiz questions.</p>';
        });
    }
  };
})();
