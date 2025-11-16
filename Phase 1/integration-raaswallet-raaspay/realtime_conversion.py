"""
realtime_conversion.py
Phase 1 — Raaskoin <-> Fiat conversion utilities using live gold price feed.
"""

def raaskoin_to_usd(raaskoin_amount: float, gold_price_per_gram_usd: float = 78.32) -> float:
    # Raaskoin is defined as 0.001 gram of gold per unit (example)
    grams_per_raaskoin = 0.001
    return raaskoin_amount * grams_per_raaskoin * gold_price_per_gram_usd

def usd_to_raaskoin(usd_amount: float, gold_price_per_gram_usd: float = 78.32) -> float:
    grams_per_raaskoin = 0.001
    return usd_amount / (grams_per_raaskoin * gold_price_per_gram_usd)

if __name__ == "__main__":
    print(raaskoin_to_usd(1000, 78.32))
