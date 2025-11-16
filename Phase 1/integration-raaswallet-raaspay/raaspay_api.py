"""
raaspay_api.py
Phase 1 — Merchant settlement & payment gateway stubs for Raaspay integration.
"""

import requests
from typing import Dict

RAASPAY_API_BASE = "https://sandbox.raaspay.example/api/v1"  # Example sandbox

def create_payment_intent(amount_cents: int, currency: str, merchant_id: str) -> Dict:
    """
    Create a payment intent for merchant settlement.
    """
    payload = {
        "merchant_id": merchant_id,
        "amount": amount_cents,
        "currency": currency
    }
    # TODO: replace with authenticated requests
    print(f"[raaspay] create_intent {payload}")
    return {"status": "created", "intent_id": "intent_12345"}

def capture_payment(intent_id: str) -> Dict:
    """
    Capture a previously authorized payment.
    """
    print(f"[raaspay] capture {intent_id}")
    return {"status": "captured", "capture_id": "cap_12345"}
