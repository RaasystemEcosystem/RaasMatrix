# Simulation Plan — Phase 1

## Objectives
- Simulate realistic traffic profiles to validate TPS and latency.
- Inject node failure scenarios to test self-heal.

## Tools
- `stress_test_transactions.py` (local)
- Locust / K6 for HTTP/gRPC load generation

## Scenarios
1. Normal load: 200 TPS for 1 hour.
2. Peak load: 2,000 TPS for 30 minutes.
3. Burst: 5,000 TPS for 60 seconds.
4. Failure injection: kill one validator, observe self-heal.

## Metrics to record
- TPS, latency, block time, failed txs, CPU/RAM.
