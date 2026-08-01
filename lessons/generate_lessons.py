import json
import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - English Communication Master</title>
    <link rel="stylesheet" href="../css/theme.css">
    <link rel="stylesheet" href="../css/app.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
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
            <a href="day{day_num_padded}.html" class="active">Day {day_num}</a>
        </div>
    </nav>

    <div class="lesson-layout">
        <main class="lesson-content">
            <section class="lesson-hero">
                <div class="breadcrumb">Home > Dashboard > Day {day_num}</div>
                <br>
                <span class="day-pill">DAY {day_num} OF 30</span>
                <h1 style="margin-top: 1rem; font-size: 2.5rem;">{topic}</h1>
                <div class="meta-info" style="margin-top: 1rem; opacity: 0.9;">Tier: {tier} | Grammar: {grammar_topic}</div>
                <div class="progress-bar-container" style="background: rgba(255,255,255,0.2); height: 8px; border-radius: 4px; margin-top: 1.5rem;">
                    <div id="hero-progress" style="background: #4ade80; height: 100%; width: 0%; border-radius: 4px; transition: width 0.3s;"></div>
                </div>
                <div style="margin-top: 1.5rem; display: flex; justify-content: space-between;">
                    <button class="btn" style="background: rgba(255,255,255,0.2);" onclick="window.location.href='{prev_link}'">Prev Day</button>
                    <button class="btn" style="background: white; color: #2563eb;" onclick="window.location.href='{next_link}'">Next Day</button>
                </div>
            </section>
            
            <aside class="toc-sidebar">
                <h3 style="margin-top: 0;">Modules</h3>
                <div class="toc-list">
                    <a href="#module-1" class="toc-link" id="toc-module-1"><span class="toc-icon">○</span> 1. Daily Motivation</a>
                    <a href="#module-2" class="toc-link" id="toc-module-2"><span class="toc-icon">○</span> 2. Warm-up Conversation</a>
                    <a href="#module-3" class="toc-link" id="toc-module-3"><span class="toc-icon">○</span> 3. Vocabulary ({vocab_count})</a>
                    <a href="#module-4" class="toc-link" id="toc-module-4"><span class="toc-icon">○</span> 4. Phrasal Verbs</a>
                    <a href="#module-5" class="toc-link" id="toc-module-5"><span class="toc-icon">○</span> 5. Idioms</a>
                    <a href="#module-6" class="toc-link" id="toc-module-6"><span class="toc-icon">○</span> 6. Grammar</a>
                    <a href="#module-7" class="toc-link" id="toc-module-7"><span class="toc-icon">○</span> 7. Speaking Practice ({speaking_count})</a>
                    <a href="#module-8" class="toc-link" id="toc-module-8"><span class="toc-icon">○</span> 8. Role-Play Conversations ({roleplay_count})</a>
                    <a href="#module-9" class="toc-link" id="toc-module-9"><span class="toc-icon">○</span> 9. Pronunciation ({pronunciation_count})</a>
                    <a href="#module-10" class="toc-link" id="toc-module-10"><span class="toc-icon">○</span> 10. Reading Practice</a>
                    <a href="#module-11" class="toc-link" id="toc-module-11"><span class="toc-icon">○</span> 11. Listening Practice</a>
                    <a href="#module-12" class="toc-link" id="toc-module-12"><span class="toc-icon">○</span> 12. Writing Practice</a>
                    <a href="#module-13" class="toc-link" id="toc-module-13"><span class="toc-icon">○</span> 13. HR Interview Coaching</a>
                    <a href="#module-14" class="toc-link" id="toc-module-14"><span class="toc-icon">○</span> 14. Technical Communication</a>
                    <a href="#module-15" class="toc-link" id="toc-module-15"><span class="toc-icon">○</span> 15. Group Discussion</a>
                    <a href="#module-16" class="toc-link" id="toc-module-16"><span class="toc-icon">○</span> 16. Storytelling Challenge</a>
                    <a href="#module-17" class="toc-link" id="toc-module-17"><span class="toc-icon">○</span> 17. Rapid Fire Challenge</a>
                    <a href="#module-18" class="toc-link" id="toc-module-18"><span class="toc-icon">○</span> 18. Common Indian English Mistakes ({mistakes_count})</a>
                    <a href="#module-19" class="toc-link" id="toc-module-19"><span class="toc-icon">○</span> 19. Daily Revision Quiz</a>
                    <a href="#module-20" class="toc-link" id="toc-module-20"><span class="toc-icon">○</span> 20. Homework</a>
                    <a href="#module-21" class="toc-link" id="toc-module-21"><span class="toc-icon">○</span> 21. Daily Evaluation</a>
                </div>
            </aside>
            
            <section id="module-1" class="module-section">
                <h2 class="module-title">Module 1: Daily Motivation</h2>
                <div style="border-left: 4px solid #3b82f6; padding: 1.5rem; background: linear-gradient(to right, #eff6ff, white); border-radius: 0 8px 8px 0;">
                    <blockquote style="font-size: 1.25rem; font-style: italic; color: #1e3a8a;">"Consistency is what transforms average into excellence."</blockquote>
                    <p>Welcome to Day {day_num}! Focus on today's goals and give it your best shot.</p>
                </div>
            </section>
            
            <section id="module-2" class="module-section">
                <h2 class="module-title">Module 2: Warm-up Conversation</h2>
                <p>Answer the following questions to warm up your English muscles.</p>
                <div style="margin-bottom: 1rem;"><p>1. How are you feeling today?</p><textarea rows="2" placeholder="Your answer..."></textarea></div>
                <div style="margin-bottom: 1rem;"><p>2. What is your goal for today's lesson?</p><textarea rows="2" placeholder="Your answer..."></textarea></div>
                <button class="btn" onclick="alert('Great job on the warm-up!')">Submit & Check</button>
            </section>
            
            <section id="module-3" class="module-section">
                <h2 class="module-title">Module 3: Vocabulary</h2>
                <div class="vocab-grid">
                    {vocab_html}
                </div>
            </section>
            
            <section id="module-4" class="module-section">
                <h2 class="module-title">Module 4: Phrasal Verbs</h2>
                <div class="phrasal-grid">
                    {phrasal_html}
                </div>
            </section>
            
            <section id="module-5" class="module-section">
                <h2 class="module-title">Module 5: Idioms</h2>
                <div class="idiom-grid">
                    {idioms_html}
                </div>
            </section>
            
            <section id="module-6" class="module-section">
                <h2 class="module-title">Module 6: Grammar — {grammar_topic}</h2>
                <p><strong>Overview:</strong> {grammar_desc}</p>
                <div class="code-block" style="margin: 1rem 0;">
                    {grammar_examples}
                </div>
                <h3>Exercises</h3>
                <div>
                    <input type="text" placeholder="Practice sentence 1..."><br>
                    <input type="text" placeholder="Practice sentence 2..."><br>
                    <button class="btn">Check Answers</button>
                </div>
            </section>
            
            <section id="module-7" class="module-section">
                <h2 class="module-title">Module 7: Speaking Practice</h2>
                {speaking_html}
            </section>
            
            <section id="module-8" class="module-section">
                <h2 class="module-title">Module 8: Role-Play Conversations</h2>
                {roleplay_html}
            </section>
            
            <section id="module-9" class="module-section">
                <h2 class="module-title">Module 9: Pronunciation</h2>
                <div class="vocab-grid">
                    {pronunciation_html}
                </div>
            </section>
            
            <section id="module-10" class="module-section">
                <h2 class="module-title">Module 10: Reading Practice</h2>
                <h3>{reading_title}</h3>
                <div style="padding: 1.5rem; background: #f8fafc; border-radius: 8px; line-height: 1.6;">
                    <p>{reading_content}</p>
                </div>
                <h4>Questions</h4>
                <textarea rows="2" placeholder="Q1 Answer..."></textarea>
                <textarea rows="2" placeholder="Q2 Answer..."></textarea>
                <h4>Summary Task</h4>
                <textarea rows="4" placeholder="Write a summary..."></textarea>
            </section>
            
            <section id="module-11" class="module-section">
                <h2 class="module-title">Module 11: Listening Practice</h2>
                <p><strong>Recommendation:</strong> {listening_title}</p>
                <div style="background: #e2e8f0; height: 300px; display: flex; align-items: center; justify-content: center; border-radius: 8px;">
                    <button class="btn btn-large" style="width: auto;">Load Media Embed</button>
                </div>
                <h4>Summary Task</h4>
                <textarea rows="4" placeholder="Write a summary of the talk..."></textarea>
            </section>
            
            <section id="module-12" class="module-section">
                <h2 class="module-title">Module 12: Writing Practice</h2>
                <p><strong>Task:</strong> {writing_task}</p>
                <div class="code-block" style="margin: 1rem 0;">
                    {writing_model}
                </div>
                <textarea rows="6" placeholder="Your attempt here..."></textarea>
            </section>
            
            <section id="module-13" class="module-section">
                <h2 class="module-title">Module 13: HR Interview Coaching</h2>
                <h3>Question: "{hr_q}"</h3>
                <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                    <div style="flex: 1; padding: 1rem; background: #fef2f2; border: 1px solid #ef4444; border-radius: 8px;">
                        <h4 style="color: #ef4444; margin-top:0;">Bad</h4>
                        <p>{hr_bad}</p>
                    </div>
                    <div style="flex: 1; padding: 1rem; background: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px;">
                        <h4 style="color: #f59e0b; margin-top:0;">Good</h4>
                        <p>{hr_good}</p>
                    </div>
                    <div style="flex: 1; padding: 1rem; background: #f0fdf4; border: 1px solid #22c55e; border-radius: 8px;">
                        <h4 style="color: #22c55e; margin-top:0;">Excellent</h4>
                        <p>{hr_excellent}</p>
                    </div>
                </div>
                <textarea rows="4" placeholder="Record your own answer..."></textarea>
            </section>
            
            <section id="module-14" class="module-section">
                <h2 class="module-title">Module 14: Technical Communication</h2>
                <p><strong>Concept:</strong> {tech_comm}</p>
                <textarea rows="4" placeholder="Practice explaining this concept..."></textarea>
            </section>
            
            <section id="module-15" class="module-section">
                <h2 class="module-title">Module 15: Group Discussion</h2>
                <h3>Topic: "{gd_topic}"</h3>
                <p><strong>Opening Statement:</strong> Prepare your thoughts on this topic.</p>
                <textarea rows="4" placeholder="Your arguments..."></textarea>
            </section>
            
            <section id="module-16" class="module-section">
                <h2 class="module-title">Module 16: Storytelling Challenge</h2>
                <p><strong>Prompt:</strong> {story_prompt}</p>
                <div style="text-align: center; padding: 2rem; background: #1e293b; color: white; border-radius: 8px; margin-bottom: 1rem;">
                    <h2 id="timer-display" style="margin:0; font-size: 3rem;">02:00</h2>
                    <button class="btn btn-success" onclick="startTimer()" style="margin-top: 1rem; padding: 0.5rem 2rem; font-size: 1.1rem;">Start Timer</button>
                </div>
                <textarea rows="6" placeholder="Write your story script here..."></textarea>
            </section>
            
            <section id="module-17" class="module-section">
                <h2 class="module-title">Module 17: Rapid Fire Challenge (20 Questions)</h2>
                <p>Answer fast! 5 seconds per question. (Auto-advances)</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    {rapid_fire_html}
                </div>
            </section>
            
            <section id="module-18" class="module-section">
                <h2 class="module-title">Module 18: Common Indian English Mistakes</h2>
                {mistakes_html}
            </section>
            
            <section id="module-19" class="module-section">
                <h2 class="module-title">Module 19: Daily Revision Quiz</h2>
                <div class="quiz-container" style="background: #f8fafc; padding: 2rem; border-radius: 8px;">
                    <p>Review Quiz</p>
                    <div id="quiz-ui">
                        <h4>Q1: Quick check question based on today's grammar?</h4>
                        <button class="btn" style="display:block; width:100%; text-align:left; background: white; color: black; border: 1px solid #ccc; margin-bottom: 0.5rem;" onclick="this.style.background='#22c55e'; this.style.color='white'; document.getElementById('score-display').innerText='Score: 1 / 5';">A) Correct Option</button>
                        <button class="btn" style="display:block; width:100%; text-align:left; background: white; color: black; border: 1px solid #ccc; margin-bottom: 0.5rem;" onclick="this.style.background='#ef4444'; this.style.color='white';">B) Incorrect Option</button>
                    </div>
                    <p id="score-display" style="font-size: 1.2rem; font-weight: bold; margin-top: 1rem;">Score: 0 / 5</p>
                </div>
            </section>
            
            <section id="module-20" class="module-section">
                <h2 class="module-title">Module 20: Homework</h2>
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 1. Review flashcards</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 2. Write practice sentences</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 3. Practice shadowing (10 mins)</label></div>
                </div>
            </section>
            
            <section id="module-21" class="module-section">
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
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete()">Mark Day {day_num} Complete</button>
                </div>
            </section>
        </main>
    </div>
    
    <div class="bottom-nav" style="padding: 2rem; max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between;">
        <button class="btn btn-large" style="background: #cbd5e1; width: 48%;" onclick="window.location.href='{prev_link}'">Previous Day</button>
        <button class="btn btn-large" style="width: 48%;" onclick="window.location.href='{next_link}'">Next Day</button>
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
                document.getElementById('feedback-display').innerText = "Evaluation saved! Great effort today. Focus on your weaker areas tomorrow.";
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
                l.querySelector('.toc-icon').innerHTML = '✓';
                l.querySelector('.toc-icon').style.color = '#16a34a';
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

