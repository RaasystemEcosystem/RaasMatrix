$repoPath = "C:\Users\hp\Raasystem\RaasMatrix"
$scriptPath = "$repoPath\push_changes.ps1"

# Create a filesystem watcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $repoPath
$watcher.IncludeSubdirectories = $true
$watcher.Filter = "*.*"
$watcher.EnableRaisingEvents = $true

# Define the action on change
$action = {
    Start-Sleep -Milliseconds 500  # Small delay to allow file write
    & "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy Bypass -File $Event.SourceEventArgs.FullPath
    & $scriptPath
    Write-Host "Change detected. Auto-pushed at $(Get-Date)"
}

# Register events
Register-ObjectEvent $watcher Created -Action $action
Register-ObjectEvent $watcher Changed -Action $action
Register-ObjectEvent $watcher Deleted -Action $action
Register-ObjectEvent $watcher Renamed -Action $action

Write-Host "Watching for changes in $repoPath. Press Ctrl+C to stop."

# Keep script running
while ($true) { Start-Sleep 1 }
