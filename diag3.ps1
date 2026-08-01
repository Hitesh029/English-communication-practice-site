$dir = "C:\Users\ASUS\.gemini\antigravity\scratch\English-Communication-Master\lessons"
$files = @("day02.html","day07.html","day10.html")

foreach ($name in $files) {
    $c = [System.IO.File]::ReadAllText("$dir\$name")
    $mainEnd    = $c.IndexOf('</main>')
    $asideStart = $c.IndexOf('<aside')
    Write-Host "--- $name ---"
    Write-Host "  mainEnd=$mainEnd  asideStart=$asideStart  asideAfterMain=$($asideStart -gt $mainEnd)"
    $lines = $c -split "`n"
    $i = 1
    $count = 0
    foreach ($l in $lines) {
        $t = $l.Trim()
        if ($t -match '<main|</main>|<aside|</aside>|sidebar|content-col|lesson-content') {
            Write-Host "  LINE $i : $t"
            $count++
            if ($count -ge 15) { break }
        }
        $i++
    }
    Write-Host ""
}
