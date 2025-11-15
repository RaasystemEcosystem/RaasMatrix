import time
from pathlib import Path

# Define your nodes and their log files
NODES = {
    "validator1": "C:/Users/hp/Raasystem/RaasMatrix/logs/validator1.log",
    "validator2": "C:/Users/hp/Raasystem/RaasMatrix/logs/validator2.log",
    "validator3": "C:/Users/hp/Raasystem/RaasMatrix/logs/validator3.log",
    "poa1": "C:/Users/hp/Raasystem/RaasMatrix/logs/poa1.log"
}

def tail_logs(file_path, last_n=20):
    """Read the last N lines of a log file"""
    path = Path(file_path)
    if not path.exists():
        return []
    with path.open("r") as f:
        lines = f.readlines()
    return lines[-last_n:]

def parse_line(line):
    """Extract TPS, Latency, Failed from a log line"""
    try:
        parts = line.strip().split()
        tps = int(parts[1].split(":")[1])
        latency = int(parts[2].split(":")[1])
        failed = int(parts[3].split(":")[1])
        return tps, latency, failed
    except:
        return None, None, None

def main():
    print("🚀 Monitoring all nodes started...")
    while True:
        for node, log_file in NODES.items():
            lines = tail_logs(log_file, last_n=20)
            tps_list, latency_list, failed_list = [], [], []

            for line in lines:
                tps, latency, failed = parse_line(line)
                if tps is not None:
                    tps_list.append(tps)
                    latency_list.append(latency)
                    failed_list.append(failed)

            if tps_list:
                avg_tps = sum(tps_list) / len(tps_list)
                avg_latency = sum(latency_list) / len(latency_list)
                total_failed = sum(failed_list)
                print(f"[{node}] Avg TPS: {avg_tps:.1f}, Avg Latency: {avg_latency:.1f}ms, Failed: {total_failed}")
            else:
                print(f"[{node}] No log data yet.")

        print("-" * 60)
        time.sleep(5)  # update every 5 seconds

if __name__ == "__main__":
    main()
