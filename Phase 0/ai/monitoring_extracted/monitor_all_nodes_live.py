import os
import time
import pandas as pd
from colorama import Fore, Style, init

init(autoreset=True)

# Node log files
NODES = {
    "validator1": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\validator1.log",
    "validator2": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\validator2.log",
    "validator3": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\validator3.log",
    "poa1": r"C:\Users\hp\Raasystem\RaasMatrix\ai\monitoring_extracted\poa1.log"
}

last_positions = {node: 0 for node in NODES}

def parse_log(lines):
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
            "Avg TPS": round(sum(tps_list)/len(tps_list),1),
            "Max TPS": max(tps_list),
            "Min TPS": min(tps_list),
            "Avg Latency": round(sum(latency_list)/len(latency_list),1),
            "Max Latency": max(latency_list),
            "Min Latency": min(latency_list),
            "Failed": sum(failed_list)
        }
    return {"Avg TPS":0,"Max TPS":0,"Min TPS":0,"Avg Latency":0,"Max Latency":0,"Min Latency":0,"Failed":0}

def read_new_lines(file_path, last_pos):
    if not os.path.exists(file_path):
        return [], last_pos
    with open(file_path, "r") as f:
        f.seek(last_pos)
        lines = f.readlines()
        last_pos = f.tell()
    return lines, last_pos

def colorize(row):
    tps_color = Fore.RED if row["Avg TPS"] < 80 else ""
    latency_color = Fore.YELLOW if row["Max Latency"] > 180 else ""
    failed_color = Fore.RED if row["Failed"] > 0 else ""
    return [
        f"{tps_color}{row['Avg TPS']}{Style.RESET_ALL}",
        f"{row['Max TPS']}",
        f"{row['Min TPS']}",
        f"{latency_color}{row['Avg Latency']}{Style.RESET_ALL}",
        f"{row['Max Latency']}",
        f"{row['Min Latency']}",
        f"{failed_color}{row['Failed']}{Style.RESET_ALL}"
    ]

print("🚀 Live Monitoring All Nodes (1s refresh)...\n")

try:
    while True:
        os.system("cls")
        combined_stats = {}
        for node, path in NODES.items():
            lines, last_positions[node] = read_new_lines(path, last_positions[node])
            stats = parse_log(lines)
            combined_stats[node] = stats

        df = pd.DataFrame(combined_stats).T
        df_colored = pd.DataFrame([colorize(row) for _, row in df.iterrows()],
                                  index=df.index,
                                  columns=["Avg TPS","Max TPS","Min TPS","Avg Latency","Max Latency","Min Latency","Failed"])

        print(df_colored)
        print("\nUpdated:", time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
