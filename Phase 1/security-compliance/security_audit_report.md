# Security Audit — Phase 1 Baseline

**Date:** 2025-11-15  
**Scope:** Node hardening, RBAC, firewall, DDoS, transaction protections

## Findings (Initial)
- RBAC: default roles created; recommend least-privilege review.
- Firewall: internal-only access recommended for RPC nodes.
- DDoS: basic rate limiting implemented; integrate cloud-edge DDoS protection.

## Actions
- Schedule penetration test (external).
- Harden SSH access via bastion host.
- Implement secrets management (Vault) for keys and API secrets.