def build_vocab_html(words):
    html = []
    for w in words:
        html.append(f'''
                    <div class="vocab-card">
                        <h3 style="margin-top: 0; display: flex; justify-content: space-between; align-items: center;">{w} <button class="btn" style="padding: 0.2rem 0.5rem; font-size: 0.8rem;" onclick="window.Pronunciation?.speak('{w}')">🔊</button></h3>
                        <p><strong>Definition:</strong> Important term for professional communication.</p>
                        <div style="margin-top: 1rem;">
                            <p><span class="tag tag-corp">Usage</span> "Make sure to use {w} properly in context."</p>
                        </div>
                        <textarea rows="2" placeholder="Write your own sentence using this word..."></textarea>
                    </div>''')
    return "\\n".join(html)

def build_phrasal_html(phrasals):
    html = []
    for p in phrasals:
        html.append(f'''
                    <div class="phrasal-card">
                        <h3>{p}</h3>
                        <p><strong>Meaning:</strong> Professional usage in workplace environments.</p>
                        <ul>
                            <li><span class="tag tag-corp">Office</span> "Let's {p} this afternoon."</li>
                        </ul>
                        <input type="text" placeholder="Fill in the blank...">
                    </div>''')
    return "\\n".join(html)

def build_idioms_html(idioms):
    html = []
    for i in idioms:
        html.append(f'''
                    <div class="idiom-card">
                        <h3>{i}</h3>
                        <p><strong>Meaning:</strong> Common figurative expression in business.</p>
                        <p><span class="tag tag-corp">Corporate</span> "We need to {i} to succeed."</p>
                    </div>''')
    return "\\n".join(html)

