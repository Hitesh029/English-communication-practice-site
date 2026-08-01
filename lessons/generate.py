import os

out_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons"
os.makedirs(out_dir, exist_ok=True)

def generate_html(day_num, title, tier, grammar_topic, modules_html):
    prev_day = f"day{day_num-1:02d}.html" if day_num > 1 else "day01.html"
    next_day = f"day{day_num+1:02d}.html"
    next_day_num = day_num + 1

    toc_default = """                    <a href="#module-1" class="toc-link" id="toc-module-1"><span class="toc-icon">○</span> 1. Daily Motivation</a>
                    <a href="#module-2" class="toc-link" id="toc-module-2"><span class="toc-icon">○</span> 2. Warm-up Conversation</a>
                    <a href="#module-3" class="toc-link" id="toc-module-3"><span class="toc-icon">○</span> 3. Vocabulary</a>
                    <a href="#module-4" class="toc-link" id="toc-module-4"><span class="toc-icon">○</span> 4. Phrasal Verbs</a>
                    <a href="#module-5" class="toc-link" id="toc-module-5"><span class="toc-icon">○</span> 5. Idioms</a>
                    <a href="#module-6" class="toc-link" id="toc-module-6"><span class="toc-icon">○</span> 6. Grammar</a>
                    <a href="#module-7" class="toc-link" id="toc-module-7"><span class="toc-icon">○</span> 7. Speaking Practice</a>
                    <a href="#module-8" class="toc-link" id="toc-module-8"><span class="toc-icon">○</span> 8. Role-Play Conversations</a>
                    <a href="#module-9" class="toc-link" id="toc-module-9"><span class="toc-icon">○</span> 9. Pronunciation</a>
                    <a href="#module-10" class="toc-link" id="toc-module-10"><span class="toc-icon">○</span> 10. Reading Practice</a>
                    <a href="#module-11" class="toc-link" id="toc-module-11"><span class="toc-icon">○</span> 11. Listening Practice</a>
                    <a href="#module-12" class="toc-link" id="toc-module-12"><span class="toc-icon">○</span> 12. Writing Practice</a>
                    <a href="#module-13" class="toc-link" id="toc-module-13"><span class="toc-icon">○</span> 13. HR Interview Coaching</a>
                    <a href="#module-14" class="toc-link" id="toc-module-14"><span class="toc-icon">○</span> 14. Technical Communication</a>
                    <a href="#module-15" class="toc-link" id="toc-module-15"><span class="toc-icon">○</span> 15. Group Discussion</a>
                    <a href="#module-16" class="toc-link" id="toc-module-16"><span class="toc-icon">○</span> 16. Storytelling Challenge</a>
                    <a href="#module-17" class="toc-link" id="toc-module-17"><span class="toc-icon">○</span> 17. Rapid Fire Challenge</a>
                    <a href="#module-18" class="toc-link" id="toc-module-18"><span class="toc-icon">○</span> 18. Common Indian English Mistakes</a>
                    <a href="#module-19" class="toc-link" id="toc-module-19"><span class="toc-icon">○</span> 19. Daily Revision Quiz</a>
                    <a href="#module-20" class="toc-link" id="toc-module-20"><span class="toc-icon">○</span> 20. Homework</a>
                    <a href="#module-21" class="toc-link" id="toc-module-21"><span class="toc-icon">○</span> 21. Daily Evaluation</a>"""

    toc_day14 = """                    <a href="#module-1" class="toc-link" id="toc-module-1"><span class="toc-icon">○</span> 1. Motivation</a>
                    <a href="#module-2" class="toc-link" id="toc-module-2"><span class="toc-icon">○</span> 2. Comprehensive Assessment</a>
                    <a href="#module-3" class="toc-link" id="toc-module-3"><span class="toc-icon">○</span> 3. Vocabulary Review</a>
                    <a href="#module-4" class="toc-link" id="toc-module-4"><span class="toc-icon">○</span> 4. Phrasal Verbs Review</a>
                    <a href="#module-5" class="toc-link" id="toc-module-5"><span class="toc-icon">○</span> 5. Idioms Review</a>
                    <a href="#module-6" class="toc-link" id="toc-module-6"><span class="toc-icon">○</span> 6. Grammar</a>
                    <a href="#module-7" class="toc-link" id="toc-module-7"><span class="toc-icon">○</span> 7. Speaking</a>
                    <a href="#module-8" class="toc-link" id="toc-module-8"><span class="toc-icon">○</span> 8. Mock HR Role-Play</a>
                    <a href="#module-9" class="toc-link" id="toc-module-9"><span class="toc-icon">○</span> 9. Pronunciation Review</a>
                    <a href="#module-10" class="toc-link" id="toc-module-10"><span class="toc-icon">○</span> 10. Reading</a>
                    <a href="#module-11" class="toc-link" id="toc-module-11"><span class="toc-icon">○</span> 11. Listening</a>
                    <a href="#module-12" class="toc-link" id="toc-module-12"><span class="toc-icon">○</span> 12. Writing</a>
                    <a href="#module-13" class="toc-link" id="toc-module-13"><span class="toc-icon">○</span> 13. HR</a>
                    <a href="#module-14" class="toc-link" id="toc-module-14"><span class="toc-icon">○</span> 14. Technical</a>
                    <a href="#module-15" class="toc-link" id="toc-module-15"><span class="toc-icon">○</span> 15. GD</a>
                    <a href="#module-16" class="toc-link" id="toc-module-16"><span class="toc-icon">○</span> 16. Storytelling</a>
                    <a href="#module-17" class="toc-link" id="toc-module-17"><span class="toc-icon">○</span> 17. Placement Readiness Diagnostic</a>
                    <a href="#module-18" class="toc-link" id="toc-module-18"><span class="toc-icon">○</span> 18. Indian English</a>
                    <a href="#module-19" class="toc-link" id="toc-module-19"><span class="toc-icon">○</span> 19. Quiz</a>
                    <a href="#module-20" class="toc-link" id="toc-module-20"><span class="toc-icon">○</span> 20. Phase 1 & 2 Completion Certificate</a>
                    <a href="#module-21" class="toc-link" id="toc-module-21"><span class="toc-icon">○</span> 21. Evaluation</a>"""

    toc = toc_day14 if day_num == 14 else toc_default

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day {day_num}: {title} - English Communication Master</title>
    <link rel="stylesheet" href="../css/theme.css">
    <link rel="stylesheet" href="../css/app.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #f1f5f9; margin: 0; padding: 0; }}
        .topbar {{ display: flex; justify-content: space-between; padding: 1rem 2rem; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        .topbar a {{ text-decoration: none; color: #333; margin-left: 1rem; font-weight: 500; }}
        .topbar .active {{ color: #2563eb; }}
        
        .lesson-hero {{
            background: linear-gradient(135deg, #1e3a8a, #3b82f6);
            color: white;
            padding: 3rem 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
        }}
        .day-pill {{
            background: rgba(255,255,255,0.2);
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            text-transform: uppercase;
        }}
        .lesson-layout {{
            display: flex;
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .lesson-content {{
            flex: 3;
            min-width: 0;
        }}
        .toc-sidebar {{
            flex: 1;
            position: sticky;
            top: 2rem;
            height: calc(100vh - 4rem);
            overflow-y: auto;
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }}
        .toc-link {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 0;
            color: #475569;
            text-decoration: none;
        }}
        .toc-link.active {{ color: #2563eb; font-weight: bold; }}
        .toc-icon {{ font-size: 1.2rem; }}
        
        .module-section {{
            background: white;
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }}
        .module-title {{ border-bottom: 2px solid #e2e8f0; padding-bottom: 1rem; margin-bottom: 1.5rem; color: #1e293b; }}
        
        .vocab-grid, .idiom-grid, .phrasal-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }}
        .vocab-card, .idiom-card, .phrasal-card, .pronunciation-card {{
            border: 1px solid #e2e8f0;
            padding: 1.5rem;
            border-radius: 8px;
            background: #fafaf9;
        }}
        
        .tag {{
            display: inline-block;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            background: #e2e8f0;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }}
        .tag-interview {{ background: #dbeafe; color: #1e40af; }}
        .tag-tech {{ background: #dcfce7; color: #166534; }}
        .tag-corp {{ background: #fef3c7; color: #92400e; }}
        .tag-daily {{ background: #f3e8ff; color: #6b21a8; }}
        
        .mistake-block {{
            background: #fef2f2;
            border-left: 4px solid #ef4444;
            padding: 1rem;
            margin-bottom: 1rem;
        }}
        
        .dialogue-container {{ display: flex; flex-direction: column; gap: 1rem; background: #f8fafc; padding: 1.5rem; border-radius: 8px; }}
        .dialogue-bubble {{ max-width: 70%; padding: 1rem; border-radius: 12px; }}
        .dialogue-left {{ background: #e0f2fe; align-self: flex-start; border-bottom-left-radius: 0; }}
        .dialogue-right {{ background: #dcfce7; align-self: flex-end; border-bottom-right-radius: 0; }}
        
        textarea, input[type="text"] {{
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            margin-top: 0.5rem;
            font-family: inherit;
        }}
        .btn {{
            background: #2563eb; color: white; padding: 0.5rem 1rem; border: none; border-radius: 6px; cursor: pointer; margin-top: 0.5rem; font-weight: 500;
        }}
        .btn:hover {{ background: #1d4ed8; }}
        .btn-success {{ background: #16a34a; }}
        .btn-success:hover {{ background: #15803d; }}
        .btn-large {{ padding: 1rem 2rem; font-size: 1.2rem; width: 100%; }}
        
        .code-block {{ background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; font-family: monospace; }}
        
        .bottom-nav {{ display: flex; justify-content: space-between; margin-top: 2rem; }}
    </style>
</head>
<body>
    <nav class="topbar">
        <div class="brand"><a href="../index.html">English Comm Master</a></div>
        <div class="nav-links">
            <a href="../dashboard.html">Dashboard</a>
            <a href="../roadmap.html">Roadmap</a>
            <a href="../lessons/day01.html" class="active">Start Learning</a>
        </div>
    </nav>

    <div class="lesson-layout">
        <main class="lesson-content">
            <section class="lesson-hero">
                <div class="breadcrumb">Home &gt; Dashboard &gt; Day {day_num}</div>
                <br>
                <span class="day-pill">DAY {day_num} OF 30</span>
                <h1 style="margin-top: 1rem; font-size: 2.5rem;">{title}</h1>
                <div class="meta-info" style="margin-top: 1rem; opacity: 0.9;">Duration: 60-90 min | 21 Modules | Tier: {tier} | Grammar: {grammar_topic}</div>
                <div class="progress-bar-container" style="background: rgba(255,255,255,0.2); height: 8px; border-radius: 4px; margin-top: 1.5rem;">
                    <div id="hero-progress" style="background: #4ade80; height: 100%; width: 0%; border-radius: 4px; transition: width 0.3s;"></div>
                </div>
                <div style="margin-top: 1.5rem; display: flex; justify-content: space-between;">
                    <button class="btn" style="background: rgba(255,255,255,0.2);" onclick="window.location.href='{prev_day}'">Prev Day</button>
                    <button class="btn" style="background: white; color: #2563eb;" onclick="window.location.href='{next_day}'">Next: Day {next_day_num}</button>
                </div>
            </section>
            
            <aside class="toc-sidebar">
                <h3 style="margin-top: 0;">Modules</h3>
                <div class="toc-list">
{toc}
                </div>
            </aside>

{modules_html}

        </main>
    </div>
    
    <div class="bottom-nav" style="padding: 2rem; max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between;">
        <button class="btn btn-large" style="background: #cbd5e1; width: 48%;" onclick="window.location.href='{prev_day}'">Previous Day</button>
        <button class="btn btn-large" style="width: 48%;" onclick="window.location.href='{next_day}'">Next: Day {next_day_num}</button>
    </div>

    <script src="../js/theme.js"></script>
    <script src="../js/app.js"></script>
    <script src="../js/search.js"></script>
    <script src="../js/progress.js"></script>
    <script src="../js/quiz.js"></script>
    <script src="../js/flashcards.js"></script>
    <script src="../js/pronunciation.js"></script>
    <script>
        // JS Logic
        let timerInterval;
        function startTimer() {{
            clearInterval(timerInterval);
            let timeLeft = 120;
            const display = document.getElementById('timer-display');
            if(!display) return;
            timerInterval = setInterval(() => {{
                if (timeLeft <= 0) {{
                    clearInterval(timerInterval);
                    display.innerHTML = "Time's up!";
                }} else {{
                    let m = Math.floor(timeLeft/60).toString().padStart(2, '0');
                    let s = (timeLeft%60).toString().padStart(2, '0');
                    display.innerHTML = m + ':' + s;
                }}
                timeLeft -= 1;
            }}, 1000);
        }}

        let evalChart;
        function initChart() {{
            const ctx = document.getElementById('evalChart')?.getContext('2d');
            if(!ctx) return;
            evalChart = new Chart(ctx, {{
                type: 'radar',
                data: {{
                    labels: ['Grammar', 'Vocabulary', 'Pronunciation', 'Fluency', 'Confidence', 'Communication', 'Professional English', 'Interview Readiness'],
                    datasets: [{{
                        label: 'Self Evaluation',
                        data: [5, 5, 5, 5, 5, 5, 5, 5],
                        backgroundColor: 'rgba(59, 130, 246, 0.2)',
                        borderColor: 'rgba(59, 130, 246, 1)',
                        borderWidth: 2,
                        pointBackgroundColor: 'rgba(59, 130, 246, 1)'
                    }}]
                }},
                options: {{
                    scales: {{ r: {{ min: 0, max: 10, ticks: {{ stepSize: 1 }} }} }}
                }}
            }});
        }}
        
        function updateChart(index, value) {{
            if(evalChart) {{
                evalChart.data.datasets[0].data[index] = parseInt(value);
                evalChart.update();
            }}
        }}
        
        function saveEvaluation() {{
            if(evalChart) {{
                localStorage.setItem('day{day_num}_eval', JSON.stringify(evalChart.data.datasets[0].data));
                const feedback = document.getElementById('feedback-display');
                if(feedback) feedback.innerText = "Evaluation saved! Great effort today. Focus on your weaker areas tomorrow.";
            }}
        }}

        function markComplete() {{
            localStorage.setItem('day{day_num}_completed', 'true');
            // Confetti
            const confettiScript = document.createElement('script');
            confettiScript.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js";
            confettiScript.onload = () => {{
                confetti({{ particleCount: 150, spread: 70, origin: {{ y: 0.6 }} }});
            }};
            document.head.appendChild(confettiScript);
            
            // Toast
            const toast = document.createElement('div');
            toast.textContent = "Day {day_num} Complete! Excellent Job!";
            toast.style.cssText = "position:fixed; bottom:20px; right:20px; background:#16a34a; color:white; padding:1rem 2rem; border-radius:8px; box-shadow:0 4px 6px rgba(0,0,0,0.1); font-weight:bold; z-index:9999;";
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 4000);
            
            document.querySelectorAll('.toc-link').forEach(l => {{
                const icon = l.querySelector('.toc-icon');
                if(icon) {{
                    icon.innerHTML = '✓';
                    icon.style.color = '#16a34a';
                }}
            }});
        }}
        
        function saveProgress() {{
            // Simple visual persistence logic hook
        }}

        // Scroll spy for TOC
        window.addEventListener('scroll', () => {{
            const sections = document.querySelectorAll('.module-section');
            let current = '';
            sections.forEach(section => {{
                const sectionTop = section.offsetTop;
                if (pageYOffset >= sectionTop - 150) {{
                    current = section.getAttribute('id');
                }}
            }});
            
            document.querySelectorAll('.toc-link').forEach(link => {{
                link.classList.remove('active');
                if (link.getAttribute('href').substring(1) === current) {{
                    link.classList.add('active');
                }}
            }});
            
            // Progress bar
            const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const progress = (window.pageYOffset / docHeight) * 100;
            const bar = document.getElementById('hero-progress');
            if(bar) bar.style.width = progress + '%';
        }});

        // Initialize things
        document.addEventListener('DOMContentLoaded', () => {{
            initChart();
            if (window.Pronunciation) window.Pronunciation.init();
            
            // Rapid Fire auto advance
            const rfInputs = document.querySelectorAll('.rf-input');
            rfInputs.forEach((input, idx) => {{
                input.addEventListener('focus', () => {{
                    setTimeout(() => {{
                        if(idx + 1 < rfInputs.length) {{
                            rfInputs[idx + 1].focus();
                        }}
                    }}, 5000); // 5 sec per question
                }});
            }});
        }});
    </script>
</body>
</html>"""
    
    with open(os.path.join(out_dir, f"day{day_num:02d}.html"), "w", encoding="utf-8") as f:
        f.write(html)

def generate_default_modules(day):
    mods = []
    for i in range(1, 22):
        if i == 21:
            mods.append(f"""            <section id="module-21" class="module-section">
                <h2 class="module-title">Module 21: Daily Evaluation</h2>
                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 300px;">
                        <canvas id="evalChart"></canvas>
                    </div>
                    <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 1rem;">
                        <label>Grammar: <input type="range" min="1" max="10" value="5" oninput="updateChart(0, this.value)" style="width:100%"></label>
                        <label>Vocabulary: <input type="range" min="1" max="10" value="5" oninput="updateChart(1, this.value)" style="width:100%"></label>
                        <label>Pronunciation: <input type="range" min="1" max="10" value="5" oninput="updateChart(2, this.value)" style="width:100%"></label>
                        <label>Fluency: <input type="range" min="1" max="10" value="5" oninput="updateChart(3, this.value)" style="width:100%"></label>
                        <label>Confidence: <input type="range" min="1" max="10" value="5" oninput="updateChart(4, this.value)" style="width:100%"></label>
                        <label>Communication: <input type="range" min="1" max="10" value="5" oninput="updateChart(5, this.value)" style="width:100%"></label>
                        <label>Professional English: <input type="range" min="1" max="10" value="5" oninput="updateChart(6, this.value)" style="width:100%"></label>
                        <label>Interview Readiness: <input type="range" min="1" max="10" value="5" oninput="updateChart(7, this.value)" style="width:100%"></label>
                        <button class="btn btn-success" onclick="saveEvaluation()">Save Evaluation</button>
                    </div>
                </div>
                <div style="margin-top: 2rem; text-align: center;">
                    <div id="feedback-display" style="margin-bottom: 1rem; color: #16a34a; font-weight: bold;"></div>
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete()">Mark Day {day} Complete</button>
                </div>
            </section>""")
        else:
            mods.append(f"""            <section id="module-{i}" class="module-section">
                <h2 class="module-title">Module {i}: Topic {i}</h2>
                <p>Content for module {i} goes here...</p>
            </section>""")
    return "\\n".join(mods)

# Day 12
day12_mods = []
titles_12 = ["Daily Motivation", "Warm-up Conversation", "Vocabulary", "Phrasal Verbs", "Idioms", "Grammar", "Speaking Practice", "Role-Play Conversations", "Pronunciation", "Reading Practice", "Listening Practice", "Writing Practice", "HR Interview Coaching", "Technical Communication", "Group Discussion", "Storytelling Challenge", "Rapid Fire Challenge", "Common Indian English Mistakes", "Daily Revision Quiz", "Homework", "Daily Evaluation"]
for i, t in enumerate(titles_12, 1):
    content = f"<p>Content for {t} goes here...</p>"
    if i == 3:
        content = f"""<p>Vocabulary (25): Deflect, Navigate, Diplomatically, Gracefully, Composure, Tactfully, Strategically, Redirect, Acknowledge, Address, Respond, Handle, Manage, Control, Maintain, Recover, Adapt, Pivot, Clarify, Reframe, Pause, Consider, Thoughtful, Deliberate, Balanced</p>
<div class="vocab-grid">
    <div class="vocab-card"><h3>Deflect</h3><p>Definition...</p></div>
    <div class="vocab-card"><h3>Navigate</h3><p>Definition...</p></div>
</div>"""
    elif i == 4:
        content = "<p>Phrasal Verbs: Buy time, Keep cool, Hold your ground, Brush off, Talk around, Stay composed, Steer away, Turn the tables, Think on your feet, Move past</p>"
    elif i == 5:
        content = "<p>Idioms: Keep your cool, Don't panic, Under pressure, Face the music, Keep a level head, Stand your ground, Keep it together, Bite your tongue, Hold your horses, Weather the storm</p>"
    elif i == 6:
        content = "<p>Grammar: Polite refusal ('I'm afraid I'm not in a position to...', 'While I appreciate...'), hedging language ('It might be the case that...', 'From my perspective...'), diplomatic disagreement ('I see your point, however...'), gap-fill time phrases ('That's an interesting question; let me think...')</p>"
    elif i == 13:
        content = """<h3>HR Q: 'What is your biggest weakness?' and 'Where do you see yourself in 5 years?'</h3>
<div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
    <div style="flex: 1; padding: 1rem; background: #fef2f2; border: 1px solid #ef4444; border-radius: 8px;"><h4 style="color: #ef4444; margin-top:0;">Bad</h4><p>...</p></div>
    <div style="flex: 1; padding: 1rem; background: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px;"><h4 style="color: #f59e0b; margin-top:0;">Good</h4><p>...</p></div>
    <div style="flex: 1; padding: 1rem; background: #f0fdf4; border: 1px solid #22c55e; border-radius: 8px;"><h4 style="color: #22c55e; margin-top:0;">Excellent</h4><p>...</p></div>
</div>"""
    elif i == 14:
        content = "<p>Tech Communication: How to handle 'I don't know the answer' situations gracefully in a technical interview ('While I'm not 100% certain, I believe...')</p>"
    elif i == 15:
        content = "<p>GD Topic: 'Social Media: Is it a Positive or Negative Influence on Society?'</p>"
    elif i == 17:
        content = """<p>Special for Module 17 (Rapid Fire): 20 'curveball' interview questions with 5-second answer training.</p>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
    <input type="text" placeholder="Q1: Quick answer..." style="margin-bottom:0.5rem;" class="rf-input">
    <input type="text" placeholder="Q2: Quick answer..." style="margin-bottom:0.5rem;" class="rf-input">
</div>"""
    elif i == 18:
        content = "<p>Indian English Mistakes (10): Diplomatic language errors.</p>"
    elif i == 21:
        content = f"""                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 300px;">
                        <canvas id="evalChart"></canvas>
                    </div>
                    <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 1rem;">
                        <label>Grammar: <input type="range" min="1" max="10" value="5" oninput="updateChart(0, this.value)" style="width:100%"></label>
                        <button class="btn btn-success" onclick="saveEvaluation()">Save Evaluation</button>
                    </div>
                </div>
                <div style="margin-top: 2rem; text-align: center;">
                    <div id="feedback-display" style="margin-bottom: 1rem; color: #16a34a; font-weight: bold;"></div>
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete()">Mark Day 12 Complete</button>
                </div>"""
        
    day12_mods.append(f"""            <section id="module-{i}" class="module-section">
                <h2 class="module-title">Module {i}: {t}</h2>
                {content}
            </section>""")
            
generate_html(12, "Handling Difficult Questions &amp; High Pressure Situations", "Intermediate", "Polite Refusal, Hedging &amp; Diplomatic Language", "\\n".join(day12_mods))

# Day 13
day13_mods = []
titles_13 = ["Daily Motivation", "Warm-up Conversation", "Vocabulary", "Phrasal Verbs", "Idioms", "Grammar", "Speaking Practice", "Role-Play Conversations", "Pronunciation", "Reading Practice", "Listening Practice", "Writing Practice", "HR Interview Coaching", "Technical Communication", "Group Discussion", "Storytelling Challenge", "Rapid Fire Challenge", "Common Indian English Mistakes", "Daily Revision Quiz", "Homework", "Daily Evaluation"]
for i, t in enumerate(titles_13, 1):
    content = f"<p>Content for {t} goes here...</p>"
    if i == 3: content = "<p>Vocabulary (25): Network, Connection, Endorsement, Recommendation, Portfolio, Profile, Visibility, Brand, Credibility, Outreach, Engagement, Impression, Influence, Presence, Reputation, Authority, Expertise, Recognition, Promotion, Community, Collaboration, Opportunity, Discovery, Pitch, Value</p>"
    elif i == 4: content = "<p>Phrasal Verbs: Reach out to, Connect with, Build up, Put yourself out there, Follow up on, Check in with, Keep in touch, Stand out from, Get noticed, Open up to</p>"
    elif i == 5: content = "<p>Idioms: Make your mark, Put your best foot forward, Cast a wide net, Build bridges, Get your foot in the door, Word of mouth, You never know who's watching, First impressions count, Your network is your net worth, Be on everyone's radar</p>"
    elif i == 6: content = "<p>Grammar: Value proposition statements, professional headline formulas, concise summary writing, active vs passive self-description, strong opening lines for messages</p>"
    elif i == 12: content = "<p>Writing Module 12: Write a LinkedIn connection request message + follow-up message for a recruiter</p><textarea rows='4' placeholder='Your message here...'></textarea>"
    elif i == 13: content = """<h3>HR Q: 'How would you describe yourself professionally?' (LinkedIn-style bio)</h3>
<div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
    <div style="flex: 1; padding: 1rem; background: #fef2f2; border: 1px solid #ef4444; border-radius: 8px;"><h4 style="color: #ef4444; margin-top:0;">Bad</h4><p>...</p></div>
    <div style="flex: 1; padding: 1rem; background: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px;"><h4 style="color: #f59e0b; margin-top:0;">Good</h4><p>...</p></div>
    <div style="flex: 1; padding: 1rem; background: #f0fdf4; border: 1px solid #22c55e; border-radius: 8px;"><h4 style="color: #22c55e; margin-top:0;">Excellent</h4><p>...</p></div>
</div>"""
    elif i == 14: content = "<p>Tech Communication: Writing a technical LinkedIn post that demonstrates expertise without being jargon-heavy</p>"
    elif i == 15: content = "<p>GD Topic: 'Social Networking Sites: Professional Tool or Productivity Killer?'</p>"
    elif i == 18: content = "<p>Indian English Mistakes (10): Common errors in professional self-description and networking messages</p>"
    elif i == 21:
        content = f"""                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 300px;">
                        <canvas id="evalChart"></canvas>
                    </div>
                    <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 1rem;">
                        <label>Grammar: <input type="range" min="1" max="10" value="5" oninput="updateChart(0, this.value)" style="width:100%"></label>
                        <button class="btn btn-success" onclick="saveEvaluation()">Save Evaluation</button>
                    </div>
                </div>
                <div style="margin-top: 2rem; text-align: center;">
                    <div id="feedback-display" style="margin-bottom: 1rem; color: #16a34a; font-weight: bold;"></div>
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete()">Mark Day 13 Complete</button>
                </div>"""
        
    day13_mods.append(f"""            <section id="module-{i}" class="module-section">
                <h2 class="module-title">Module {i}: {t}</h2>
                {content}
            </section>""")

generate_html(13, "Networking on LinkedIn &amp; Professional Platforms", "Intermediate", "Concise Summarization &amp; Professional Self-Promotion", "\\n".join(day13_mods))

# Day 14
day14_mods = []
titles_14 = ["Motivation", "Comprehensive Assessment", "Vocabulary Review", "Phrasal Verbs Review", "Idioms Review", "Grammar", "Speaking", "Mock HR Role-Play", "Pronunciation Review", "Reading", "Listening", "Writing", "HR", "Technical", "GD", "Storytelling", "Placement Readiness Diagnostic", "Indian English", "Quiz", "Phase 1 & 2 Completion Certificate", "Evaluation"]
for i, t in enumerate(titles_14, 1):
    content = f"<p>Content for {t} goes here...</p>"
    if i == 1: content = "<p>'You have completed Phase 1 & 2. You've built a foundation. Now we accelerate.'</p>"
    elif i == 2: content = "<p>15 questions spanning Days 1-13 content (vocabulary, grammar, idioms, phrasal verbs)</p>"
    elif i == 3: content = "<p>Key 25 words from Days 8-13 as compact review cards</p>"
    elif i == 4: content = "<p>10 most important phrasal verbs from Phase 1 & 2</p>"
    elif i == 5: content = "<p>10 most important idioms from Phase 1 & 2</p>"
    elif i == 6: content = "<p>Grammar: Complex Sentences & Relative Clauses - who, which, that, whose, where, when clauses in interview contexts</p>"
    elif i == 7: content = "<p>Speaking: 20 synthesis speaking questions that integrate multiple topics</p>"
    elif i == 8: content = "<p>Mock HR Role-Play: A full 10-turn HR mock interview role-play with evaluator feedback notes</p>"
    elif i == 9: content = "<p>Pronunciation Review: 20 most mispronounced words from Phase 1 & 2</p>"
    elif i == 10: content = "<p>Reading: 'Are You Placement-Ready? A Self-Assessment Checklist for Software Engineers' (400 words)</p>"
    elif i == 11: content = "<p>Listening: Simon Sinek 'How Great Leaders Inspire Action'</p>"
    elif i == 12: content = "<p>Writing: Write a complete 'Tell me about yourself' response (200 words professional bio)</p>"
    elif i == 13: content = "<p>HR: 'Tell me everything about yourself, your skills, and why we should hire you.' Full Excellent model answer.</p>"
    elif i == 14: content = "<p>Technical: Full 5-minute technical self-introduction explaining tech stack, projects, and expertise</p>"
    elif i == 15: content = "<p>GD: 'Technology is Making the World a Better Place - Agree or Disagree?'</p>"
    elif i == 16: content = "<p>Storytelling: Your professional journey story in 2 minutes</p>"
    elif i == 17: content = "<p>Placement Readiness Diagnostic: Comprehensive 30-question diagnostic test</p>"
    elif i == 18: content = "<p>Indian English: 10 most critical mistakes from Phase 1 & 2</p>"
    elif i == 19: content = "<p>Quiz: 10-question comprehensive quiz</p>"
    elif i == 20: content = "<div style='padding:2rem; border:2px solid gold; text-align:center;'><h3>Phase 1 & 2 Completion Certificate</h3><p>Name: <input type='text'></p></div>"
    elif i == 21:
        content = f"""                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 300px;">
                        <canvas id="evalChart"></canvas>
                    </div>
                    <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 1rem;">
                        <label>Grammar: <input type="range" min="1" max="10" value="5" oninput="updateChart(0, this.value)" style="width:100%"></label>
                        <button class="btn btn-success" onclick="saveEvaluation()">Save Evaluation</button>
                    </div>
                </div>
                <div style="margin-top: 2rem; text-align: center;">
                    <div id="feedback-display" style="margin-bottom: 1rem; color: #16a34a; font-weight: bold;"></div>
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete()">Begin Phase 3 - Day 15</button>
                </div>"""
        
    day14_mods.append(f"""            <section id="module-{i}" class="module-section">
                <h2 class="module-title">Module {i}: {t}</h2>
                {content}
            </section>""")

generate_html(14, "Mid-Course Assessment &amp; Placement Readiness Check", "Intermediate", "Complex Sentences &amp; Relative Clauses (Review)", "\\n".join(day14_mods))


# Day 15
day15_mods = []
titles_15 = ["Daily Motivation", "Warm-up Conversation", "Vocabulary", "Phrasal Verbs", "Idioms", "Grammar", "Speaking Practice", "Role-Play Conversations", "Pronunciation", "Reading Practice", "Listening Practice", "Writing Practice", "HR Interview Coaching", "Technical Communication", "Group Discussion", "Storytelling Challenge", "Rapid Fire Challenge", "Common Indian English Mistakes", "Daily Revision Quiz", "Homework", "Daily Evaluation"]
for i, t in enumerate(titles_15, 1):
    content = f"<p>Content for {t} goes here...</p>"
    if i == 3: content = "<p>Vocabulary (25): Array, Linked-list, Stack, Queue, Tree, Graph, Hash, Complexity, Traversal, Recursion, Sorting, Searching, Dynamic, Greedy, Backtracking, Memoization, Optimization, Runtime, Space-complexity, Asymptotic, Binary, Hierarchical, Adjacency, Weighted, Directed</p>"
    elif i == 4: content = "<p>Phrasal Verbs: Break down (complexity), Build up (a solution), Narrow down (options), Filter out, Sort through, Look up, Set up, Point to, Map out, Trace through</p>"
    elif i == 5: content = "<p>Idioms: Building blocks, Step by step, Layer by layer, From the ground up, The bigger picture, Finding the needle in a haystack, All roads lead to Rome, Two birds one stone, In a nutshell, Trade-offs</p>"
    elif i == 6: content = "<p>Grammar: Comparatives/superlatives in technical context ('More efficient than', 'The fastest algorithm', 'Better time complexity'), contrast connectors for tradeoffs</p>"
    elif i == 7: content = "<p>Speaking: 20 questions about explaining data structures (escalating from 'What is an array?' to 'When would you choose a red-black tree over a hash map?')</p>"
    elif i == 8: content = "<p>Role-Plays: Explaining Big O to intern / Justifying algorithm choice to tech lead / Whiteboard interview simulation / System design discussion / Code review feedback on algorithm choice</p>"
    elif i == 10: content = "<p>Reading Article: 'How to Explain Your Algorithm Choices During a Technical Interview' (400 words)</p>"
    elif i == 13: content = """<h3>HR Q: 'How do you approach algorithm design in your projects?'</h3>
<div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
    <div style="flex: 1; padding: 1rem; background: #fef2f2; border: 1px solid #ef4444; border-radius: 8px;"><h4 style="color: #ef4444; margin-top:0;">Bad</h4><p>...</p></div>
    <div style="flex: 1; padding: 1rem; background: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px;"><h4 style="color: #f59e0b; margin-top:0;">Good</h4><p>...</p></div>
    <div style="flex: 1; padding: 1rem; background: #f0fdf4; border: 1px solid #22c55e; border-radius: 8px;"><h4 style="color: #22c55e; margin-top:0;">Excellent</h4><p>...</p></div>
</div>"""
    elif i == 14: content = "<p>Tech Communication: Professional explanation of Array vs LinkedList vs HashMap for different use cases (full English script for technical interview)</p>"
    elif i == 15: content = "<p>GD Topic: 'Should Computer Science Education Focus More on Practical Coding or Theoretical Algorithms?'</p>"
    elif i == 18: content = "<p>Indian English Mistakes (10): Technical communication language errors when explaining algorithms</p>"
    elif i == 21:
        content = f"""                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 300px;">
                        <canvas id="evalChart"></canvas>
                    </div>
                    <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 1rem;">
                        <label>Grammar: <input type="range" min="1" max="10" value="5" oninput="updateChart(0, this.value)" style="width:100%"></label>
                        <button class="btn btn-success" onclick="saveEvaluation()">Save Evaluation</button>
                    </div>
                </div>
                <div style="margin-top: 2rem; text-align: center;">
                    <div id="feedback-display" style="margin-bottom: 1rem; color: #16a34a; font-weight: bold;"></div>
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete()">Mark Day 15 Complete</button>
                </div>"""
        
    day15_mods.append(f"""            <section id="module-{i}" class="module-section">
                <h2 class="module-title">Module {i}: {t}</h2>
                {content}
            </section>""")

generate_html(15, "Data Structures &amp; Algorithms Professional Explanation", "Professional", "Comparatives &amp; Superlatives for Performance Analysis", "\\n".join(day15_mods))

print("Successfully generated all files")
