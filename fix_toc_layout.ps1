# fix_toc_layout.ps1
# Fixes the TOC sidebar being nested inside <main class="lesson-content">
# for all lesson files where toc-inside=True (days 08-30)
# Strategy: Find the <aside class="toc-sidebar"...> block inside main,
# cut it out, and paste it AFTER </main> as a sibling in the flex row.

$lessonsDir = "C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons"
$fixedCount  = 0
$skippedCount = 0

# Files that need fixing: toc-sidebar is nested inside main
$targetFiles = @(
    "day08.html","day09.html","day10.html","day12.html","day13.html",
    "day14.html","day15.html","day16.html","day17.html","day18.html",
    "day19.html","day20.html","day21.html","day22.html","day23.html",
    "day24.html","day25.html","day26.html","day27.html","day28.html",
    "day29.html","day30.html"
)

# Improved inline CSS block to inject for lesson layout (same as day01 fix)
$layoutCssBlock = @"
        .lesson-layout {
            display: flex;
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
            align-items: flex-start;
        }
        .lesson-content {
            flex: 3;
            min-width: 0;
        }
        .toc-sidebar {
            flex: 0 0 260px;
            width: 260px;
            position: sticky;
            top: 2rem;
            max-height: calc(100vh - 4rem);
            overflow-y: auto;
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            order: 2;
            z-index: 1;
        }
        .toc-link {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.45rem 0.75rem;
            color: #475569;
            text-decoration: none;
            border-radius: 6px;
            border-left: 3px solid transparent;
            font-size: 0.85rem;
            transition: all 0.15s ease;
            line-height: 1.4;
        }
        .toc-link:hover { background: #eff6ff; color: #2563eb; border-left-color: #93c5fd; }
        .toc-link.active { color: #2563eb; font-weight: 700; background: #eff6ff; border-left-color: #2563eb; }
        .toc-icon { font-size: 0.8rem; opacity: 0.6; flex-shrink: 0; }
        @media (max-width: 900px) {
            .lesson-layout { flex-direction: column; }
            .toc-sidebar { position: static; width: 100%; flex: none; order: -1; max-height: 300px; }
        }
"@

foreach ($fileName in $targetFiles) {
    $filePath = Join-Path $lessonsDir $fileName

    if (-not (Test-Path $filePath)) {
        Write-Host "  SKIP (not found): $fileName"
        $skippedCount++
        continue
    }

    # Read as single string preserving line endings
    $content = [System.IO.File]::ReadAllText($filePath)

    # Check: is toc-sidebar really inside main?
    # Pattern: <main...> ... <aside class="toc-sidebar"
    if ($content -notmatch '(?s)<main[^>]*>.*?<aside[^>]*class="toc-sidebar"') {
        Write-Host "  SKIP (no inside-toc): $fileName"
        $skippedCount++
        continue
    }

    # ── Step 1: Extract the complete <aside class="toc-sidebar"...>...</aside> block
    # We match from <aside class="toc-sidebar" to matching </aside>
    $asidePattern = '(?s)(\s*<aside[^>]*class="toc-sidebar"[^>]*>.*?</aside>)'
    $asideMatch = [regex]::Match($content, $asidePattern)

    if (-not $asideMatch.Success) {
        Write-Host "  WARN (aside not matched): $fileName"
        $skippedCount++
        continue
    }

    $asideBlock = $asideMatch.Value

    # ── Step 2: Remove the aside block from inside main
    $contentWithoutAside = $content -replace [regex]::Escape($asideBlock), ''

    # ── Step 3: Insert the aside AFTER </main> as a sibling
    # Find the first </main> and insert after it
    $fixed = $contentWithoutAside -replace '(</main>)', "`$1`n$asideBlock"

    # ── Step 4: Fix layout CSS if old/wrong styles exist
    # Replace old toc-sidebar height:calc with max-height:calc
    $fixed = $fixed -replace 'height: calc\(100vh - 4rem\)', 'max-height: calc(100vh - 4rem)'
    $fixed = $fixed -replace '\.toc-sidebar \{([^}]*?)flex: 1;', '.toc-sidebar {$1flex: 0 0 260px; width: 260px;'
    
    # Fix align-items on lesson-layout if missing
    $fixed = $fixed -replace '(\.lesson-layout \{[^}]*?)(display: flex;)', '$1display: flex;$2'
    $fixed = $fixed -replace '(\.lesson-layout \{[^}]*?)(\})', 
        { if ($_.Value -notmatch 'align-items') { $_.Value -replace '(\})', "    align-items: flex-start;`n        `$1" } else { $_.Value } }

    # Write back
    [System.IO.File]::WriteAllText($filePath, $fixed, [System.Text.Encoding]::UTF8)
    Write-Host "  FIXED: $fileName"
    $fixedCount++
}

Write-Host ""
Write-Host "========================================"
Write-Host "Done! Fixed: $fixedCount | Skipped: $skippedCount"
Write-Host "========================================"