def build_speaking_html(count):
    html = []
    for i in range(1, count + 1):
        html.append(f'''
                <div style="margin-bottom: 1rem;"><p>{i}. Scenario Practice {i}</p><button class="btn" style="background:#ef4444;" onclick="this.innerHTML='🎙️ Recording...'">🎤 Record</button><textarea rows="2" placeholder="Or type your notes..."></textarea></div>''')
    return "\\n".join(html)

def build_roleplay_html(roles):
    html = []
    for r in roles:
        html.append(f'''
                <div style="margin-bottom: 2rem;">
                    <h3>Role-Play: {r}</h3>
                    <div class="dialogue-container">
                        <div class="dialogue-bubble dialogue-left"><strong>Partner:</strong> Let's discuss this matter.</div>
                        <div class="dialogue-bubble dialogue-right"><strong>You:</strong> Yes, absolutely.</div>
                        <div class="dialogue-bubble dialogue-left"><strong>Partner:</strong> How should we proceed?</div>
                        <div class="dialogue-bubble dialogue-right"><strong>You:</strong> I recommend we...</div>
                    </div>
                </div>''')
    return "\\n".join(html)

def build_pronunciation_html(words):
    html = []
    for w in words:
        html.append(f'''
                    <div class="pronunciation-card">
                        <h3 style="display: flex; justify-content: space-between; margin-top:0;">{w} <button class="btn" onclick="window.Pronunciation?.speak('{w}')">🔊</button></h3>
                        <p><strong>Shadowing:</strong> "Practice saying {w} clearly."</p>
                    </div>''')
    return "\\n".join(html)

