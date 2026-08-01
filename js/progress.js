// js/progress.js — Progress Tracking System
// Exposes window.Progress as a global

(function () {
  'use strict';

  window.Progress = {
    STORAGE_KEY: 'ecm-progress',

    ACHIEVEMENTS: [
      { id: 'first_step',   name: '🎯 First Step',       desc: 'Complete Day 1',           check: (d) => d.completedDays.length >= 1 },
      { id: 'week_warrior', name: '🔥 Week Warrior',      desc: 'Complete 7 days',          check: (d) => d.completedDays.length >= 7 },
      { id: 'halfway',      name: '🏃 Halfway There',     desc: 'Complete 15 days',         check: (d) => d.completedDays.length >= 15 },
      { id: 'champion',     name: '🏆 Course Champion',   desc: 'Complete all 30 days',     check: (d) => d.completedDays.length >= 30 },
      { id: 'streak_3',     name: '⚡ On Fire',           desc: '3-day streak',             check: (d) => d.streak >= 3 },
      { id: 'streak_7',     name: '🌟 Unstoppable',       desc: '7-day streak',             check: (d) => d.streak >= 7 },
      { id: 'vocab_master', name: '📖 Vocab Master',      desc: 'Learn 500+ words',         check: (d) => d.totalWords >= 500 },
      { id: 'quiz_ace',     name: '🎓 Quiz Ace',          desc: 'Score 90%+ on 5 quizzes',  check: (d) => (d.highScores || []).filter(s => s >= 90).length >= 5 }
    ],

    data: {
      completedDays: [],
      dayProgress: {},
      streak: 0,
      lastStudied: null,
      totalWords: 0,
      totalMinutes: 0,
      achievements: [],
      highScores: [],
      xp: 0
    },

    init() {
      this.loadProgress();
      this.updateStreak();
      this.renderUI();
    },

    loadProgress() {
      try {
        const saved = localStorage.getItem(this.STORAGE_KEY);
        if (saved) {
          const parsed = JSON.parse(saved);
          this.data = Object.assign({}, this.data, parsed);
        }
      } catch (e) {
        console.warn('ECM: Could not load progress', e);
      }
    },

    saveProgress() {
      try {
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(this.data));
        window.dispatchEvent(new CustomEvent('ecm-progress-updated', { detail: this.data }));
      } catch (e) {
        console.warn('ECM: Could not save progress', e);
      }
    },

    markDayComplete(day) {
      day = parseInt(day);
      if (!this.data.completedDays.includes(day)) {
        this.data.completedDays.push(day);
        if (!this.data.dayProgress[day]) this.data.dayProgress[day] = {};
        this.data.dayProgress[day].completedAt = new Date().toISOString();
        this.addXP(100);
        this.checkAchievements();
        this.saveProgress();
        window.dispatchEvent(new CustomEvent('ecm-day-complete', { detail: { day } }));
      }
    },

    markModuleComplete(day, moduleName) {
      day = parseInt(day);
      if (!this.data.dayProgress[day]) this.data.dayProgress[day] = { modules: {}, score: 0 };
      if (!this.data.dayProgress[day].modules) this.data.dayProgress[day].modules = {};
      if (!this.data.dayProgress[day].modules[moduleName]) {
        this.data.dayProgress[day].modules[moduleName] = true;
        this.addXP(10);
        this.saveProgress();
      }
    },

    getDayProgress(day) {
      return this.data.dayProgress[parseInt(day)] || null;
    },

    isDayComplete(day) {
      return this.data.completedDays.includes(parseInt(day));
    },

    getOverallProgress() {
      return {
        daysCompleted: this.data.completedDays.length,
        percentage: Math.round((this.data.completedDays.length / 30) * 100),
        xp: this.data.xp,
        streak: this.data.streak,
        totalWords: this.data.totalWords,
        totalMinutes: this.data.totalMinutes,
        achievements: this.data.achievements
      };
    },

    updateStreak() {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const todayMs = today.getTime();

      if (!this.data.lastStudied) {
        this.data.streak = 1;
      } else {
        const last = new Date(this.data.lastStudied);
        last.setHours(0, 0, 0, 0);
        const diffDays = Math.round((todayMs - last.getTime()) / 86400000);
        if (diffDays === 0) {
          // Same day, no change
        } else if (diffDays === 1) {
          this.data.streak += 1;
          this.addXP(this.data.streak * 5);
        } else {
          this.data.streak = 1; // Reset streak
        }
      }
      this.data.lastStudied = new Date().toISOString();
      this.saveProgress();
    },

    addXP(amount) {
      this.data.xp = (this.data.xp || 0) + amount;
    },

    recordQuizScore(day, score) {
      day = parseInt(day);
      if (!this.data.dayProgress[day]) this.data.dayProgress[day] = {};
      this.data.dayProgress[day].score = score;
      if (!this.data.highScores) this.data.highScores = [];
      this.data.highScores.push(score);
      this.checkAchievements();
      this.saveProgress();
    },

    checkAchievements() {
      this.ACHIEVEMENTS.forEach(ach => {
        if (!this.data.achievements.includes(ach.id) && ach.check(this.data)) {
          this.data.achievements.push(ach.id);
          window.dispatchEvent(new CustomEvent('ecm-achievement', { detail: ach }));
          if (window.Utils && window.Utils.showToast) {
            window.Utils.showToast(`🏆 Achievement Unlocked: ${ach.name}`, 'success', 4000);
          }
        }
      });
    },

    getAchievements() {
      return this.ACHIEVEMENTS.map(a => ({
        ...a,
        unlocked: this.data.achievements.includes(a.id)
      }));
    },

    exportProgress() {
      return btoa(JSON.stringify(this.data));
    },

    importProgress(encoded) {
      try {
        const data = JSON.parse(atob(encoded));
        this.data = Object.assign({}, this.data, data);
        this.saveProgress();
        return true;
      } catch (e) {
        console.error('ECM: Failed to import progress', e);
        return false;
      }
    },

    resetProgress() {
      this.data = {
        completedDays: [], dayProgress: {}, streak: 0,
        lastStudied: null, totalWords: 0, totalMinutes: 0,
        achievements: [], highScores: [], xp: 0
      };
      this.saveProgress();
    },

    // Render progress indicators on current page
    renderUI() {
      // Update XP display elements
      document.querySelectorAll('.xp-display').forEach(el => {
        el.textContent = `${this.data.xp} XP`;
      });
      // Update streak display
      document.querySelectorAll('.streak-display').forEach(el => {
        el.textContent = `${this.data.streak} 🔥`;
      });
      // Update days completed
      document.querySelectorAll('.days-completed').forEach(el => {
        el.textContent = this.data.completedDays.length;
      });
      // Update overall progress bars
      const pct = this.getOverallProgress().percentage;
      document.querySelectorAll('.overall-progress-bar').forEach(el => {
        el.style.width = pct + '%';
      });
      document.querySelectorAll('.overall-progress-text').forEach(el => {
        el.textContent = pct + '%';
      });
      // Mark completed day links
      this.data.completedDays.forEach(day => {
        document.querySelectorAll(`[data-day="${day}"]`).forEach(el => {
          el.classList.add('day-complete');
        });
      });
    }
  };

  document.addEventListener('DOMContentLoaded', () => window.Progress.init());
})();
