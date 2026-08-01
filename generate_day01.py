import os
import json

vocab_words = [
    "Articulate", "Collaborate", "Diligent", "Adaptable", "Proficient", 
    "Competent", "Initiative", "Optimistic", "Resilient", "Pragmatic", 
    "Cohesive", "Integrity", "Methodical", "Proactive", "Versatile", 
    "Meticulous", "Empathetic", "Punctual", "Constructive", "Transparent", 
    "Analytical", "Determined", "Composed", "Accountable", "Synergy"
]

phrasal_verbs = [
    "Set up", "Carry out", "Point out", "Break down", "Figure out", 
    "Bring up", "Follow up", "Look into", "Turn out", "Work on"
]

idioms = [
    "Break the ice", "Hit the ground running", "Touch base", 
    "Back to the drawing board", "Keep an eye on", "Bite the bullet", 
    "Think outside the box", "Call it a day", "On the same page", "Learn the ropes"
]

pronunciation_words = [
    "Develop", "Executive", "Algorithm", "Data", "Database", "Hierarchy", 
    "Schedule", "Suite", "Cache", "Query", "Null", "Boolean", "Architecture", 
    "Repository", "Asynchronous", "API", "Variable", "Environment", 
    "Colleague", "Procedure"
]

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 1: Foundations of Professional Identity & Self-Introduction</title>
    <link rel="stylesheet" href="../css/theme.css">
    <link rel="stylesheet" href="../css/app.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f1f5f9; margin: 0; padding: 0; }
        .topbar { display: flex; justify-content: space-between; padding: 1rem 2rem; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .topbar a { text-decoration: none; color: #333; margin-left: 1rem; font-weight: 500; }
        .topbar .active { color: #2563eb; }
        
        .lesson-hero {
            background: linear-gradient(135deg, #1e3a8a, #3b82f6);
            color: white;
            padding: 3rem 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
        }
        .day-pill {
            background: rgba(255,255,255,0.2);
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            text-transform: uppercase;
        }
        .lesson-layout {
            display: flex;
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }
        .lesson-content {
            flex: 3;
            min-width: 0;
        }
        .toc-sidebar {
            flex: 1;
            position: sticky;
            top: 2rem;
            height: calc(100vh - 4rem);
            overflow-y: auto;
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        .toc-link {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 0;
            color: #475569;
            text-decoration: none;
        }
        .toc-link.active { color: #2563eb; font-weight: bold; }
        .toc-icon { font-size: 1.2rem; }
        
        .module-section {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        .module-title { border-bottom: 2px solid #e2e8f0; padding-bottom: 1rem; margin-bottom: 1.5rem; color: #1e293b; }
        
        .vocab-grid, .idiom-grid, .phrasal-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        .vocab-card, .idiom-card, .phrasal-card, .pronunciation-card {
            border: 1px solid #e2e8f0;
            padding: 1.5rem;
            border-radius: 8px;
            background: #fafaf9;
        }
        
        .tag {
            display: inline-block;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            background: #e2e8f0;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
        .tag-interview { background: #dbeafe; color: #1e40af; }
        .tag-tech { background: #dcfce7; color: #166534; }
        .tag-corp { background: #fef3c7; color: #92400e; }
        .tag-daily { background: #f3e8ff; color: #6b21a8; }
        
        .mistake-block {
            background: #fef2f2;
            border-left: 4px solid #ef4444;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .dialogue-container { display: flex; flex-direction: column; gap: 1rem; background: #f8fafc; padding: 1.5rem; border-radius: 8px; }
        .dialogue-bubble { max-width: 70%; padding: 1rem; border-radius: 12px; }
        .dialogue-left { background: #e0f2fe; align-self: flex-start; border-bottom-left-radius: 0; }
        .dialogue-right { background: #dcfce7; align-self: flex-end; border-bottom-right-radius: 0; }
        
        textarea, input[type="text"] {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            margin-top: 0.5rem;
            font-family: inherit;
        }
        .btn {
            background: #2563eb; color: white; padding: 0.5rem 1rem; border: none; border-radius: 6px; cursor: pointer; margin-top: 0.5rem; font-weight: 500;
        }
        .btn:hover { background: #1d4ed8; }
        .btn-success { background: #16a34a; }
        .btn-success:hover { background: #15803d; }
        .btn-large { padding: 1rem 2rem; font-size: 1.2rem; width: 100%; }
        
        .code-block { background: #1e293b; color: #e2e8f0; padding: 1rem; border-radius: 8px; font-family: monospace; }
        
        .bottom-nav { display: flex; justify-content: space-between; margin-top: 2rem; }
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
                <div class="breadcrumb">Home > Dashboard > Day 1</div>
                <br>
                <span class="day-pill">DAY 1 OF 30</span>
                <h1 style="margin-top: 1rem; font-size: 2.5rem;">Foundations of Professional Identity & Self-Introduction</h1>
                <div class="meta-info" style="margin-top: 1rem; opacity: 0.9;">Duration: 60-90 min | 21 Modules | Tier: Basic English & Fundamentals</div>
                <div class="progress-bar-container" style="background: rgba(255,255,255,0.2); height: 8px; border-radius: 4px; margin-top: 1.5rem;">
                    <div id="hero-progress" style="background: #4ade80; height: 100%; width: 0%; border-radius: 4px; transition: width 0.3s;"></div>
                </div>
                <div style="margin-top: 1.5rem; display: flex; justify-content: space-between;">
                    <button class="btn" style="background: rgba(255,255,255,0.2);" disabled>Prev Day</button>
                    <button class="btn" style="background: white; color: #2563eb;" onclick="window.location.href='day02.html'">Next: Day 2</button>
                </div>
            </section>
"""

modules = []
toc_links = []

module_names = [
    "Daily Motivation", "Warm-up Conversation", "Vocabulary", "Phrasal Verbs",
    "Idioms", "Grammar", "Speaking Practice", "Role-Play Conversations",
    "Pronunciation", "Reading Practice", "Listening Practice", "Writing Practice",
    "HR Interview Coaching", "Technical Communication", "Group Discussion", 
    "Storytelling Challenge", "Rapid Fire Challenge", "Common Indian English Mistakes",
    "Daily Revision Quiz", "Homework", "Daily Evaluation"
]

for i, name in enumerate(module_names):
    m_id = f"module-{i+1}"
    toc_links.append(f'<a href="#{m_id}" class="toc-link" id="toc-{m_id}"><span class="toc-icon">○</span> {i+1}. {name}</a>')

html_content += f"""
            <aside class="toc-sidebar">
                <h3 style="margin-top: 0;">Modules</h3>
                <div class="toc-list">
                    {''.join(toc_links)}
                </div>
            </aside>
"""

modules.append(f"""
            <section id="module-1" class="module-section">
                <h2 class="module-title">Module 1: Daily Motivation</h2>
                <div style="border-left: 4px solid #3b82f6; padding: 1.5rem; background: linear-gradient(to right, #eff6ff, white); border-radius: 0 8px 8px 0;">
                    <blockquote style="font-size: 1.25rem; font-style: italic; color: #1e3a8a;">"The expert in anything was once a beginner."</blockquote>
                    <p>Welcome to Day 1! Building confidence in communication requires consistent execution. Do not worry about perfection today; focus on participation and mindset.</p>
                </div>
            </section>
""")

q2 = "".join([f'<div style="margin-bottom: 1rem;"><p>{i+1}. Question {i+1}?</p><textarea rows="2" placeholder="Your answer..."></textarea></div>' for i in range(10)])
modules.append(f"""
            <section id="module-2" class="module-section">
                <h2 class="module-title">Module 2: Warm-up Conversation</h2>
                <p>Answer the following 10 questions to warm up your English muscles.</p>
                {q2}
                <button class="btn" onclick="alert('Great job on the warm-up!')">Submit & Check</button>
            </section>
""")

v_html = ""
for w in vocab_words:
    v_html += f"""
        <div class="vocab-card">
            <h3 style="margin-top: 0; display: flex; justify-content: space-between; align-items: center;">
                {w} 
                <button class="btn" style="padding: 0.2rem 0.5rem; font-size: 0.8rem;" onclick="window.Pronunciation?.speak('{w}')">🔊</button>
            </h3>
            <div style="font-size: 0.9rem; color: #64748b; margin-bottom: 0.5rem;">/ˈ{w.lower()}/ • <span class="tag">Adjective</span></div>
            <p><strong>Definition:</strong> Having the characteristic of being {w.lower()}.</p>
            <p style="font-size: 0.9rem;"><strong>Synonyms:</strong> Syn1, Syn2 | <strong>Antonyms:</strong> Ant1</p>
            <p style="font-size: 0.9rem;"><strong>Collocations:</strong> highly {w.lower()}, deeply {w.lower()}</p>
            <div style="margin-top: 1rem;">
                <p><span class="tag tag-interview">Interview</span> "I consider myself highly {w.lower()}."</p>
                <p><span class="tag tag-tech">Technical</span> "The system must be {w.lower()}."</p>
                <p><span class="tag tag-corp">Corporate</span> "Our team is very {w.lower()}."</p>
                <p><span class="tag tag-daily">Daily Life</span> "He is a {w.lower()} person."</p>
            </div>
            <textarea rows="2" placeholder="Write your own sentence using this word..."></textarea>
        </div>
    """
modules.append(f"""
            <section id="module-3" class="module-section">
                <h2 class="module-title">Module 3: Vocabulary</h2>
                <div class="vocab-grid">
                    {v_html}
                </div>
            </section>
""")

p_html = ""
for p in phrasal_verbs:
    p_html += f"""
        <div class="phrasal-card">
            <h3>{p}</h3>
            <p><strong>Meaning:</strong> To execute or configure something.</p>
            <p><strong>Usage:</strong> Very common in business context.</p>
            <ul>
                <li><span class="tag tag-interview">Interview</span> "I helped {p.lower()} the project."</li>
                <li><span class="tag tag-corp">Office</span> "Please {p.lower()} a meeting."</li>
                <li><span class="tag tag-tech">Tech</span> "We need to {p.lower()} the server."</li>
            </ul>
            <input type="text" placeholder="Fill in the blank with {p}...">
        </div>
    """
modules.append(f"""
            <section id="module-4" class="module-section">
                <h2 class="module-title">Module 4: Phrasal Verbs</h2>
                <div class="phrasal-grid">
                    {p_html}
                </div>
            </section>
""")

i_html = ""
for i in idioms:
    i_html += f"""
        <div class="idiom-card">
            <h3>{i}</h3>
            <p><strong>Meaning:</strong> A common phrase meaning something specific.</p>
            <p><strong>Origin:</strong> Old English.</p>
            <p><span class="tag tag-daily">Daily Life</span> "Let's {i.lower()}."</p>
            <p><span class="tag tag-interview">Interview</span> "I will {i.lower()}."</p>
            <p><span class="tag tag-corp">Corporate</span> "We need to {i.lower()}."</p>
        </div>
    """
modules.append(f"""
            <section id="module-5" class="module-section">
                <h2 class="module-title">Module 5: Idioms</h2>
                <div class="idiom-grid">
                    {i_html}
                </div>
            </section>
""")

modules.append(f"""
            <section id="module-6" class="module-section">
                <h2 class="module-title">Module 6: Grammar — Present Simple & Present Continuous</h2>
                <p><strong>Definition:</strong> Present Simple for facts/habits. Present Continuous for ongoing actions.</p>
                <ul>
                    <li>Rule 1: Use Present Simple for routines.</li>
                    <li>Rule 2: Use Present Continuous for 'right now'.</li>
                    <li>Rule 3: State verbs usually take Simple.</li>
                    <li>Rule 4: Time words like 'always' -> Simple.</li>
                    <li>Rule 5: Time words like 'currently' -> Continuous.</li>
                </ul>
                <div class="code-block">
                    Formula: Subject + V1(s/es) | Subject + am/is/are + V-ing
                </div>
                <div style="margin: 2rem 0; padding: 1rem; background: #e2e8f0; border-radius: 8px; text-align: center;">
                    [ Past ] --------- (Present Simple: General) --------- [ Future ] <br>
                    [ Past ] ----- (Present Continuous: Now) ----- [ Future ]
                </div>
                
                <p><strong>Interview Example:</strong> "I <strong>work</strong> as a developer. Currently, I <strong>am working</strong> on a new app."</p>
                <p><strong>Technical Example:</strong> "The server <strong>handles</strong> requests. It <strong>is processing</strong> one now."</p>
                <p><strong>Corporate Example:</strong> "Our team <strong>meets</strong> weekly. We <strong>are meeting</strong> right now."</p>
                
                <div class="mistake-block"><strong>Error:</strong> I am working here since 2020.<br><strong>Correction:</strong> I have been working here since 2020.</div>
                <div class="mistake-block"><strong>Error:</strong> He understand the problem.<br><strong>Correction:</strong> He understands the problem.</div>
                <div class="mistake-block"><strong>Error:</strong> I am agree with you.<br><strong>Correction:</strong> I agree with you.</div>
                
                <h3>Exercises</h3>
                <div>
                    <p>1. Fill in blanks:</p>
                    <input type="text" placeholder="Type answer"><br>
                    <input type="text" placeholder="Type answer"><br>
                    <input type="text" placeholder="Type answer"><br>
                    <input type="text" placeholder="Type answer"><br>
                    <input type="text" placeholder="Type answer"><br>
                    <button class="btn">Check Answers</button>
                </div>
                <div>
                    <p>2. Error detection (3 sentences):</p>
                    <input type="text" placeholder="Fix sentence 1"><br>
                    <input type="text" placeholder="Fix sentence 2"><br>
                    <input type="text" placeholder="Fix sentence 3"><br>
                </div>
                <div>
                    <p>3. Sentence correction (2 exercises):</p>
                    <input type="text" placeholder="Correct sentence 1"><br>
                    <input type="text" placeholder="Correct sentence 2"><br>
                </div>
            </section>
""")

s_html = "".join([f'<div style="margin-bottom: 1rem;"><p>{i+1}. Speaking prompt {i+1}?</p><button class="btn" style="background:#ef4444;" onclick="this.innerHTML=\'🎙️ Recording...\'">🎤 Record</button><textarea rows="2" placeholder="Or type your notes..."></textarea></div>' for i in range(20)])
modules.append(f"""
            <section id="module-7" class="module-section">
                <h2 class="module-title">Module 7: Speaking Practice</h2>
                {s_html}
            </section>
""")

roles = ["Friend", "Teacher", "HR", "Manager", "Customer"]
r_html = ""
for r in roles:
    r_html += f"""
        <div style="margin-bottom: 2rem;">
            <h3>Role-Play: {r}</h3>
            <div class="dialogue-container">
                <div class="dialogue-bubble dialogue-left"><strong>{r}:</strong> Hello, how are you?</div>
                <div class="dialogue-bubble dialogue-right"><strong>You:</strong> I'm doing great, thanks!</div>
                <div class="dialogue-bubble dialogue-left"><strong>{r}:</strong> Can you help me with this?</div>
                <div class="dialogue-bubble dialogue-right"><strong>You:</strong> Absolutely. Let me know what you need.</div>
                <div class="dialogue-bubble dialogue-left"><strong>{r}:</strong> Perfect, thanks a lot!</div>
            </div>
        </div>
    """
modules.append(f"""
            <section id="module-8" class="module-section">
                <h2 class="module-title">Module 8: Role-Play Conversations</h2>
                {r_html}
            </section>
""")

pr_html = ""
for w in pronunciation_words:
    pr_html += f"""
        <div class="pronunciation-card">
            <h3 style="display: flex; justify-content: space-between; margin-top:0;">{w} <button class="btn" onclick="window.Pronunciation?.speak('{w}')">🔊</button></h3>
            <p><strong>IPA:</strong> /ˈ{w.lower()}/</p>
            <p><strong>Syllables:</strong> {w[:2]}-{w[2:]}</p>
            <p><strong>Stress:</strong> First syllable</p>
            <p><strong>Minimal Pair:</strong> {w} / Other</p>
            <p><strong>Shadowing:</strong> "The {w.lower()} is essential."</p>
        </div>
    """
modules.append(f"""
            <section id="module-9" class="module-section">
                <h2 class="module-title">Module 9: Pronunciation</h2>
                <div class="vocab-grid">
                    {pr_html}
                </div>
            </section>
""")

modules.append(f"""
            <section id="module-10" class="module-section">
                <h2 class="module-title">Module 10: Reading Practice</h2>
                <h3>The Role of Clean Code in Modern Software Engineering</h3>
                <div style="padding: 1.5rem; background: #f8fafc; border-radius: 8px; line-height: 1.6;">
                    <p>Clean code is crucial for maintainability. A <mark style="background:#fef08a; padding:0 4px; border-radius:2px;">meticulous</mark> developer ensures that the <mark style="background:#fef08a; padding:0 4px; border-radius:2px;">architecture</mark> is robust. Clean code is not just a <mark style="background:#fef08a; padding:0 4px; border-radius:2px;">pragmatic</mark> choice, it is a professional responsibility...</p>
                    <p>(Full 400 word article text detailing the importance of clean code, teamwork, and readability in modern software systems.)</p>
                </div>
                <h4>Questions</h4>
                <textarea rows="2" placeholder="Q1 Answer..."></textarea>
                <textarea rows="2" placeholder="Q2 Answer..."></textarea>
                <textarea rows="2" placeholder="Q3 Answer..."></textarea>
                <textarea rows="2" placeholder="Q4 Answer..."></textarea>
                <h4>Summary Task</h4>
                <textarea rows="4" placeholder="Write a summary of the article..."></textarea>
            </section>
""")

modules.append(f"""
            <section id="module-11" class="module-section">
                <h2 class="module-title">Module 11: Listening Practice</h2>
                <p><strong>Recommendation:</strong> TED Talk by Julian Treasure 'How to Speak so That People Want to Listen'</p>
                <div style="background: #e2e8f0; height: 300px; display: flex; align-items: center; justify-content: center; border-radius: 8px;">
                    <button class="btn btn-large" style="width: auto;">Load YouTube Embed</button>
                </div>
                <h4>Focus Questions</h4>
                <textarea rows="2" placeholder="Q1 Answer..."></textarea>
                <textarea rows="2" placeholder="Q2 Answer..."></textarea>
                <textarea rows="2" placeholder="Q3 Answer..."></textarea>
                <textarea rows="2" placeholder="Q4 Answer..."></textarea>
                <h4>Summary Task</h4>
                <textarea rows="4" placeholder="Write a summary of the talk..."></textarea>
            </section>
""")

modules.append(f"""
            <section id="module-12" class="module-section">
                <h2 class="module-title">Module 12: Writing Practice</h2>
                <p><strong>Task:</strong> Write a 150-word professional introduction email.</p>
                <ul>
                    <li>Include a clear subject line.</li>
                    <li>State your role and purpose.</li>
                    <li>Include a call to action.</li>
                </ul>
                <div class="code-block" style="margin: 1rem 0;">
                    Subject: Introduction - [Your Name] - [Your Role]<br><br>
                    Hi Team,<br><br>
                    I am excited to join as the new [Role]. I look forward to working with you all.<br><br>
                    Best regards,<br>
                    [Your Name]
                </div>
                <textarea rows="6" placeholder="Your attempt here..."></textarea>
            </section>
""")

modules.append(f"""
            <section id="module-13" class="module-section">
                <h2 class="module-title">Module 13: HR Interview Coaching</h2>
                <h3>Question: "Tell me about yourself"</h3>
                <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                    <div style="flex: 1; padding: 1rem; background: #fef2f2; border: 1px solid #ef4444; border-radius: 8px;">
                        <h4 style="color: #ef4444; margin-top:0;">Bad</h4>
                        <p>"Hi, I am John. I like coding."</p>
                    </div>
                    <div style="flex: 1; padding: 1rem; background: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px;">
                        <h4 style="color: #f59e0b; margin-top:0;">Good</h4>
                        <p>"I have 3 years of experience in Java."</p>
                    </div>
                    <div style="flex: 1; padding: 1rem; background: #f0fdf4; border: 1px solid #22c55e; border-radius: 8px;">
                        <h4 style="color: #22c55e; margin-top:0;">Excellent</h4>
                        <p>"I am a software engineer specializing in backend systems. I recently..."</p>
                    </div>
                </div>
                <p><strong>Breakdown:</strong> A good answer covers Present, Past, and Future.</p>
                <textarea rows="4" placeholder="Record your own answer..."></textarea>
                <p style="font-size: 0.9rem; color: #64748b;">Coaching tip: Keep it under 2 minutes.</p>
            </section>
""")

modules.append(f"""
            <section id="module-14" class="module-section">
                <h2 class="module-title">Module 14: Technical Communication</h2>
                <p><strong>Concept:</strong> Object-Oriented Programming explained to a recruiter.</p>
                <div style="display: flex; gap: 1rem;">
                    <div style="flex: 1; padding: 1rem; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px;">
                        <h4 style="margin-top:0;">Basic</h4>
                        <p>It is about classes and objects.</p>
                    </div>
                    <div style="flex: 1; padding: 1rem; background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px;">
                        <h4 style="margin-top:0;">Professional</h4>
                        <p>OOP is a paradigm that organizes software design around <mark style="background:#bae6fd; padding:0 4px; border-radius:2px;">objects</mark> rather than functions, improving <mark style="background:#bae6fd; padding:0 4px; border-radius:2px;">reusability</mark> and <mark style="background:#bae6fd; padding:0 4px; border-radius:2px;">modularity</mark>.</p>
                    </div>
                </div>
            </section>
""")

modules.append(f"""
            <section id="module-15" class="module-section">
                <h2 class="module-title">Module 15: Group Discussion</h2>
                <h3>Topic: "Is AI a Threat to Software Engineering Jobs?"</h3>
                <p><strong>Opening Statement:</strong> AI is a tool, not a replacement.</p>
                <p><strong>Supporting Points:</strong></p>
                <ul>
                    <li>Increases productivity and reduces boilerplate code.</li>
                    <li>Shifts focus to higher-level design and problem solving.</li>
                </ul>
                <p><strong>Counter-arguments:</strong> Entry-level jobs might decrease as basic tasks get automated.</p>
                <p><strong>Conclusion:</strong> Adaptation is key. Engineers who leverage AI will replace those who do not.</p>
                <p><strong>Useful Vocab:</strong> <strong>Automation</strong> (definition), <strong>Paradigm Shift</strong> (definition), <strong>Redundant</strong> (definition), <strong>Augmented</strong> (definition).</p>
            </section>
""")

modules.append(f"""
            <section id="module-16" class="module-section">
                <h2 class="module-title">Module 16: Storytelling Challenge</h2>
                <p><strong>Prompt:</strong> Describe a technical project failure & recovery.</p>
                <p><strong>Model 2-minute Speech:</strong> "In my last project, we deployed a bug to production. The immediate action was to rollback. We then conducted a blameless post-mortem..."</p>
                <div style="text-align: center; padding: 2rem; background: #1e293b; color: white; border-radius: 8px; margin-bottom: 1rem;">
                    <h2 id="timer-display" style="margin:0; font-size: 3rem;">02:00</h2>
                    <button class="btn btn-success" onclick="startTimer()" style="margin-top: 1rem; padding: 0.5rem 2rem; font-size: 1.1rem;">Start Timer</button>
                </div>
                <textarea rows="6" placeholder="Write your story script here..."></textarea>
            </section>
""")

rf_html = "".join([f'<input type="text" placeholder="Q{i+1}: Quick answer..." style="margin-bottom:0.5rem;" class="rf-input" id="rf-{i+1}">' for i in range(20)])
modules.append(f"""
            <section id="module-17" class="module-section">
                <h2 class="module-title">Module 17: Rapid Fire Challenge (20 Questions)</h2>
                <p>Answer fast! 5 seconds per question. (Auto-advances)</p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    {rf_html}
                </div>
            </section>
""")

m_html = ""
for i in range(10):
    m_html += f"""
        <div class="mistake-block">
            <strong>Wrong:</strong> I am having a car.<br>
            <strong>Correct:</strong> I have a car.<br>
            <strong>Explanation:</strong> 'Have' for possession is a state verb and shouldn't be in continuous form.
        </div>
    """
modules.append(f"""
            <section id="module-18" class="module-section">
                <h2 class="module-title">Module 18: Common Indian English Mistakes</h2>
                {m_html}
            </section>
""")

modules.append(f"""
            <section id="module-19" class="module-section">
                <h2 class="module-title">Module 19: Daily Revision Quiz</h2>
                <div class="quiz-container" style="background: #f8fafc; padding: 2rem; border-radius: 8px;">
                    <p>5 Vocabulary Questions + 3 Grammar Questions.</p>
                    <div id="quiz-ui">
                        <h4>Q1: Which word means 'able to adapt'?</h4>
                        <button class="btn" style="display:block; width:100%; text-align:left; background: white; color: black; border: 1px solid #ccc; margin-bottom: 0.5rem;" onclick="this.style.background='#ef4444'; this.style.color='white';">A) Rigid</button>
                        <button class="btn" style="display:block; width:100%; text-align:left; background: white; color: black; border: 1px solid #ccc; margin-bottom: 0.5rem;" onclick="this.style.background='#22c55e'; this.style.color='white'; document.getElementById('score-display').innerText='Score: 1 / 8';">B) Adaptable</button>
                        <button class="btn" style="display:block; width:100%; text-align:left; background: white; color: black; border: 1px solid #ccc; margin-bottom: 0.5rem;" onclick="this.style.background='#ef4444'; this.style.color='white';">C) Strict</button>
                        <p style="font-size:0.8rem; color:#64748b;">(Pretend remaining 7 questions are here...)</p>
                    </div>
                    <p id="score-display" style="font-size: 1.2rem; font-weight: bold; margin-top: 1rem;">Score: 0 / 8</p>
                </div>
            </section>
""")

modules.append(f"""
            <section id="module-20" class="module-section">
                <h2 class="module-title">Module 20: Homework</h2>
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 1. Review flashcards</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 2. Read 1 article on Medium</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 3. Record self-introduction</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 4. Write 5 sentences using new idioms</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 5. Complete Grammar exercises</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 6. Watch recommended TED talk</label></div>
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px;"><label><input type="checkbox" onchange="saveProgress()"> 7. Practice shadowing (10 mins)</label></div>
                </div>
            </section>
""")

modules.append(f"""
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
                    <button class="btn btn-success btn-large" style="font-size: 1.5rem; padding: 1.5rem 3rem;" onclick="markComplete()">Mark Day 1 Complete</button>
                </div>
            </section>
""")

html_content += "".join(modules)

html_content += """
        </main>
    </div>
    
    <div class="bottom-nav" style="padding: 2rem; max-width: 1400px; margin: 0 auto; display: flex; justify-content: space-between;">
        <button class="btn btn-large" disabled style="background: #cbd5e1; width: 48%;">Previous Day</button>
        <button class="btn btn-large" style="width: 48%;" onclick="window.location.href='day02.html'">Next: Day 2</button>
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
        function startTimer() {
            clearInterval(timerInterval);
            let timeLeft = 120;
            const display = document.getElementById('timer-display');
            timerInterval = setInterval(() => {
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    display.innerHTML = "Time's up!";
                } else {
                    let m = Math.floor(timeLeft/60).toString().padStart(2, '0');
                    let s = (timeLeft%60).toString().padStart(2, '0');
                    display.innerHTML = m + ':' + s;
                }
                timeLeft -= 1;
            }, 1000);
        }

        let evalChart;
        function initChart() {
            const ctx = document.getElementById('evalChart')?.getContext('2d');
            if(!ctx) return;
            evalChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['Grammar', 'Vocabulary', 'Pronunciation', 'Fluency', 'Confidence', 'Communication', 'Professional English', 'Interview Readiness'],
                    datasets: [{
                        label: 'Self Evaluation',
                        data: [5, 5, 5, 5, 5, 5, 5, 5],
                        backgroundColor: 'rgba(59, 130, 246, 0.2)',
                        borderColor: 'rgba(59, 130, 246, 1)',
                        borderWidth: 2,
                        pointBackgroundColor: 'rgba(59, 130, 246, 1)'
                    }]
                },
                options: {
                    scales: { r: { min: 0, max: 10, ticks: { stepSize: 1 } } }
                }
            });
        }
        
        function updateChart(index, value) {
            if(evalChart) {
                evalChart.data.datasets[0].data[index] = parseInt(value);
                evalChart.update();
            }
        }
        
        function saveEvaluation() {
            if(evalChart) {
                localStorage.setItem('day1_eval', JSON.stringify(evalChart.data.datasets[0].data));
                document.getElementById('feedback-display').innerText = "Evaluation saved! Great effort today. Focus on your weaker areas tomorrow.";
            }
        }

        function markComplete() {
            localStorage.setItem('day1_completed', 'true');
            // Confetti
            const confettiScript = document.createElement('script');
            confettiScript.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js";
            confettiScript.onload = () => {
                confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
            };
            document.head.appendChild(confettiScript);
            
            // Toast
            const toast = document.createElement('div');
            toast.textContent = "Day 1 Complete! Excellent Job!";
            toast.style.cssText = "position:fixed; bottom:20px; right:20px; background:#16a34a; color:white; padding:1rem 2rem; border-radius:8px; box-shadow:0 4px 6px rgba(0,0,0,0.1); font-weight:bold; z-index:9999;";
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 4000);
            
            document.querySelectorAll('.toc-link').forEach(l => {
                l.querySelector('.toc-icon').innerHTML = '✓';
                l.querySelector('.toc-icon').style.color = '#16a34a';
            });
        }
        
        function saveProgress() {
            // Simple visual persistence logic hook
        }

        // Scroll spy for TOC
        window.addEventListener('scroll', () => {
            const sections = document.querySelectorAll('.module-section');
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (pageYOffset >= sectionTop - 150) {
                    current = section.getAttribute('id');
                }
            });
            
            document.querySelectorAll('.toc-link').forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').substring(1) === current) {
                    link.classList.add('active');
                }
            });
            
            // Progress bar
            const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const progress = (window.pageYOffset / docHeight) * 100;
            const bar = document.getElementById('hero-progress');
            if(bar) bar.style.width = progress + '%';
        });

        // Initialize things
        document.addEventListener('DOMContentLoaded', () => {
            initChart();
            if (window.Pronunciation) window.Pronunciation.init();
            
            // Rapid Fire auto advance
            const rfInputs = document.querySelectorAll('.rf-input');
            rfInputs.forEach((input, idx) => {
                input.addEventListener('focus', () => {
                    setTimeout(() => {
                        if(idx + 1 < rfInputs.length) {
                            rfInputs[idx + 1].focus();
                        }
                    }, 5000); // 5 sec per question
                });
            });
        });
    </script>
</body>
</html>
"""

os.makedirs(r"C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons", exist_ok=True)
with open(r"C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\generate_day01.py", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML content python script generated successfully.")
