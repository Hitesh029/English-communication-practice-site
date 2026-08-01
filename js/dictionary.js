/* ============================================================
   ENGLISH COMMUNICATION MASTER COURSE
   js/dictionary.js — Indian Languages & English Dictionary Module
   ============================================================ */

window.ECM_Dictionary = (function() {
  'use strict';

  const LANG_META = {
    en: { name: 'English', native: 'English', flag: '🇬🇧', speakers: '1.5B+ speakers' },
    hi: { name: 'Hindi', native: 'हिन्दी', flag: '🇮🇳', speakers: '600M+ speakers' },
    bn: { name: 'Bengali', native: 'বাংলা', flag: '🇧🇩', speakers: '270M+ speakers' },
    te: { name: 'Telugu', native: 'తెలుగు', flag: '🟠', speakers: '95M+ speakers' },
    ta: { name: 'Tamil', native: 'தமிழ்', flag: '🟡', speakers: '80M+ speakers' },
    mr: { name: 'Marathi', native: 'मराठी', flag: '🟣', speakers: '95M+ speakers' },
    gu: { name: 'Gujarati', native: 'ગુજરાતી', flag: '🟤', speakers: '60M+ speakers' },
    kn: { name: 'Kannada', native: 'ಕನ್ನಡ', flag: '🔴', speakers: '55M+ speakers' },
    ml: { name: 'Malayalam', native: 'മലയാളം', flag: '🟢', speakers: '38M+ speakers' },
    pa: { name: 'Punjabi', native: 'ਪੰਜਾਬੀ', flag: '🟠', speakers: '130M+ speakers' },
    ur: { name: 'Urdu', native: 'اردو', flag: '🇵🇰', speakers: '70M+ speakers' },
    or: { name: 'Odia', native: 'ଓଡ଼ିଆ', flag: '🔵', speakers: '35M+ speakers' },
    as: { name: 'Assamese', native: 'অসমীয়া', flag: '🟡', speakers: '15M+ speakers' },
    sa: { name: 'Sanskrit', native: 'संस्कृत', flag: '🕉️', speakers: 'Classical' },
    ne: { name: 'Nepali', native: 'नेपाली', flag: '🇳🇵', speakers: '17M+ speakers' },
    sd: { name: 'Sindhi', native: 'سنڌي', flag: '🔶', speakers: '25M+ speakers' }
  };

  const FEATURED_WORDS = [
    { en: 'Articulate', hi: 'स्पष्टवादी' },
    { en: 'Collaborate', hi: 'सहयोग करना' },
    { en: 'Resilient', hi: 'लचीला' },
    { en: 'Professional', hi: 'पेशेवर' },
    { en: 'Innovation', hi: 'नवाचार' },
    { en: 'Leadership', hi: 'नेतृत्व' },
    { en: 'Integrity', hi: 'ईमानदारी' },
    { en: 'Diligent', hi: 'परिश्रमी' },
    { en: 'Eloquent', hi: 'वाकपटु' },
    { en: 'Proactive', hi: 'सक्रिय' },
    { en: 'Enthusiasm', hi: 'उत्साह' },
    { en: 'Competent', hi: 'योग्य' }
  ];

  async function translate(text, fromLang = 'en', toLang = 'hi') {
    if (!text || !text.trim()) return null;
    const pair = `${fromLang}|${toLang}`;
    const url = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text.trim())}&langpair=${pair}`;
    try {
      const res = await fetch(url);
      const data = await res.json();
      if (data.responseStatus === 200 || data.responseStatus === '200') {
        return {
          translatedText: data.responseData.translatedText,
          match: data.responseData.match,
          matches: data.matches || []
        };
      }
      return null;
    } catch (e) {
      console.error('Translation error:', e);
      return null;
    }
  }

  async function getMeaning(word) {
    if (!word || !word.trim()) return null;
    const cleanWord = word.trim().split(/\s+/)[0];
    const url = `https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(cleanWord)}`;
    try {
      const res = await fetch(url);
      if (!res.ok) return null;
      const data = await res.json();
      return data;
    } catch (e) {
      console.error('Meaning error:', e);
      return null;
    }
  }

  function speak(text, lang = 'en') {
    if (!window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = lang === 'hi' ? 'hi-IN' : 'en-US';
    u.rate = 0.85;
    u.pitch = 1.0;
    const voices = window.speechSynthesis.getVoices();
    const voice = voices.find(v => v.lang.startsWith(lang)) || voices.find(v => v.lang.startsWith('en'));
    if (voice) u.voice = voice;
    window.speechSynthesis.speak(u);
  }

  return {
    LANG_META,
    FEATURED_WORDS,
    translate,
    getMeaning,
    speak
  };
})();
