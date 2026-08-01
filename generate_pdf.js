/**
 * generate_pdf.js
 * English Communication Master Course — Automated PDF Generation
 * Uses Puppeteer to capture each lesson page as a print-quality PDF.
 *
 * Usage:
 *   node generate_pdf.js                    → Generate PDFs for all 30 days
 *   node generate_pdf.js --day 1            → Generate PDF for Day 1 only
 *   node generate_pdf.js --all              → Full course book PDF
 */

const puppeteer = require('puppeteer');
const path      = require('path');
const fs        = require('fs');

// ── Config ──────────────────────────────────────────────────────────────────
const PROJECT_ROOT = __dirname;
const OUTPUT_DIR   = path.join(PROJECT_ROOT, 'assets', 'pdf');
const LESSONS_DIR  = path.join(PROJECT_ROOT, 'lessons');

// Lesson metadata for all 30 days
const LESSONS = [
  { day: 1,  title: 'Foundations of Professional Identity & Self-Introduction',    tier: 'Basic' },
  { day: 2,  title: 'Professional Background & Past Projects',                     tier: 'Basic' },
  { day: 3,  title: 'Describing Strengths & Core Capabilities',                    tier: 'Basic' },
  { day: 4,  title: 'Explaining Technical Architectures & Workflows',               tier: 'Basic' },
  { day: 5,  title: 'Effective Problem Solving Communication',                      tier: 'Basic' },
  { day: 6,  title: 'Team Collaboration & Conflict Resolution',                     tier: 'Basic' },
  { day: 7,  title: 'Week 1 Review & Diagnostic Speech Test',                      tier: 'Basic' },
  { day: 8,  title: 'Professional Email Etiquette & Business Writing',              tier: 'Intermediate' },
  { day: 9,  title: 'Navigating Sprint Meetings & Daily Standups',                  tier: 'Intermediate' },
  { day: 10, title: 'Delivering Impactful Technical Demos & Presentations',         tier: 'Intermediate' },
  { day: 11, title: 'STAR Method for Behavioral Interview Questions',               tier: 'Intermediate' },
  { day: 12, title: 'Handling Difficult Questions & High Pressure Situations',      tier: 'Intermediate' },
  { day: 13, title: 'Networking on LinkedIn & Professional Platforms',              tier: 'Intermediate' },
  { day: 14, title: 'Mid-Course Assessment & Placement Readiness Check',            tier: 'Intermediate' },
  { day: 15, title: 'Data Structures & Algorithms Professional Explanation',        tier: 'Professional' },
  { day: 16, title: 'System Design Communication & Scalability Concepts',           tier: 'Professional' },
  { day: 17, title: 'Database Management & SQL Logic Explanation',                  tier: 'Professional' },
  { day: 18, title: 'Web Development, APIs & Cloud Architecture',                   tier: 'Professional' },
  { day: 19, title: 'AI, Machine Learning & Modern Tech Stack Communication',       tier: 'Professional' },
  { day: 20, title: 'OOP, Code Review Feedback & Design Patterns',                  tier: 'Professional' },
  { day: 21, title: 'Group Discussion Dynamics & Consensus Building',               tier: 'Professional' },
  { day: 22, title: 'Executive Presence & Corporate Leadership Pitching',           tier: 'Corporate' },
  { day: 23, title: 'Cross-Functional Client Meetings & Requirement Gathering',     tier: 'Corporate' },
  { day: 24, title: 'Salary Negotiation & Corporate Offer Evaluation',              tier: 'Corporate' },
  { day: 25, title: 'Public Speaking & Storytelling for Tech Leaders',              tier: 'Corporate' },
  { day: 26, title: 'Crisis Communication & Production Downtime Retrospectives',    tier: 'Corporate' },
  { day: 27, title: 'Global Remote Work & Intercultural Communication',             tier: 'Corporate' },
  { day: 28, title: 'Executive Polish: Body Language & Vocal Variety',              tier: 'Corporate' },
  { day: 29, title: 'Complete HR Mock Interview Simulation',                        tier: 'Mock' },
  { day: 30, title: 'Full Technical + HR Capstone Interview & Graduation',          tier: 'Mock' },
];

