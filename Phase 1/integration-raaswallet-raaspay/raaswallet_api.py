"""
raaswallet_api.py
Phase 1 — Wallet gateway interface (stub)
"""

from typing import Dict

WALLET_RPC = "http://localhost:8546"  # Example RPC for wallet service

def get_balance(address: str) -> Dict:
    """
    Return mock balance for an address.
    """
    print(f"[raaswallet] get_balance {address}")
    return {"address": address, "balance": 1000000}

def send_transaction(from_addr: str, to_addr: str, amount: int) -> Dict:
    """
    Send a transaction (placeholder).
    """
    print(f"[raaswallet] send {amount} from {from_addr} -> {to_addr}")
    return {"status": "sent", "tx_hash": "0xdeadbeef"}
