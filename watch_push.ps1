# ==== Config ====
$repoPath = "C:\Users\hp\Raasystem\RaasMatrix"
$commitMessage = "Auto-update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$ignoreFile = "watch_push.ps1"  # Don't trigger on this script itself

# ==== Navigate to repo ====
Set-Location $repoPath

# ==== Ensure remote URL is correct ====
$desiredRemote = "https://github.com/RaasystemEcosystem/RaasMatrix.git"
$currentRemote = git remote get-url origin 2>$null
if ($currentRemote -ne $desiredRemote) {
    git remote set-url origin $desiredRemote
    Write-Host "Updated remote URL to $desiredRemote"
}

# ==== Create filesystem watcher ====
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $repoPath
$watcher.IncludeSubdirectories = $true
$watcher.Filter = "*.*"
$watcher.EnableRaisingEvents = $true

# ==== Define action on change ====
$action = {
    $changedFile = $Event.SourceEventArgs.FullPath
    if ($changedFile -notlike "*\$ignoreFile") {
        Start-Sleep -Milliseconds 500  # Allow file writes to complete
        try {
            # Pull latest changes first
            git pull origin main --ff-only | Out-Null
        } catch {
            Write-Host "$(Get-Date -Format 'HH:mm:ss') - Warning: Pull failed."
        }

        # Stage all changes, including renames
        git add -A

        # Commit & push if there are changes
        $changes = git status --porcelain
        if ($changes) {
            git commit -m "$commitMessage" | Out-Null
            git push origin main | Out-Null
            Write-Host "$(Get-Date -Format 'HH:mm:ss') - Change detected in $changedFile. Auto-pushed."
        }
    }
}

# ==== Register events ====
Register-ObjectEvent $watcher Created -Action $action
Register-ObjectEvent $watcher Changed -Action $action
Register-ObjectEvent $watcher Deleted -Action $action
Register-ObjectEvent $watcher Renamed -Action $action

Write-Host "Watching for changes in $repoPath. Press Ctrl+C to stop."

# ==== Keep script running ====
while ($true) { Start-Sleep 1 }
