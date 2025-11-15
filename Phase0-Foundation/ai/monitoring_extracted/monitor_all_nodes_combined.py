import os
import time
import pandas as pd

# Node log files
NODES = {
    "validator1": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\validator1.log",
    "validator2": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\validator2.log",
    "validator3": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\validator3.log",
    "poa1": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\poa1.log"
}

# Track last read position to avoid re-reading old lines
last_positions = {node: 0 for node in NODES}

def parse_log(lines):
    """Parse log lines to extract TPS, Latency, Failed"""
    tps_list, latency_list, failed_list = [], [], []
    for line in lines:
        if "TPS:" in line and "Latency:" in line and "Failed:" in line:
            parts = line.strip().split()
            tps = int(parts[1].split(":")[1])
            latency = int(parts[2].split(":")[1])
            failed = int(parts[3].split(":")[1])
            tps_list.append(tps)
            latency_list.append(latency)
            failed_list.append(failed)
    if tps_list:
        return {
            "Avg TPS": round(sum(tps_list)/len(tps_list), 1),
            "Avg Latency": round(sum(latency_list)/len(latency_list), 1),
            "Failed": sum(failed_list)
        }
    else:
        return {
            "Avg TPS": 0,
            "Avg Latency": 0,
            "Failed": 0
        }

def read_new_lines(file_path, last_pos):
    """Read only new lines from the log file"""
    if not os.path.exists(file_path):
        return [], last_pos
    with open(file_path, "r") as f:
        f.seek(last_pos)
        lines = f.readlines()
        last_pos = f.tell()
    return lines, last_pos

print("🚀 Monitoring all nodes combined...\n")

try:
    while True:
        os.system("cls")  # Clear console for live update
        combined_stats = {}
        for node, path in NODES.items():
            lines, last_positions[node] = read_new_lines(path, last_positions[node])
            stats = parse_log(lines)
            combined_stats[node] = stats

        # Display table using pandas for nice formatting
        df = pd.DataFrame(combined_stats).T
        print(df)
        print("\nUpdated: ", time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(2)  # Update every 2 seconds

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
