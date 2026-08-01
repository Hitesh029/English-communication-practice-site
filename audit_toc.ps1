$dir = "C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons"
$all = Get-ChildItem $dir -Filter "*.html" | Sort-Object Name

Write-Host "=== FINAL LAYOUT AUDIT: All 30 Lesson Files ==="
Write-Host "Checking: aside must NOT be nested inside main"
Write-Host ""

$allGood    = $true
$okCount    = 0
$brokenList = New-Object System.Collections.Generic.List[string]

foreach ($f in $all) {
    $c = [System.IO.File]::ReadAllText($f.FullName)

    $mainOpen  = $c.IndexOf('<main')
    $mainClose = $c.IndexOf('</main>')
    $asideOpen = $c.IndexOf('<aside')

    # BROKEN: aside is nested inside main (between open and close of main)
    $insideMain = ($mainOpen -ge 0) -and ($mainClose -ge 0) -and ($asideOpen -ge 0) -and ($asideOpen -gt $mainOpen) -and ($asideOpen -lt $mainClose)
    $noAside    = ($asideOpen -lt 0)

    if ($insideMain) {
        $tag = "[BROKEN - aside nested inside main]"
        $allGood = $false
        $brokenList.Add($f.Name)
    } elseif ($noAside) {
        $tag = "[WARNING - no aside found]"
        $allGood = $false
        $brokenList.Add($f.Name)
    } else {
        $tag = "[OK - aside is flex sibling]"
        $okCount++
    }

    Write-Host "$tag  $($f.Name)"
}

Write-Host ""
Write-Host "=============================="
Write-Host "OK     : $okCount / 30"
Write-Host "Issues : $($brokenList.Count) / 30"
if ($brokenList.Count -gt 0) {
    foreach ($n in $brokenList) {
        Write-Host "  - $n"
    }
}
Write-Host "=============================="
