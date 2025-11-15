# ================================================
# Smart Dummy Telemetry Generator for RaasMatrix
# ================================================

$nodes = @("validator1","validator2","validator3","poa1")
$logPath = "C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring"

Write-Output "🟢 Starting smart dummy telemetry generation..."

while ($true) {
    foreach ($node in $nodes) {
        # Base TPS and latency ranges
        $baseTPS = Get-Random -Minimum 60 -Maximum 120
        $baseLatency = Get-Random -Minimum 100 -Maximum 200
        $failed = 0

        # Introduce occasional spikes or failures
        $randEvent = Get-Random -Minimum 1 -Maximum 100
        if ($randEvent -le 10) { 
            # 10% chance of latency spike
            $latency = $baseLatency + (Get-Random -Minimum 50 -Maximum 150)
        } else { 
            $latency = $baseLatency
        }

        if ($randEvent -ge 85) { 
            # 15% chance of failed transactions
            $failed = Get-Random -Minimum 1 -Maximum 5
        }

        # Simulate TPS dip if failures occur
        $tps = $baseTPS - ($failed * 5)

        $line = "[time] TPS:$tps Latency:$latency Failed:$failed"
        Add-Content "$logPath\$node.log" $line
    }

    Start-Sleep -Seconds 2
}
