# Paths to the Python monitoring scripts
$monitorScripts = @(
    "C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring\monitor_validator1.py",
    "C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring\monitor_validator2.py",
    "C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring\monitor_validator3.py",
    "C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring\monitor_poa1.py"
)

# Start all monitors in background jobs and display output in one console
$jobs = @()
foreach ($script in $monitorScripts) {
    $jobs += Start-Job -ScriptBlock {
        param($s)
        python $s
    } -ArgumentList $script
}

Write-Host "🚀 All monitors started in background jobs."

# Continuously show output from all jobs
while ($true) {
    Clear-Host
    foreach ($job in $jobs) {
        $output = Receive-Job -Job $job -Keep
        if ($output) {
            Write-Output $output
        }
    }
    Start-Sleep -Seconds 2
}
