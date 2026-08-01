// js/pronunciation.js — Web Speech API Integration
// Exposes window.Pronunciation as a global

(function () {
  'use strict';

  window.Pronunciation = {
    synth: window.speechSynthesis || null,
    voices: [],
    preferredVoice: null,
    isSpeaking: false,
    recognition: null,

    SETTINGS: {
      rate: 0.85,
      pitch: 1.0,
      volume: 1.0,
      slowRate: 0.55,
      lang: 'en-US'
    },

    init() {
      if (!this.synth) {
        console.warn('ECM Pronunciation: SpeechSynthesis not supported');
        return;
      }
      this.loadVoices();
      if (this.synth.onvoiceschanged !== undefined) {
        this.synth.onvoiceschanged = () => this.loadVoices();
      }
      this.initSpeechRecognition();
    },

    loadVoices() {
      this.voices = this.synth.getVoices();
      // Prefer Google US English > Microsoft US > any en-US
      this.preferredVoice =
        this.voices.find(v => v.name === 'Google US English') ||
        this.voices.find(v => v.name.includes('Microsoft') && v.lang === 'en-US') ||
        this.voices.find(v => v.lang === 'en-US') ||
        this.voices.find(v => v.lang.startsWith('en')) ||
        null;
    },

    speak(text, slow = false) {
      if (!this.synth || !text) return;
      this.synth.cancel();

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = this.SETTINGS.lang;
      utterance.rate = slow ? this.SETTINGS.slowRate : this.SETTINGS.rate;
      utterance.pitch = this.SETTINGS.pitch;
      utterance.volume = this.SETTINGS.volume;
      if (this.preferredVoice) utterance.voice = this.preferredVoice;

      // Visual feedback: find buttons near the source and animate them
      utterance.onstart = () => {
        this.isSpeaking = true;
        this.startVisualizer();
      };
      utterance.onend = () => {
        this.isSpeaking = false;
        this.stopVisualizer();
      };
      utterance.onerror = () => {
        this.isSpeaking = false;
        this.stopVisualizer();
      };

      this.synth.speak(utterance);
    },

    speakSentence(sentence) {
      this.speak(sentence, false);
    },

    stop() {
      if (this.synth) {
        this.synth.cancel();
        this.isSpeaking = false;
        this.stopVisualizer();
      }
    },

    startVisualizer() {
      document.querySelectorAll('.audio-bars').forEach(el => {
        el.classList.add('playing');
      });
      document.querySelectorAll('.pronunciation-btn.active-speaking').forEach(btn => {
        btn.innerHTML = '<i class="fas fa-stop"></i>';
      });
    },

    stopVisualizer() {
      document.querySelectorAll('.audio-bars').forEach(el => {
        el.classList.remove('playing');
      });
    },

    getVoices() {
      return this.voices.filter(v => v.lang.startsWith('en'));
    },

    // Setup pronunciation buttons on the current page
    setupButtons() {
      document.querySelectorAll('[data-speak]').forEach(btn => {
        const text = btn.getAttribute('data-speak');
        const slow = btn.hasAttribute('data-slow');
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          if (this.isSpeaking) {
            this.stop();
            btn.querySelector('i') && (btn.querySelector('i').className = 'fas fa-volume-up');
          } else {
            // Reset all buttons
            document.querySelectorAll('[data-speak] i').forEach(i => i.className = 'fas fa-volume-up');
            btn.classList.add('active-speaking');
            if (btn.querySelector('i')) btn.querySelector('i').className = 'fas fa-stop';
            this.speak(text, slow);
          }
        });
      });

      // Setup shadowing buttons
      document.querySelectorAll('[data-shadow]').forEach(btn => {
        btn.addEventListener('click', () => {
          const text = btn.getAttribute('data-shadow');
          this.startShadowing(text, btn);
        });
      });
    },

    // Speech Recognition for shadowing practice
    initSpeechRecognition() {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) return;

      this.recognition = new SpeechRecognition();
      this.recognition.lang = 'en-US';
      this.recognition.continuous = false;
      this.recognition.interimResults = false;
    },

    startShadowing(targetText, btn) {
      if (!this.recognition) {
        window.Utils && window.Utils.showToast('Speech recognition not supported in this browser', 'info');
        return;
      }
      const originalText = btn.innerHTML;
      btn.innerHTML = '<i class="fas fa-microphone-alt" style="color:#ef4444;animation:pulse 1s infinite;"></i> Listening...';

      this.recognition.start();
      this.recognition.onresult = (event) => {
        const spoken = event.results[0][0].transcript.toLowerCase().trim();
        const target = targetText.toLowerCase().trim();
        const score = this.compareStrings(spoken, target);
        btn.innerHTML = originalText;

        const feedback = score >= 80
          ? `<span style="color:#22c55e">✅ Great! (${score}% match)</span>`
          : score >= 50
            ? `<span style="color:#f59e0b">⚠️ Good try! (${score}% match)</span>`
            : `<span style="color:#ef4444">❌ Try again (${score}% match)</span>`;

        const feedbackEl = btn.parentElement.querySelector('.shadow-feedback') || document.createElement('div');
        feedbackEl.className = 'shadow-feedback';
        feedbackEl.innerHTML = feedback;
        btn.parentElement.appendChild(feedbackEl);
        setTimeout(() => feedbackEl.remove(), 4000);
      };
      this.recognition.onerror = () => { btn.innerHTML = originalText; };
      this.recognition.onend = () => { btn.innerHTML = originalText; };
    },

    compareStrings(a, b) {
      // Simple word-overlap similarity score
      const wordsA = a.split(/\s+/);
      const wordsB = b.split(/\s+/);
      const setB = new Set(wordsB);
      const matches = wordsA.filter(w => setB.has(w)).length;
      return Math.round((matches / Math.max(wordsA.length, wordsB.length)) * 100);
    }
  };

  document.addEventListener('DOMContentLoaded', () => {
    window.Pronunciation.init();
    window.Pronunciation.setupButtons();
  });
})();
