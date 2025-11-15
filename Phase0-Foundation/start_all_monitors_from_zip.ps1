# Paths
$zipPath = "C:\Users\hp\Raasystem\RaasMatrix\monitoring_package_final.zip"
$extractPath = "C:\Users\hp\Raasystem\RaasMatrix\monitoring_live"

# Remove old folder if exists
if (Test-Path $extractPath) {
    Remove-Item -Path $extractPath -Recurse -Force
}

# Extract ZIP
Expand-Archive -Path $zipPath -DestinationPath $extractPath

Write-Host "✅ Monitoring package extracted to $extractPath"

# List of monitoring scripts
$scripts = @(
    "monitor_validator1.py",
    "monitor_validator2.py",
    "monitor_validator3.py",
    "monitor_poa1.py",
    "monitor_all_nodes.py"
)

# Launch each script in a separate PowerShell window
foreach ($script in $scripts) {
    $scriptPath = Join-Path $extractPath $script
    Start-Process powershell -ArgumentList "-NoExit", "-Command python `"$scriptPath`""
}

Write-Host "🚀 All monitoring scripts launched!"
