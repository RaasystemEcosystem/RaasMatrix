# start_all_monitors.ps1
# Launch all RaasMatrix node monitors in separate PowerShell windows

$basePath = "C:\Users\hp\Raasystem\RaasMatrix\monitoring_test"

# List of monitoring scripts
$scripts = @(
    "monitor_validator1.py",
    "monitor_validator2.py",
    "monitor_validator3.py",
    "monitor_poa1.py"
)

# Start each script in a new PowerShell window
foreach ($script in $scripts) {
    Start-Process powershell -ArgumentList "-NoExit", "-Command `"$basePath\$script`""
}