def build_rapid_fire_html(count):
    html = []
    for i in range(1, count + 1):
        html.append(f'<input type="text" placeholder="Q{i}: Quick answer..." style="margin-bottom:0.5rem;" class="rf-input" id="rf-{i}">')
    return "\\n".join(html)

def build_mistakes_html(count, context):
    html = []
    for i in range(1, count + 1):
        html.append(f'''
                <div class="mistake-block">
                    <strong>Wrong:</strong> Common incorrect phrase ({context} #{i}).<br>
                    <strong>Correct:</strong> Better professional alternative.<br>
                    <strong>Explanation:</strong> Explanation for why this is preferred.
                </div>''')
    return "\\n".join(html)

days = [
    {{
        "day_num": 8,
        "day_num_padded": "08",
        "topic": "Professional Email Etiquette & Business Writing",
        "tier": "Intermediate",
        "grammar_topic": "Formal Sentence Structures & Connectors",
        "prev_link": "day07.html",
        "next_link": "day09.html",
        "vocab": ["Correspondence", "Salutation", "Recipient", "Attachment", "Agenda", "Pursuant", "Hereby", "Aforementioned", "Concisely", "Formally", "Professionally", "Acknowledge", "Confirm", "Clarify", "Reiterate", "Summarize", "Enumerate", "Ascertain", "Facilitate", "Coordinate", "Expedite", "Notify", "Convey", "Dispatch", "Transmit"],
        "phrasal": ["Follow up on", "Get back to", "Copy in", "Loop in", "Touch base", "Circle back", "Reach out to", "Wrap up", "Sign off", "Fill in"],
        "idioms": ["Get the ball rolling", "Put something in writing", "Cover your tracks", "Above board", "Touch base", "Read between the lines", "Keep in the loop", "On the same page", "In a nutshell", "Cut to the chase"],
        "grammar_desc": "Formal connectors (Furthermore, However, Nevertheless, Consequently, In addition, Moreover), sentence starters, formal vs informal tone, hedging language, professional email structure",
        "grammar_examples": "Informal: But we can't do it.\\nFormal: However, we are unable to proceed.\\n\\nInformal: Also, we need more time.\\nFormal: Furthermore, additional time is required.",
        "speaking_count": 20,
        "roleplays": ["Apologizing for delay", "Following up on interview", "Requesting information professionally", "Declining invitation professionally", "Thanking a colleague via email"],
        "pronunciation": ["Correspondence", "Acknowledgement", "Pursuant", "Consequently", "Furthermore", "Nevertheless", "Enumerate", "Transmit", "Recipient", "Aforementioned", "Salutation", "Expedite", "Ascertain", "Facilitate", "Coordinate", "Notify", "Reiterate", "Convey", "Dispatch", "Formally"],
        "reading_title": "The Anatomy of a Perfect Professional Email",
        "reading_content": "A perfect professional email is concise, clear, and action-oriented. It begins with a strong subject line, a polite salutation, and immediately addresses the core purpose. Formal language should be used to maintain professionalism, avoiding slang or overly casual phrasing.",
        "listening_title": "TED Talk by Tim Urban 'Inside the Mind of a Master Procrastinator'",
        "writing_task": "Write a professional follow-up email after an interview (150 words).",
        "writing_model": "Dear [Interviewer Name],\\n\\nThank you for taking the time to interview me for the [Position] role at [Company]. I enjoyed learning more about...\\n\\nBest regards,\\n[Your Name]",
        "hr_q": "How do you manage your inbox and professional communications?",
        "hr_bad": "I just answer emails when I see them.",
        "hr_good": "I check my email twice a day and reply to important ones.",
        "hr_excellent": "I prioritize my inbox using labels and rules. I allocate specific blocks of time for communication so it doesn't interrupt deep work.",
        "tech_comm": "How to write a technical incident report email to engineering leadership",
        "gd_topic": "Digital Communication vs Face-to-Face Interaction in Modern Workplaces",
        "story_prompt": "Describe a time when a misunderstood email caused a problem at work/college.",
        "mistakes_count": 10,
        "mistakes_context": "Email error"
    }},
    {{
        "day_num": 9,
        "day_num_padded": "09",
        "topic": "Navigating Sprint Meetings & Daily Standups",
        "tier": "Intermediate",
        "grammar_topic": "Future Tenses (will/going to/Present Continuous)",
        "prev_link": "day08.html",
        "next_link": "day10.html",
        "vocab": ["Sprint", "Standup", "Retrospective", "Burndown", "Velocity", "Epic", "Backlog", "Blockers", "Deliverable", "Capacity", "Estimation", "Grooming", "Planning", "Review", "Demo", "Release", "Increment", "Scrum", "Kanban", "Waterfall", "Milestone", "Deadline", "Dependency", "Refinement", "Acceptance"],
        "phrasal": ["Stand up for", "Wrap up", "Pick up slack", "Sign off on", "Carry over", "Block out", "Schedule in", "Build in", "Flag up", "Check off"],
        "idioms": ["Move the goalposts", "Drop the ball", "In the pipeline", "On track", "Behind schedule", "Light at the end of the tunnel", "Up and running", "Ahead of the curve", "Breaking ground", "Keep the momentum"],
        "grammar_desc": "Future tenses - will (spontaneous decisions), going to (planned intentions), Present Continuous (fixed arrangements), Future Perfect, Future Continuous",
        "grammar_examples": "I will fix it now. (Spontaneous)\\nI am going to start the new epic tomorrow. (Intention)\\nWe are deploying the app at 5 PM. (Fixed arrangement)",
        "speaking_count": 20,
        "roleplays": ["Daily Standup Update", "Sprint Planning", "Retrospective Feedback", "Reporting a Blocker", "Demoing a Feature"],
        "pronunciation": ["Sprint", "Standup", "Retrospective", "Burndown", "Velocity", "Epic", "Backlog", "Blockers", "Deliverable", "Capacity", "Estimation", "Grooming", "Planning", "Review", "Demo", "Release", "Increment", "Scrum", "Kanban", "Waterfall"],
        "reading_title": "How High-Performing Software Teams Run Sprint Ceremonies",
        "reading_content": "Sprint ceremonies are essential for agile teams to sync up, plan, and review their work. Effective standups are brief, focusing on progress and blockers without diving into deep problem-solving.",
        "listening_title": "Agile Methodology Explained",
        "writing_task": "Write a sprint retrospective summary.",
        "writing_model": "In this sprint, we successfully delivered the authentication module. What went well: team collaboration. What could be improved: code review turnaround time.",
        "hr_q": "How do you handle sprint planning when requirements keep changing?",
        "hr_bad": "I get frustrated and complain.",
        "hr_good": "I try to adapt and work on the new requirements.",
        "hr_excellent": "I communicate with the product owner to understand the priority of the changes, re-estimate the effort, and negotiate what can be moved to the backlog to accommodate the new scope.",
        "tech_comm": "Explaining your sprint standup update using Yesterday/Today/Blockers format in professional English",
        "gd_topic": "Agile vs Waterfall: Which Methodology is Better for Large-Scale Enterprise Software?",
        "story_prompt": "Describe a time when you overcame a significant blocker during a sprint.",
        "mistakes_count": 10,
        "mistakes_context": "Meeting communication error"
    }},
    {{
        "day_num": 10,
        "day_num_padded": "10",
        "topic": "Delivering Impactful Technical Demos & Presentations",
        "tier": "Intermediate",
        "grammar_topic": "Signposting & Transition Language",
        "prev_link": "day09.html",
        "next_link": "day11.html",
        "vocab": ["Demonstrate", "Showcase", "Illustrate", "Highlight", "Emphasize", "Clarify", "Summarize", "Conclude", "Transition", "Engage", "Captivate", "Articulate", "Convey", "Present", "Structure", "Framework", "Overview", "Walkthrough", "Handoff", "Q&A", "Feedback", "Iteration", "Polish", "Delivery", "Impact"],
        "phrasal": ["Walk through", "Break down", "Zoom in on", "Sum up", "Wrap up", "Kick off", "Build up", "Come across", "Stand out", "Follow up"],
        "idioms": ["Get to the point", "Paint a picture", "Steal the show", "Hit the nail on the head", "Leave on a high note", "Set the stage", "Capture attention", "Drive the point home", "Make or break", "Command the room"],
        "grammar_desc": "Signposting language - 'To begin with', 'Moving on to', 'As I mentioned earlier', 'To summarize', transition connectors in presentations",
        "grammar_examples": "To begin with, let's look at the architecture.\\nMoving on to the database schema...\\nAs I mentioned earlier, scalability is a key factor.",
        "speaking_count": 20,
        "roleplays": ["Opening a Presentation", "Transitioning between topics", "Handling Q&A", "Concluding a Demo", "Explaining a complex chart"],
        "pronunciation": ["Demonstrate", "Showcase", "Illustrate", "Highlight", "Emphasize", "Clarify", "Summarize", "Conclude", "Transition", "Engage", "Captivate", "Articulate", "Convey", "Present", "Structure", "Framework", "Overview", "Walkthrough", "Handoff", "Feedback"],
        "reading_title": "The Art of the Technical Demo",
        "reading_content": "A successful technical demo requires more than just showing working code. It involves storytelling, focusing on the user value, and clearly articulating the technical challenges overcome to achieve the result.",
        "listening_title": "TED Talk by Nancy Duarte 'The Secret Structure of Great Talks'",
        "writing_task": "Write an outline for a 5-minute technical presentation.",
        "writing_model": "1. Introduction (Hook & Problem Statement)\\n2. Proposed Solution Overview\\n3. Technical Deep Dive (Key Feature)\\n4. Results & Impact\\n5. Q&A",
        "hr_q": "How do you prepare and deliver technical presentations to stakeholders?",
        "hr_bad": "I just open my code and explain it.",
        "hr_good": "I make some slides and explain the project.",
        "hr_excellent": "I tailor my presentation to the audience. For non-technical stakeholders, I focus on business impact and high-level architecture, using analogies. I anticipate questions and prepare a clear agenda.",
        "tech_comm": "How to present a live coding demo or system architecture to a mixed technical/non-technical audience",
        "gd_topic": "Open Source Software vs Proprietary Software: Which Should Enterprises Choose?",
        "story_prompt": "Describe a time when a live demo failed and how you recovered.",
        "mistakes_count": 10,
        "mistakes_context": "Presentation language error"
    }},
    {{
        "day_num": 11,
        "day_num_padded": "11",
        "topic": "STAR Method for Behavioral Interview Questions",
        "tier": "Intermediate",
        "grammar_topic": "Action Verbs & Metric Expressions",
        "prev_link": "day10.html",
        "next_link": "day12.html",
        "vocab": ["Situation", "Task", "Action", "Result", "Led", "Coordinated", "Achieved", "Improved", "Reduced", "Increased", "Developed", "Implemented", "Managed", "Delivered", "Exceeded", "Streamlined", "Optimized", "Resolved", "Built", "Designed", "Launched", "Established", "Aligned", "Transformed", "Measured"],
        "phrasal": ["Take on", "Come up with", "Work towards", "Pull through", "Step in", "Turn around", "Build upon", "Follow through", "Carry out", "Stand out"],
        "idioms": ["Walk the talk", "Put your money where your mouth is", "Actions speak louder than words", "Rise to the occasion", "Hit the ground running", "Lead by example", "Bite the bullet", "Go above and beyond", "Make a difference", "Leave a lasting impression"],
        "grammar_desc": "Powerful action verbs with metrics, quantified impact statements, past perfect for context, present perfect for ongoing impact",
        "grammar_examples": "I reduced API latency by 40%.\\nWe had already established the baseline before the migration.\\nThe system has processed 1 million requests since launch.",
        "speaking_count": 20,
        "roleplays": ["Answering a Leadership Question", "Explaining a failure", "Describing conflict resolution", "Detailing a technical achievement", "Discussing a tight deadline"],
        "pronunciation": ["Situation", "Task", "Action", "Result", "Led", "Coordinated", "Achieved", "Improved", "Reduced", "Increased", "Developed", "Implemented", "Managed", "Delivered", "Exceeded", "Streamlined", "Optimized", "Resolved", "Built", "Designed"],
        "reading_title": "How to Use the STAR Method to Ace Any Behavioral Interview",
        "reading_content": "The STAR method (Situation, Task, Action, Result) provides a structured way to answer behavioral interview questions. It ensures you provide enough context, focus on your specific contributions, and conclude with quantifiable outcomes.",
        "listening_title": "Mastering the Behavioral Interview",
        "writing_task": "Write out a STAR story for a time you solved a complex problem.",
        "writing_model": "Situation: Our database queries were timing out.\\nTask: I needed to optimize the queries to handle high load.\\nAction: I implemented indexing and rewrote the join logic.\\nResult: Query times decreased by 80%.",
        "hr_q": "Tell me about a time you showed leadership.",
        "hr_bad": "I led a team last year.",
        "hr_good": "I was the team lead for a project and made sure everyone did their work on time.",
        "hr_excellent": "In my previous role, our tech lead left abruptly mid-project (Situation). I volunteered to take over coordinating the sprints (Task). I facilitated daily standups, unblocked junior developers, and communicated progress to stakeholders (Action). As a result, we delivered the project on time and I was formally promoted (Result).",
        "tech_comm": "STAR-formatted answer for 'Describe a technical challenge you solved under a deadline'",
        "gd_topic": "Should Companies Prioritize Experience or Potential When Hiring Fresh Graduates?",
        "story_prompt": "Describe your most significant professional achievement.",
        "mistakes_count": 10,
        "mistakes_context": "Storytelling error"
    }}
]