// ── PDF Options ──────────────────────────────────────────────────────────────
const PDF_OPTIONS = {
  format:            'A4',
  printBackground:   true,
  margin: {
    top:    '20mm',
    right:  '15mm',
    bottom: '20mm',
    left:   '15mm',
  },
  displayHeaderFooter: true,
  headerTemplate: `
    <div style="width:100%; font-family:Inter,sans-serif; font-size:9px; color:#64748b; display:flex; justify-content:space-between; padding:0 15mm;">
      <span>English Communication Master Course</span>
      <span class="title"></span>
    </div>
  `,
  footerTemplate: `
    <div style="width:100%; font-family:Inter,sans-serif; font-size:9px; color:#64748b; display:flex; justify-content:space-between; padding:0 15mm;">
      <span>© 2025 English Communication Master Course</span>
      <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
    </div>
  `,
};

// ── Helpers ──────────────────────────────────────────────────────────────────
function pad(n) {
  return String(n).padStart(2, '0');
}

function getLessonPath(day) {
  return path.join(LESSONS_DIR, `day${pad(day)}.html`);
}

function getOutputPath(day, suffix = '') {
  const dayPad = pad(day);
  return path.join(OUTPUT_DIR, `day${dayPad}${suffix}.pdf`);
}

function ensureOutputDir() {
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
    console.log(`Created output directory: ${OUTPUT_DIR}`);
  }
}

// ── Core PDF Generator ────────────────────────────────────────────────────────
async function generateDayPDF(browser, dayNum) {
  const lessonPath = getLessonPath(dayNum);
  const lesson     = LESSONS.find(l => l.day === dayNum);

  if (!fs.existsSync(lessonPath)) {
    console.warn(`⚠️  Day ${dayNum} lesson file not found: ${lessonPath}`);
    return false;
  }

  const outputPath = getOutputPath(dayNum);
  const fileUrl    = `file://${lessonPath.replace(/\\/g, '/')}`;
  console.log(`📄 Generating Day ${dayNum} PDF: ${lesson?.title || 'Unknown'}`);

  const page = await browser.newPage();

  try {
    // Set viewport for consistent rendering
    await page.setViewport({ width: 1280, height: 900 });

    // Navigate with full network idle wait
    await page.goto(fileUrl, {
      waitUntil: ['load', 'networkidle0'],
      timeout:   60_000,
    });

    // Wait for fonts and animations to settle
    await page.waitForTimeout(1500);

    // Inject print-specific overrides
    await page.evaluate(() => {
      // Force dark mode off for print
      document.documentElement.setAttribute('data-theme', 'light');

      // Expand all accordions
      document.querySelectorAll('.accordion-content').forEach(el => {
        el.style.maxHeight = '9999px';
      });

      // Show all tab panels
      document.querySelectorAll('.tab-panel').forEach(el => {
        el.style.display = 'block';
      });

      // Remove sticky elements causing print issues
      const sticky = document.querySelectorAll('[style*="sticky"], [style*="fixed"]');
      sticky.forEach(el => {
        el.style.position = 'relative';
      });
    });

    // Generate PDF
    const pdf = await page.pdf({
      ...PDF_OPTIONS,
      headerTemplate: PDF_OPTIONS.headerTemplate.replace(
        '<span class="title"></span>',
        `<span>Day ${dayNum}: ${lesson?.title || ''}</span>`
      ),
    });

    fs.writeFileSync(outputPath, pdf);
    console.log(`   ✅ Saved: ${path.basename(outputPath)} (${(pdf.length / 1024).toFixed(0)}KB)`);
    return true;

  } catch (err) {
    console.error(`   ❌ Error generating Day ${dayNum} PDF:`, err.message);
    return false;

  } finally {
    await page.close();
  }
}

