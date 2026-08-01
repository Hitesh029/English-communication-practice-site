import os

def create_lesson(day, title, tier, prev_day, next_day, grammar, vocab, phrasal, idioms, roleplays, extra_modules):
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day {day}: {title} - English Communication Master</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/responsive.css">
    <link rel="stylesheet" href="../css/animations.css">
    <link rel="stylesheet" href="../css/dark.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #f1f5f9; margin: 0; padding: 0; }}
        .topbar {{ display: flex; justify-content: space-between; padding: 1rem 2rem; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        .topbar a {{ text-decoration: none; color: #333; margin-left: 1rem; font-weight: 500; }}
        .topbar .active {{ color: #2563eb; }}
        .lesson-hero {{ background: linear-gradient(135deg, #1e3a8a, #3b82f6); color: white; padding: 3rem 2rem; border-radius: 12px; margin-bottom: 2rem; }}
        .day-pill {{ background: rgba(255,255,255,0.2); padding: 0.2rem 0.8rem; border-radius: 20px; font-size: 0.8rem; text-transform: uppercase; }}
        .lesson-layout {{ display: flex; gap: 2rem; max-width: 1400px; margin: 0 auto; padding: 2rem; }}
        .lesson-content {{ flex: 3; min-width: 0; }}
        .toc-sidebar {{ flex: 1; position: sticky; top: 2rem; height: calc(100vh - 4rem); overflow-y: auto; background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
        .toc-link {{ display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 0; color: #475569; text-decoration: none; }}
        .toc-link.active {{ color: #2563eb; font-weight: bold; }}
        .module-section {{ background: white; padding: 2rem; border-radius: 12px; margin-bottom: 2rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
        .module-title {{ border-bottom: 2px solid #e2e8f0; padding-bottom: 1rem; margin-bottom: 1.5rem; color: #1e293b; }}
        .vocab-grid, .idiom-grid, .phrasal-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }}
        .vocab-card, .idiom-card, .phrasal-card, .pronunciation-card {{ border: 1px solid #e2e8f0; padding: 1.5rem; border-radius: 8px; background: #fafaf9; }}
        .mistake-block {{ background: #fef2f2; border-left: 4px solid #ef4444; padding: 1rem; margin-bottom: 1rem; }}
        .dialogue-container {{ display: flex; flex-direction: column; gap: 1rem; background: #f8fafc; padding: 1.5rem; border-radius: 8px; }}
        .dialogue-bubble {{ max-width: 70%; padding: 1rem; border-radius: 12px; }}
        .dialogue-left {{ background: #e0f2fe; align-self: flex-start; border-bottom-left-radius: 0; }}
        .dialogue-right {{ background: #dcfce7; align-self: flex-end; border-bottom-right-radius: 0; }}
        textarea, input[type="text"] {{ width: 100%; padding: 0.75rem; border: 1px solid #cbd5e1; border-radius: 6px; margin-top: 0.5rem; font-family: inherit; }}
        .btn {{ background: #2563eb; color: white; padding: 0.5rem 1rem; border: none; border-radius: 6px; cursor: pointer; margin-top: 0.5rem; font-weight: 500; }}
        .btn-success {{ background: #16a34a; }}
        .btn-large {{ padding: 1rem 2rem; font-size: 1.2rem; width: 100%; }}
        .code-block {{ background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; font-family: monospace; }}
    </style>
</head>
<body>
    <nav class="topbar">
        <div class="brand"><a href="../index.html">English Comm Master</a></div>
        <div class="nav-links">
            <a href="../dashboard.html">Dashboard</a>
            <a href="../roadmap.html">Roadmap</a>
            <a href="day{day}.html" class="active">Day {day}</a>
        </div>
        <div class="topbar-actions">
            <button class="search-toggle">🔍</button>
            <button class="theme-toggle">🌙</button>
            <button class="mobile-menu-toggle">☰</button>
        </div>
    </nav>

    <div class="lesson-layout">
        <main class="lesson-content">
            <section class="lesson-hero">
                <div class="breadcrumb">Home > Dashboard > Day {day}</div>
                <br>
                <span class="day-pill">DAY {day} OF 30</span>
                <h1 style="margin-top: 1rem; font-size: 2.5rem;">{title}</h1>
                <div class="meta-info" style="margin-top: 1rem; opacity: 0.9;">⏱️ 60-90 min | 📚 21 Modules | Tier: {tier} | Grammar: {grammar}</div>
                <div class="progress-bar-container" style="background: rgba(255,255,255,0.2); height: 8px; border-radius: 4px; margin-top: 1.5rem;">
                    <div id="hero-progress" style="background: #4ade80; height: 100%; width: 0%; border-radius: 4px; transition: width 0.3s;"></div>
                </div>
                <div style="margin-top: 1.5rem; display: flex; justify-content: space-between;">
                    <button class="btn" style="background: rgba(255,255,255,0.2);" onclick="window.location.href='{prev_day}'">Prev Day</button>
                    <button class="btn" style="background: white; color: #2563eb;" onclick="window.location.href='{next_day}'">Next: Day {int(day)+1}</button>
                </div>
            </section>
            
            <aside class="toc-sidebar">
                <h3 style="margin-top: 0;">Modules</h3>
                <div class="toc-list">
"""
    for i in range(1, 22):
        template += f'                    <a href="#module-{i}" class="toc-link" id="toc-module-{i}"><span class="toc-icon">○</span> {i}. Module {i}</a>\n'

    template += """                </div>
            </aside>
            
            <section id="module-1" class="module-section">
                <h2 class="module-title">Module 1: Mindset Lesson</h2>
                <div style="border-left: 4px solid #3b82f6; padding: 1.5rem; background: linear-gradient(to right, #eff6ff, white); border-radius: 0 8px 8px 0;">
                    <blockquote style="font-size: 1.25rem; font-style: italic; color: #1e3a8a;">""" + extra_modules.get('quote', '"Coming together is a beginning, staying together is progress, working together is success." — Henry Ford') + """</blockquote>
                    <p>""" + extra_modules.get('mindset', 'Focus on collaborative intelligence.') + """</p>
                </div>
            </section>

            <section id="module-2" class="module-section">
                <h2 class="module-title">Module 2: Warm-up Questions</h2>
                <p>Answer the following questions to warm up.</p>
"""
    for i, q in enumerate(extra_modules.get('warmups', ["Warmup question"] * 10), 1):
        template += f'                <div style="margin-bottom: 1rem;"><p>{i}. {q}</p><textarea rows="2" placeholder="Your answer..."></textarea></div>\n'
        
    template += """                <button class="btn" onclick="alert('Great job on the warm-up!')">Submit & Check</button>
            </section>
            
            <section id="module-3" class="module-section">
                <h2 class="module-title">Module 3: Vocabulary</h2>
                <div class="vocab-grid">
"""
    for v in vocab:
        template += f'                    <div class="vocab-card"><h3 style="margin-top: 0;">{v} <button class="btn" style="padding: 0.2rem 0.5rem; font-size: 0.8rem;" onclick="window.Pronunciation?.speak(\'{v}\')">🔊</button></h3><p><strong>Definition:</strong> Professional vocabulary term.</p><textarea rows="2" placeholder="Your sentence..."></textarea></div>\n'

    template += """                </div>
            </section>

            <section id="module-4" class="module-section">
                <h2 class="module-title">Module 4: Phrasal Verbs</h2>
                <div class="phrasal-grid">
"""
    for pv in phrasal:
        template += f'                    <div class="phrasal-card"><h3>{pv}</h3><p><strong>Meaning:</strong> Professional context meaning.</p><input type="text" placeholder="Fill in the blank..."></div>\n'

    template += """                </div>
            </section>
            
            <section id="module-5" class="module-section">
                <h2 class="module-title">Module 5: Idioms</h2>
                <div class="idiom-grid">
"""
    for idm in idioms:
        template += f'                    <div class="idiom-card"><h3>{idm}</h3><p><strong>Meaning:</strong> Idiomatic expression meaning.</p></div>\n'

    template += """                </div>
            </section>
            
            <section id="module-6" class="module-section">
                <h2 class="module-title">Module 6: Grammar & Language</h2>
                <p><strong>Focus:</strong> """ + grammar + """</p>
                <div class="code-block" style="margin: 1rem 0;">
                    Example uses of this grammar in context.
                </div>
                <h3>Exercises</h3>
                <div>
                    <input type="text" placeholder="Practice here..."><br>
                    <button class="btn">Check Answers</button>
                </div>
            </section>

            <section id="module-7" class="module-section">
                <h2 class="module-title">Module 7: Speaking Practice (20 Questions)</h2>
"""
    for i in range(1, 21):
        template += f'                <div style="margin-bottom: 1rem;"><p>{i}. Speaking scenario prompt.</p><button class="btn" style="background:#ef4444;" onclick="this.innerHTML=\'🎙️ Recording...\'">🎤 Record</button><textarea rows="2" placeholder="Or type your notes..."></textarea></div>\n'

    template += """            </section>

            <section id="module-8" class="module-section">
                <h2 class="module-title">Module 8: Role-Play Conversations</h2>
"""
    for rp in roleplays:
        template += f"""                <div style="margin-bottom: 2rem;">
                    <h3>{rp}</h3>
                    <div class="dialogue-container">
                        <div class="dialogue-bubble dialogue-left"><strong>A:</strong> Opening statement.</div>
                        <div class="dialogue-bubble dialogue-right"><strong>B:</strong> Response.</div>
                    </div>
                </div>\n"""

    template += """            </section>

            <section id="module-9" class="module-section">
                <h2 class="module-title">Module 9: Pronunciation</h2>
                <div class="vocab-grid">
"""
    for v in vocab[:20]:
        template += f'                    <div class="pronunciation-card"><h3>{v} <button class="btn" onclick="window.Pronunciation?.speak(\'{v}\')">🔊</button></h3></div>\n'
        
    template += """                </div>
            </section>

            <section id="module-10" class="module-section">
                <h2 class="module-title">Module 10: Reading Practice</h2>
                <h3>Professional Communication Concepts</h3>
                <div style="padding: 1.5rem; background: #f8fafc; border-radius: 8px; line-height: 1.6;">
                    <p>Detailed reading passage about today's topic, covering best practices and strategies.</p>
                </div>
                <h4>Questions</h4>
                <textarea rows="2" placeholder="Q1 Answer..."></textarea>
                <textarea rows="2" placeholder="Q2 Answer..."></textarea>
            </section>

            <section id="module-11" class="module-section">
                <h2 class="module-title">Module 11: Listening Practice</h2>
                <div style="background: #e2e8f0; height: 300px; display: flex; align-items: center; justify-content: center; border-radius: 8px;">
                    <button class="btn btn-large" style="width: auto;">Load Audio/Video Embed</button>
                </div>
                <h4>Focus Questions</h4>
                <textarea rows="4" placeholder="Write your notes..."></textarea>
            </section>

            <section id="module-12" class="module-section">
                <h2 class="module-title">Module 12: Writing Practice</h2>
                <p><strong>Task:</strong> Write a response or summary.</p>
                <textarea rows="6" placeholder="Your attempt here..."></textarea>
            </section>

            <section id="module-13" class="module-section">
                <h2 class="module-title">Module 13: HR Interview Coaching</h2>
                <h3>Question: """ + extra_modules.get('hr_q', 'HR Question?') + """</h3>
                <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                    <div style="flex: 1; padding: 1rem; background: #fef2f2; border: 1px solid #ef4444; border-radius: 8px;">
                        <h4 style="color: #ef4444; margin-top:0;">Bad</h4>
                        <p>Poorly phrased response.</p>
                    </div>
                    <div style="flex: 1; padding: 1rem; background: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px;">
                        <h4 style="color: #f59e0b; margin-top:0;">Good</h4>
                        <p>Adequate response.</p>
                    </div>
                    <div style="flex: 1; padding: 1rem; background: #f0fdf4; border: 1px solid #22c55e; border-radius: 8px;">
                        <h4 style="color: #22c55e; margin-top:0;">Excellent</h4>
                        <p>Perfectly structured, professional response.</p>
                    </div>
                </div>
            </section>

            <section id="module-14" class="module-section">
                <h2 class="module-title">Module 14: Technical Communication</h2>
                <p><strong>Concept:</strong> Integration of technical details.</p>
                <textarea rows="4" placeholder="Practice explaining this concept..."></textarea>
            </section>

            <section id="module-15" class="module-section">
                <h2 class="module-title">Module 15: """ + extra_modules.get('mod15_title', 'Group Discussion Topics') + """</h2>
                <p><strong>Topic 1:</strong> Prepare arguments.</p>
                <textarea rows="4" placeholder="Your arguments..."></textarea>
            </section>

            <section id="module-16" class="module-section">
                <h2 class="module-title">Module 16: Storytelling Challenge</h2>
                <div style="text-align: center; padding: 2rem; background: #1e293b; color: white; border-radius: 8px; margin-bottom: 1rem;">
                    <h2 id="timer-display-{day}" style="margin:0; font-size: 3rem;">02:00</h2>
                    <button class="btn btn-success" onclick="startTimer{day}()" style="margin-top: 1rem; padding: 0.5rem 2rem; font-size: 1.1rem;">Start Timer</button>
                </div>
                <textarea rows="6" placeholder="Write your story script here..."></textarea>
            </section>

            <section id="module-17" class="module-section">
                <h2 class="module-title">Module 17: Rapid Fire Challenge (20 Questions)</h2>
                <p>Answer fast! 5 seconds per question. (Auto-advances)</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
"""
    for i in range(1, 21):
        template += f'                    <input type="text" placeholder="Q{i}: Quick answer..." class="rf-input" id="rf-{day}-{i}">\n'

    template += """                </div>
            </section>

            <section id="module-18" class="module-section">
                <h2 class="module-title">Module 18: Common Indian English Mistakes</h2>
"""
    for i in range(10):
        template += f"""                <div class="mistake-block">
                    <strong>Wrong:</strong> Incorrect phrasing.<br>
                    <strong>Correct:</strong> Proper phrasing.<br>
                    <strong>Explanation:</strong> Why this is incorrect.
                </div>\n"""

    template += """            </section>

            <section id="module-19" class="module-section">
                <h2 class="module-title">Module 19: Daily Revision Quiz</h2>
                <div class="quiz-container" style="background: #f8fafc; padding: 2rem; border-radius: 8px;">
                    <p>Review Quiz</p>
                    <div id="quiz-ui">
                        <h4>Q1: Which of the following is correct?</h4>
                        <button class="btn" style="display:block; width:100%; text-align:left; background: white; color: black; border: 1px solid #ccc; margin-bottom: 0.5rem;" onclick="this.style.background='#ef4444'; this.style.color='white';">A) Wrong choice.</button>
                        <button class="btn" style="display:block; width:100%; text-align:left; background: white; color: black; border: 1px solid #ccc; margin-bottom: 0.5rem;" onclick="this.style.background='#22c55e'; this.style.color='white'; document.getElementById('score-display-{day}').innerText='Score: 1 / 1';">B) Correct choice.</button>
                    </div>
                    <p id="score-display-{day}" style="font-size: 1.2rem; font-weight: bold; margin-top: 1rem;">Score: 0 / 1</p>
                </div>
            </section>

            <section id="module-20" class="module-section">
                <h2 class="module-title">Module 20: Homework</h2>
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox"> Task 1</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox"> Task 2</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox"> Task 3</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox"> Task 4</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox"> Task 5</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox"> Task 6</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox"> Task 7</label></div>
                </div>
            </section>

            <section id="module-21" class="module-section">
                <h2 class="module-title">Module 21: Daily Evaluation</h2>
                <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 300px;">
                        <canvas id="evalChart{day}"></canvas>
                    </div>
                    <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 1rem;">
                        <label>Grammar: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(0, this.value)" style="width:100%"></label>
                        <label>Vocabulary: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(1, this.value)" style="width:100%"></label>
                        <label>Pronunciation: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(2, this.value)" style="width:100%"></label>
                        <label>Fluency: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(3, this.value)" style="width:100%"></label>
                        <label>Confidence: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(4, this.value)" style="width:100%"></label>
                        <label>Communication: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(5, this.value)" style="width:100%"></label>
                        <label>Professional English: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(6, this.value)" style="width:100%"></label>
                        <label>Interview Readiness: <input type="range" min="1" max="10" value="5" oninput="updateChart{day}(7, this.value)" style="width:100%"></label>
                        <button class="btn btn-success" onclick="saveEvaluation{day}()">Save Evaluation</button>
                    </div>
                </div>
                <div style="margin-top: 2rem; text-align: center;">
                    <div id="feedback-display-{day}" style="margin-bottom: 1rem; color: #16a34a; font-weight: bold;"></div>
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete{day}()">Mark Day {day} Complete</button>
                </div>
            </section>
        </main>
        
        <button id="back-to-top" style="position:fixed; bottom:20px; right:20px; display:none; background:#2563eb; color:white; border:none; padding:10px; border-radius:50%; cursor:pointer;" onclick="window.scrollTo(0,0);">↑</button>
    </div>

    <footer style="text-align: center; padding: 2rem; margin-top: 2rem; border-top: 1px solid #e2e8f0; color: #64748b;">
        &copy; 2026 English Communication Master Course. All rights reserved.
    </footer>

    <script src="../js/theme.js"></script>
    <script src="../js/app.js"></script>
    <script src="../js/search.js"></script>
    <script src="../js/progress.js"></script>
    <script src="../js/quiz.js"></script>
    <script src="../js/flashcards.js"></script>
    <script src="../js/pronunciation.js"></script>
    <script>
        let timerInterval{day};
        function startTimer{day}() {{
            clearInterval(timerInterval{day});
            let timeLeft = 120;
            const display = document.getElementById('timer-display-{day}');
            timerInterval{day} = setInterval(() => {{
                if (timeLeft <= 0) {{
                    clearInterval(timerInterval{day});
                    display.innerHTML = "Time's up!";
                }} else {{
                    let m = Math.floor(timeLeft/60).toString().padStart(2, '0');
                    let s = (timeLeft%60).toString().padStart(2, '0');
                    display.innerHTML = m + ':' + s;
                }}
                timeLeft -= 1;
            }}, 1000);
        }}

        let evalChart{day};
        function initChart{day}() {{
            const ctx = document.getElementById('evalChart{day}')?.getContext('2d');
            if(!ctx) return;
            evalChart{day} = new Chart(ctx, {{
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
                options: {{ scales: {{ r: {{ min: 0, max: 10, ticks: {{ stepSize: 1 }} }} }} }}
            }});
        }}
        
        function updateChart{day}(index, value) {{
            if(evalChart{day}) {{
                evalChart{day}.data.datasets[0].data[index] = parseInt(value);
                evalChart{day}.update();
            }}
        }}
        
        function saveEvaluation{day}() {{
            if(evalChart{day}) {{
                localStorage.setItem('day{day}_eval', JSON.stringify(evalChart{day}.data.datasets[0].data));
                document.getElementById('feedback-display-{day}').innerText = "Evaluation saved! Great effort today.";
            }}
        }}

        function markComplete{day}() {{
            localStorage.setItem('day{day}_completed', 'true');
            const confettiScript = document.createElement('script');
            confettiScript.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js";
            confettiScript.onload = () => {{
                confetti({{ particleCount: 150, spread: 70, origin: {{ y: 0.6 }} }});
            }};
            document.head.appendChild(confettiScript);
            
            document.querySelectorAll('.toc-link').forEach(l => {{
                l.querySelector('.toc-icon').innerHTML = '✓';
                l.querySelector('.toc-icon').style.color = '#16a34a';
            }});
        }}

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
            
            const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const progress = (window.pageYOffset / docHeight) * 100;
            const bar = document.getElementById('hero-progress');
            if(bar) bar.style.width = progress + '%';
            
            const btt = document.getElementById('back-to-top');
            if(window.pageYOffset > 500) btt.style.display = 'block';
            else btt.style.display = 'none';
        }});

        document.addEventListener('DOMContentLoaded', () => {{
            initChart{day}();
            if (window.Pronunciation) window.Pronunciation.init();
        }});
    </script>
</body>
</html>
"""
    return template

def generate():
    # Day 21
    vocab_21 = ['Consensus', 'Perspective', 'Standpoint', 'Advocate', 'Oppose', 'Moderate', 'Facilitate', 'Mediate', 'Synthesize', 'Acknowledge', 'Reinforce', 'Challenge', 'Substantiate', 'Counter', 'Propose', 'Support', 'Conclude', 'Summarize', 'Bridge', 'Navigate', 'Resolve', 'Articulate', 'Debate', 'Collaborate', 'Persuade']
    phrasal_21 = ['Build on', 'Back up', 'Sum up', 'Step back', 'Jump in', 'Cut off', 'Move on', 'Round up', 'Open up', 'Wrap up']
    idioms_21 = ['Round table', 'Put it to a vote', 'See eye to eye', 'Middle ground', 'Common ground', 'Agree to disagree', "Devil's advocate", 'Talk in circles', 'Have the floor', 'Meet halfway']
    roleplays_21 = ["4-person GD: 'Is AI threatening software jobs?'", "3-person GD: 'Remote work vs office'", "4-person GD: 'Open source vs proprietary'", "HR-observed GD practice between 3 candidates", "Group consensus-building meeting about tech stack choice"]
    html21 = create_lesson('21', 'Group Discussion Dynamics & Consensus Building', 'Professional', 'day20.html', 'day22.html', 'Discussion language — interrupting politely, conceding a point, building on ideas, steering conclusions', vocab_21, phrasal_21, idioms_21, roleplays_21, {
        'quote': '"Coming together is a beginning, staying together is progress, working together is success." — Henry Ford',
        'mindset': 'Mindset lesson on collaborative intelligence (150 words).',
        'hr_q': 'How do you typically behave in a group discussion?',
        'mod15_title': 'Group Discussion — 5 Full Topic Briefs',
        'warmups': ['Have you ever led a group discussion?', 'How do you handle someone who monopolizes the conversation?'] + ['Warmup ' + str(i) for i in range(3, 11)]
    })
    
    # Day 22
    vocab_22 = ['Visionary', 'Strategic', 'Pioneering', 'Impactful', 'Transformative', 'Revolutionary', 'Compelling', 'Disruptive', 'Scalable', 'Profitable', 'Sustainable', 'Innovative', 'Forward-thinking', 'Data-driven', 'Customer-centric', 'Results-oriented', 'Agile', 'Collaborate', 'Inclusive', 'Accountable', 'Empowering', 'Purpose-driven', 'Mission-critical', 'Growth-oriented', 'Market-leading']
    phrasal_22 = ['Step up', 'Drive forward', 'Build out', 'Scale up', 'Gear up', 'Stand behind', 'Rally around', 'Chart out', 'Lay out', 'Push through']
    idioms_22 = ['Make your mark', 'Raise the bar', 'Move mountains', 'Set the tone', 'Break new ground', 'Lead from the front', 'Punch above your weight', 'Think big', 'Plant the seed', 'Change the game']
    roleplays_22 = ["2-minute elevator pitch to CEO", "Board presentation opener", "Investor Q&A session", "Leadership interview with 'Why should we choose you?'", "Executive self-introduction at industry conference"]
    html22 = create_lesson('22', 'Executive Presence & Corporate Leadership Pitching', 'Corporate', 'day21.html', 'day23.html', "Persuasive rhetoric — rule of three, rhetorical questions, anaphora, power phrases", vocab_22, phrasal_22, idioms_22, roleplays_22, {
        'quote': '"Leadership is not about being in charge. It is about taking care of those in your charge." — Simon Sinek',
        'hr_q': 'Where do you see yourself in 10 years as a tech leader?',
    })
    
    # Day 23
    vocab_23 = ['Requirement', 'Specification', 'Stakeholder', 'Use-case', 'Acceptance', 'Prioritize', 'Scope', 'Constraint', 'Dependency', 'Deliverable', 'Timeline', 'Budget', 'Risk', 'Assumption', 'Issue', 'Change-request', 'Sign-off', 'Baseline', 'Phase', 'Iteration', 'Prototype', 'Wireframe', 'MVP', 'Feedback', 'Approval']
    phrasal_23 = ['Flesh out', 'Map out', 'Nail down', 'Run by', 'Run through', 'Draw up', 'Factor in', 'Rule out', 'Sign off on', 'Iron out']
    idioms_23 = ['Scope creep', 'Moving target', 'On the same page', 'Read between the lines', 'Dot the i\'s and cross the t\'s', 'Get down to brass tacks', 'Ballpark figure', 'Red tape', 'Go back to the drawing board', 'Keep in the loop']
    roleplays_23 = ["Full client requirement gathering meeting", "Scope creep discussion with client", "Budget constraint negotiation", "Technical feasibility explanation", "Stakeholder alignment call"]
    html23 = create_lesson('23', 'Cross-Functional Client Meetings & Requirement Gathering', 'Corporate', 'day22.html', 'day24.html', "Clarifying questions & active listening language", vocab_23, phrasal_23, idioms_23, roleplays_23, {
        'hr_q': 'How do you gather and clarify client requirements without frustrating the client?',
    })
    
    # Day 24
    vocab_24 = ['Compensation', 'Package', 'Benefits', 'Stipend', 'Increment', 'Appraisal', 'Bonus', 'Equity', 'Stock-options', 'Fixed', 'Variable', 'CTC', 'In-hand', 'Gross', 'Net', 'Perks', 'Insurance', 'Leave', 'Flexibility', 'Notice-period', 'Counter-offer', 'Market-rate', 'Band', 'Revision', 'Negotiate']
    phrasal_24 = ['Hold out for', 'Give in', 'Talk down', 'Bargain for', 'Sweeten up', 'Throw in', 'Hold back', 'Settle for', 'Hold firm', 'Walk away']
    idioms_24 = ['Lowball offer', 'Meet halfway', 'Sweeten the deal', 'Put cards on the table', 'Hard bargain', 'Sticking point', 'Take it or leave it', 'Foot in the door', 'Golden handcuffs', 'Blank check']
    roleplays_24 = ["Phone call with recruiter (HR calling with offer)", "In-person HR salary discussion meeting", "Counter-offer discussion email roleplay (written format)", "Joining bonus and benefits negotiation", "Total compensation breakdown query call"]
    html24 = create_lesson('24', 'Salary Negotiation & Corporate Offer Evaluation', 'Corporate', 'day23.html', 'day25.html', "Conditional negotiation language — 'If you could consider...', 'Should you be able to...', 'Given that...'", vocab_24, phrasal_24, idioms_24, roleplays_24, {
        'hr_q': 'What are your salary expectations?',
    })

    with open(r'C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons\day21.html', 'w', encoding='utf-8') as f: f.write(html21)
    with open(r'C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons\day22.html', 'w', encoding='utf-8') as f: f.write(html22)
    with open(r'C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons\day23.html', 'w', encoding='utf-8') as f: f.write(html23)
    with open(r'C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons\day24.html', 'w', encoding='utf-8') as f: f.write(html24)

generate()
