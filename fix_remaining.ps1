# fix_remaining_days.ps1
# Fixes days 03, 05, 06, 07 which have different broken patterns

$dir = "C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons"

# ── Helper: move aside out of main ──────────────────────────────────────────
function Move-AsideOutOfMain {
    param($filePath, $asideClass)
    
    $content = [System.IO.File]::ReadAllText($filePath)
    
    # Match the aside block (greedy but anchored to closing tag)
    $pattern = "(?s)(\s*<aside[^>]*>.*?</aside>)"
    $match = [regex]::Match($content, $pattern)
    
    if (-not $match.Success) {
        Write-Host "  WARN: no aside found in $([System.IO.Path]::GetFileName($filePath))"
        return
    }
    
    $asideBlock = $match.Value
    
    # Remove aside from its current position (inside main)
    $cleaned = $content -replace [regex]::Escape($asideBlock), "`n"
    
    # Insert after the first </main>
    $fixed = $cleaned -replace '(</main>)', "`$1`n$asideBlock"
    
    [System.IO.File]::WriteAllText($filePath, $fixed, [System.Text.Encoding]::UTF8)
    Write-Host "  FIXED: $([System.IO.Path]::GetFileName($filePath))"
}

# ── Day 03 ── aside.sidebar-toc inside main.lesson-main ─────────────────────
Move-AsideOutOfMain -filePath "$dir\day03.html" -asideClass "sidebar-toc"

# ── Day 05 ── aside.sidebar-toc inside main.lesson-main ─────────────────────
Move-AsideOutOfMain -filePath "$dir\day05.html" -asideClass "sidebar-toc"

# ── Day 06 ── aside.sidebar inside main.layout ───────────────────────────────
Move-AsideOutOfMain -filePath "$dir\day06.html" -asideClass "sidebar"

# ── Day 07 ── No main or aside at all — inject a full working TOC ────────────
$day07Path = "$dir\day07.html"
$d7 = [System.IO.File]::ReadAllText($day07Path)

# day07 likely uses a flat layout — wrap content in flex layout + inject TOC
# Find the body content start (after nav/header)
# Strategy: find a recognisable module section and wrap everything

# Check what it looks like
$d7Lines = $d7 -split "`n"
Write-Host ""
Write-Host "--- day07.html structure preview ---"
$i = 1
foreach ($l in $d7Lines) {
    $t = $l.Trim()
    if ($t -match '^<(div|section|article|header|nav|body|aside|main)' -or $t -match 'class="(module|lesson|container|layout|content|section)') {
        Write-Host "  $i : $t"
    }
    $i++
    if ($i -gt 200) { break }
}

Write-Host ""
Write-Host "========================================"
Write-Host "Done! Check day07 manually from above output."
Write-Host "========================================"