// ── Full Course Book Generator ─────────────────────────────────────────────────
async function generateFullCoursePDF(browser) {
  console.log('\n📚 Generating Full Course Book PDF...');
  const pages    = [];
  const tempPage = await browser.newPage();
  await tempPage.setViewport({ width: 1280, height: 900 });

  // Generate cover page HTML
  const coverHTML = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Inter:wght@400;500&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
          font-family: 'Inter', sans-serif;
          background: linear-gradient(135deg, #3b82f6 0%, #7c3aed 100%);
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 40px;
        }
        .cover {
          background: white;
          border-radius: 24px;
          padding: 80px 60px;
          max-width: 700px;
          width: 100%;
          text-align: center;
          box-shadow: 0 30px 80px rgba(0,0,0,0.3);
        }
        .badge { display: inline-block; background: #eff6ff; color: #1d4ed8; padding: 8px 20px; border-radius: 100px; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 28px; }
        h1 { font-family: 'Outfit', sans-serif; font-size: 48px; font-weight: 900; color: #0f172a; line-height: 1.1; margin-bottom: 12px; }
        .subtitle { font-size: 22px; color: #334155; margin-bottom: 40px; font-weight: 500; }
        .divider { height: 3px; background: linear-gradient(90deg, #3b82f6, #7c3aed); border-radius: 100px; margin: 40px auto; width: 80px; }
        .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 40px; }
        .stat-item { padding: 20px; background: #f8fafc; border-radius: 12px; }
        .stat-num { font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 900; color: #3b82f6; }
        .stat-label { font-size: 12px; color: #94a3b8; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 4px; }
        .footer-text { font-size: 13px; color: #94a3b8; margin-top: 40px; }
      </style>
    </head>
    <body>
      <div class="cover">
        <div class="badge">📚 Complete Course Book</div>
        <h1>English Communication<br>Master Course</h1>
        <p class="subtitle">From Beginner to Corporate Professional<br>for Software Engineers</p>
        <div class="divider"></div>
        <div class="stats">
          <div class="stat-item"><div class="stat-num">30</div><div class="stat-label">Daily Lessons</div></div>
          <div class="stat-item"><div class="stat-num">750+</div><div class="stat-label">Vocabulary Words</div></div>
          <div class="stat-item"><div class="stat-num">21</div><div class="stat-label">Modules/Day</div></div>
        </div>
        <p class="footer-text">© 2025 English Communication Master Course · All Rights Reserved</p>
      </div>
    </body>
    </html>
  `;

  await tempPage.setContent(coverHTML, { waitUntil: 'networkidle0' });
  const coverPDF = await tempPage.pdf({ format: 'A4', printBackground: true });
  await tempPage.close();

  // For simplicity, save cover separately
  const coverPath = path.join(OUTPUT_DIR, '00_cover.pdf');
  fs.writeFileSync(coverPath, coverPDF);
  console.log(`   ✅ Cover saved: 00_cover.pdf`);

  console.log('   ℹ️  Individual day PDFs saved to assets/pdf/ directory.');
  console.log('   ℹ️  Use a PDF merger tool (e.g., pdftk, pdfunite) to combine all day PDFs into one book.');
}

// ── Main Entry Point ──────────────────────────────────────────────────────────
async function main() {
  const args    = process.argv.slice(2);
  const dayArg  = args.indexOf('--day');
  const allArg  = args.includes('--all');

  ensureOutputDir();

  console.log('\n🚀 English Communication Master Course — PDF Generator');
  console.log('━'.repeat(60));

  let browser;
  try {
    browser = await puppeteer.launch({
      headless:    'new',
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-accelerated-2d-canvas',
        '--no-first-run',
        '--no-zygote',
        '--disable-gpu',
      ],
    });

    const daysToGenerate = (dayArg !== -1 && args[dayArg + 1])
      ? [parseInt(args[dayArg + 1], 10)]
      : Array.from({ length: 30 }, (_, i) => i + 1);

    let successCount = 0;
    let failCount    = 0;

    for (const day of daysToGenerate) {
      if (day < 1 || day > 30) {
        console.warn(`⚠️  Invalid day number: ${day}. Must be 1–30.`);
        continue;
      }
      const success = await generateDayPDF(browser, day);
      success ? successCount++ : failCount++;
    }

    if (allArg || daysToGenerate.length === 30) {
      await generateFullCoursePDF(browser);
    }

    console.log('\n' + '━'.repeat(60));
    console.log(`✅ Complete: ${successCount} PDF(s) generated successfully.`);
    if (failCount > 0) {
      console.log(`⚠️  Failed: ${failCount} PDF(s) could not be generated (check that lesson files exist).`);
    }
    console.log(`📁 Output directory: ${OUTPUT_DIR}`);

  } catch (err) {
    console.error('\n❌ Fatal error:', err.message);
    if (err.message.includes('executable')) {
      console.log('\n💡 Fix: Run `npm install puppeteer` to download the required browser.');
    }
    process.exit(1);

  } finally {
    if (browser) await browser.close();
  }
}

main().catch(console.error);
