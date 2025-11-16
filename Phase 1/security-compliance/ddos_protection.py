"""
ddos_protection.py
Simple rate limiting example for HTTP endpoints (placeholder).
"""

from collections import defaultdict
import time

class SimpleRateLimiter:
    def __init__(self, max_requests_per_sec=200):
        self.requests = defaultdict(list)
        self.threshold = max_requests_per_sec

    def allow(self, ip: str) -> bool:
        now = time.time()
        window = 1.0
        history = self.requests[ip]
        # purge old
        self.requests[ip] = [t for t in history if now - t < window]
        self.requests[ip].append(now)
        return len(self.requests[ip]) <= self.threshold

# Example usage
if __name__ == "__main__":
    rl = SimpleRateLimiter(200)
    print(rl.allow("127.0.0.1"))
