"""
stress_test_transactions.py
Local stress tester for RaasBridge RPC (very minimal).
"""

import requests
import time

RPC_URL = "http://localhost:8545"
NUM_TX = 100

def send_dummy_tx():
    # Placeholder: calls a health endpoint or creates raw txs using test accounts
    try:
        r = requests.get(f"{RPC_URL}/health", timeout=2)
        return r.status_code == 200
    except:
        return False

if __name__ == "__main__":
    start = time.time()
    sent = 0
    for i in range(NUM_TX):
        ok = send_dummy_tx()
        if ok:
            sent += 1
        time.sleep(0.01)  # 100 TPS target for stub
    print(f"Sent {sent}/{NUM_TX} dummy txs in {time.time() - start:.2f}s")
