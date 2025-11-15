# ===============================================
# Phase0-Setup-Intelligent.ps1
# Fully Intelligent RaasMatrix Phase 0 Setup
# ===============================================

# Base path
$RAAS_PATH = "C:\Users\hp\Raasystem\RaasMatrix"

Write-Output "🚀 Starting Intelligent Phase 0 setup at $RAAS_PATH"

# -----------------------------
# 1️⃣ Create folders
# -----------------------------
$folders = @(
    "$RAAS_PATH\nodes\validator1\config",
    "$RAAS_PATH\nodes\validator1\data",
    "$RAAS_PATH\nodes\validator1\logs",
    "$RAAS_PATH\nodes\validator1\keystore",
    
    "$RAAS_PATH\nodes\validator2\config",
    "$RAAS_PATH\nodes\validator2\data",
    "$RAAS_PATH\nodes\validator2\logs",
    "$RAAS_PATH\nodes\validator2\keystore",

    "$RAAS_PATH\nodes\validator3\config",
    "$RAAS_PATH\nodes\validator3\data",
    "$RAAS_PATH\nodes\validator3\logs",
    "$RAAS_PATH\nodes\validator3\keystore",

    "$RAAS_PATH\nodes\poa1\config",
    "$RAAS_PATH\nodes\poa1\data",
    "$RAAS_PATH\nodes\poa1\logs",
    "$RAAS_PATH\nodes\poa1\keystore",

    "$RAAS_PATH\ai\monitoring",
    "$RAAS_PATH\ai\optimization",
    "$RAAS_PATH\ai\anomaly-detect",
    "$RAAS_PATH\ai\training",
    "$RAAS_PATH\scripts",
    "$RAAS_PATH\logs",
    "$RAAS_PATH\contracts",
    "$RAAS_PATH\config",
    "$RAAS_PATH\tests\unit",
    "$RAAS_PATH\tests\integration",
    "$RAAS_PATH\tests\e2e"
)

foreach ($f in $folders) { New-Item -ItemType Directory -Force -Path $f | Out-Null }
Write-Output "✅ All folders created."

# -----------------------------
# 2️⃣ Initialize Genesis (placeholder)
# -----------------------------
Write-Output "⚡ Initializing genesis.json (replace with RaasMatrix CLI commands)"
New-Item -ItemType File -Force -Path "$RAAS_PATH\config\genesis.json" | Out-Null

# Copy to all nodes
$nodes = @("validator1","validator2","validator3","poa1")
foreach ($n in $nodes) {
    Copy-Item "$RAAS_PATH\config\genesis.json" "$RAAS_PATH\nodes\$n\config\genesis.json" -Force
}
Write-Output "✅ Genesis.json copied to all nodes."

# -----------------------------
# 3️⃣ Launch nodes if executable exists
# -----------------------------
$exePath = "$RAAS_PATH\raasmatrix.exe"
if (Test-Path $exePath) {
    Write-Output "🚀 Launching nodes with AI telemetry..."
    foreach ($n in $nodes) {
        $telemetryLog = "$RAAS_PATH\ai\monitoring\$n.log"
        Start-Process -FilePath $exePath -ArgumentList "start --node $RAAS_PATH\nodes\$n --telemetry $telemetryLog" -NoNewWindow
    }
    Write-Output "✅ Nodes started."
} else {
    Write-Output "⚠️ RaasMatrix executable not found at $exePath. Skipping node launch."
}

# -----------------------------
# 4️⃣ Launch AI Monitoring & Optimization
# -----------------------------
Write-Output "🧠 Launching AI monitoring and optimization scripts..."

foreach ($n in $nodes) {
    $monitorScript = "$RAAS_PATH\ai\monitoring\monitor_$n.py"
    if (Test-Path $monitorScript) {
        Start-Process -FilePath "python" -ArgumentList $monitorScript -NoNewWindow
        Write-Output "✅ AI Monitoring started for $n"
    } else {
        Write-Output "⚠️ Monitoring script not found for $n. Place monitor_$n.py in ai\monitoring\."
    }
}

# Optimization script
$optScript = "$RAAS_PATH\ai\optimization\optimizer.py"
if (Test-Path $optScript) {
    Start-Process -FilePath "python" -ArgumentList $optScript -NoNewWindow
    Write-Output "✅ AI Optimization script started."
} else {
    Write-Output "⚠️ Optimization script not found. Place optimizer.py in ai\optimization\."
}

# -----------------------------
# 5️⃣ Placeholder for RWA mint & stress test
# -----------------------------
Write-Output "💡 Place your scripts (mintRWA.js, stressTest.js) inside $RAAS_PATH\scripts and run with Node.js"

# -----------------------------
# Done
# -----------------------------
Write-Output "🎯 Intelligent Phase 0 setup complete. RaasMatrix is now ready for AI-integrated testing."