for d in days:
    html = TEMPLATE.format(
        day_num=d["day_num"],
        day_num_padded=d["day_num_padded"],
        topic=d["topic"],
        tier=d["tier"],
        grammar_topic=d["grammar_topic"],
        prev_link=d["prev_link"],
        next_link=d["next_link"],
        vocab_count=len(d["vocab"]),
        speaking_count=d["speaking_count"],
        roleplay_count=len(d["roleplays"]),
        pronunciation_count=len(d["pronunciation"]),
        mistakes_count=d["mistakes_count"],
        vocab_html=build_vocab_html(d["vocab"]),
        phrasal_html=build_phrasal_html(d["phrasal"]),
        idioms_html=build_idioms_html(d["idioms"]),
        grammar_desc=d["grammar_desc"],
        grammar_examples=d["grammar_examples"],
        speaking_html=build_speaking_html(d["speaking_count"]),
        roleplay_html=build_roleplay_html(d["roleplays"]),
        pronunciation_html=build_pronunciation_html(d["pronunciation"]),
        reading_title=d["reading_title"],
        reading_content=d["reading_content"],
        listening_title=d["listening_title"],
        writing_task=d["writing_task"],
        writing_model=d["writing_model"],
        hr_q=d["hr_q"],
        hr_bad=d["hr_bad"],
        hr_good=d["hr_good"],
        hr_excellent=d["hr_excellent"],
        tech_comm=d["tech_comm"],
        gd_topic=d["gd_topic"],
        story_prompt=d["story_prompt"],
        rapid_fire_html=build_rapid_fire_html(20),
        mistakes_html=build_mistakes_html(d["mistakes_count"], d["mistakes_context"])
    )
    
    with open(f"C:/Users/ASUS/.gemini/antigravity/scratch/English-Communication-Master/lessons/day{d['day_num_padded']}.html", "w", encoding="utf-8") as f:
        f.write(html)
        
print("Successfully generated all files.")
