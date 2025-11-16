# Production Rollout Plan — Phase 1

## Overview
Sequence to safely move Phase 1 optimizations from staging → canary → production.

## Steps
1. Validate metrics in staging (TPS, latency, error rates).
2. Canary: deploy to 10% of production validators.
3. Run stress tests (simulate 2k TPS) for 2 hours.
4. If KPIs pass, gradually increase to 50% then 100% over 24 hours.
5. Monitor alerts, rollback on critical failures.

## Rollback plan
- Use Kubernetes rollback to previous Deployment revision.
- Revert consensus changes via `consensus_config.toml` backup.

## Contacts
- SRE: sre@raasystem.example
- On-call lead: oncall@raasystem.example
