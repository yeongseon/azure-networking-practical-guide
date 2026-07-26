---
description: Scaffold for a future Azure Networking troubleshooting lab covering private endpoint DNS zone link failure symptoms, recovery, and falsification evidence.
---

# Private Endpoint DNS link failure and recovery

This page is a scaffold only for issue #24. It establishes the canonical troubleshooting-lab shape for this repository without yet authoring the full reproducible experiment.

## Lab Metadata

| Field | Value |
| --- | --- |
| Status | Scaffold only |
| Scenario ID | ZLR-networking-01 |
| Candidate scope | Private endpoint DNS zone virtual network link failure and recovery |
| Full lab authoring | Planned in issue #24 |

## 1) Background

Placeholder: summarize the workload, DNS path, private endpoint dependency, and why a broken private DNS zone link changes resolution behavior.

## 2) Hypothesis

Placeholder: document the failure theory and the expected DNS behavior before and after the fix, including an explicit IF/THEN prediction.

## 3) Runbook

Placeholder: add the reproducible environment setup, failure injection, evidence collection commands, fix steps, and teardown sequence.

## 4) Experiment Log

Placeholder: record observed failure evidence, analysis, conclusion, and post-fix falsification evidence that proves recovery.

## Expected Evidence

Placeholder: define the pass/fail evidence table, expected DNS outputs, and any query or portal artifacts the full lab will require.

## Clean Up

Placeholder: remove lab-only DNS links, private endpoint resources, and supporting test infrastructure.

## Related Playbook

- [DNS Resolution Failures](../playbooks/dns/dns-resolution-failures.md)
- [Cannot Reach Private Endpoint](../playbooks/connectivity/cannot-reach-private-endpoint.md)

## See Also

- [Troubleshooting Lab Guides](index.md)
- [Troubleshooting Home](../index.md)
- [First 10 Minutes: DNS](../first-10-minutes/dns.md)

## Sources

- [Azure Private Endpoint private DNS zone values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)
- [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns-integration)
