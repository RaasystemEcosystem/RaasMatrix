import time
import pandas as pd
import os

MONITOR_DIR = "C:/Users/hp/Raasystem/RaasMatrix/ai/monitoring/"
NODES = ["validator1", "validator2", "validator3", "poa1"]

print("🧠 AI Optimization Engine Started...")

def analyze_node(node):
    path = os.path.join(MONITOR_DIR, f"{node}_processed.csv")
    if not os.path.exists(path):
        return None
    df = pd.read_csv(path)
    if df.empty:
        return None
    last_row = df.iloc[-1]
    # Simple heuristic: if failed_tx > 0 or latency > 200ms, suggest optimization
    suggestions = []
    if last_row.failed_tx > 0:
        suggestions.append("Check settlement failures")
    if last_row.latency > 200:
        suggestions.append("Reduce batch size / reroute transactions")
    if last_row.tps < 50:
        suggestions.append("Increase node resources or optimize consensus")
    return suggestions

while True:
    for node in NODES:
        result = analyze_node(node)
        if result:
            print(f"[{node}] ⚠️ Optimization Suggestions: {', '.join(result)}")
    time.sleep(5)
