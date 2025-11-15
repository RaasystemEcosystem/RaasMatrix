import time
import pandas as pd
from pathlib import Path

NODE_NAME = "poa1"
LOG_FILE = Path(f"C:/Users/hp/Raasystem/RaasMatrix/logs/{NODE_NAME}.log")

def tail_logs(file_path, last_n=10):
    if not file_path.exists():
        return []
    with file_path.open("r") as f:
        lines = f.readlines()
    return lines[-last_n:]

def parse_line(line):
    try:
        parts = line.strip().split()
        tps = int(parts[1].split(":")[1])
        latency = int(parts[2].split(":")[1])
        failed = int(parts[3].split(":")[1])
        return tps, latency, failed
    except:
        return None, None, None

def main():
    print(f"🚀 Monitoring {NODE_NAME} started...")
    while True:
        lines = tail_logs(LOG_FILE, last_n=20)
        tps_list, latency_list, failed_list = [], [], []

        for line in lines:
            tps, latency, failed = parse_line(line)
            if tps is not None:
                tps_list.append(tps)
                latency_list.append(latency)
                failed_list.append(failed)

        if tps_list:
            avg_tps = sum(tps_list)/len(tps_list)
            avg_latency = sum(latency_list)/len(latency_list)
            total_failed = sum(failed_list)
            print(f"[{NODE_NAME}] Avg TPS: {avg_tps:.1f}, Avg Latency: {avg_latency:.1f}ms, Failed: {total_failed}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
