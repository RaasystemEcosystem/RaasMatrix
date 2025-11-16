"""
caching_service.py
A lightweight in-memory cache for frequently accessed RWA and token metadata.
"""

import time
from typing import Any

class SimpleCache:
    def __init__(self, ttl_seconds=300):
        self.ttl = ttl_seconds
        self.store = {}

    def get(self, key: str) -> Any:
        rec = self.store.get(key)
        if not rec:
            return None
        value, ts = rec
        if time.time() - ts > self.ttl:
            del self.store[key]
            return None
        return value

    def set(self, key: str, value: Any):
        self.store[key] = (value, time.time())

# Example usage
if __name__ == "__main__":
    c = SimpleCache(60)
    c.set("RWA_001", {"owner": "Alice", "value": 1000})
    print(c.get("RWA_001"))
