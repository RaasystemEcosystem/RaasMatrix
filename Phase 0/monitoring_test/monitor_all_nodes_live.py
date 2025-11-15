import time
import os
from pathlib import Path
from colorama import init, Fore, Style
try:
    from win10toast import ToastNotifier
except ImportError:
    ToastNotifier = None

# Initialize colorama
init(autoreset=True)

# Path to monitoring folder
MONITOR_FOLDER = Path(__file__).parent

# Thresholds for alerts
FAILED_ALERT_THRESHOLD = 5
LATENCY_WARNING_THRESHOLD = 200  # ms

# Initialize toaster if available
toaster = ToastNotifier() if ToastNotifier else None

def get_nodes():
    """Automatically detect all .log files as nodes."""
    nodes = {}
    for log_file in MONITOR_FOLDER.glob("*.log"):
        node_name = log_file.stem
        nodes[node_name] = log_file
    return nodes

def tail_logs(file_path, last_n=20):
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

def format_line(node, avg_tps, avg_latency, total_failed):
    tps_color = Fore.GREEN if total_failed == 0 else Fore.RED
    latency_color = Fore.YELLOW if avg_latency > LATENCY_WARNING_THRESHOLD else Fore.GREEN
    fail_color = Fore.RED if total_failed >= FAILED_ALERT_THRESHOLD else Fore.GREEN
    return (f"[{node}] "
            f"Avg TPS: {tps_color}{avg_tps:.1f}{Style.RESET_ALL}, "
            f"Avg Latency: {latency_color}{avg_latency:.1f}ms{Style.RESET_ALL}, "
            f"Failed: {fail_color}{total_failed}{Style.RESET_ALL}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def alert_node(node, total_failed):
    print(Fore.RED + f"❌ ALERT: {node} has {total_failed} failed transactions!" + Style.RESET_ALL)
    print('\a')  # System beep
    if toaster:
        toaster.show_toast("RaasMatrix Node Alert",
                           f"{node} failed {total_failed} transactions!",
                           duration=5,
                           threaded=True)

def main():
    print("🚀 Monitoring all nodes live...")
    while True:
        clear_console()
        print("🚀 Monitoring all nodes live...\n" + "-"*60)
        nodes = get_nodes()  # detect nodes dynamically

        for node, log_path in nodes.items():
            lines = tail_logs(log_path, last_n=20)
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
                print(format_line(node, avg_tps, avg_latency, total_failed))
                if total_failed >= FAILED_ALERT_THRESHOLD:
                    alert_node(node, total_failed)
            else:
                print(f"[{node}] No log data yet.")

        print("-"*60)
        time.sleep(5)

if __name__ == "__main__":
    main()
