---
description: Azure Networking troubleshooting labs hub for reproducible experiments, evidence collection, and future lab-guides aligned to the series methodology.
---

# Troubleshooting Lab Guides

Troubleshooting labs are reproducible experiments for proving or disproving a networking failure hypothesis, collecting evidence, and validating recovery steps before using the pattern in production investigations.

This repository is establishing the lab-guides surface now so future labs can follow the series contract consistently: hypothesis-driven runbooks, explicit evidence, and a falsification step that proves the fix worked.

## How to use these labs

- Start with the matching [playbook](../playbooks/index.md) when you need diagnosis guidance for a live incident.
- Use a lab guide when you want a controlled reproduction with a documented hypothesis, experiment log, and recovery path.
- Expect every full lab to map the 16 troubleshooting methodology concepts into the canonical lab structure rather than using the concepts as literal headings.

## Planned labs

| Lab | Status | Focus | Related playbook |
| --- | --- | --- | --- |
| [Private Endpoint DNS link failure](private-endpoint-dns-link-failure.md) | Scaffold only | Missing or incorrect private DNS zone links break expected private endpoint name resolution and recovery validation. | [DNS Resolution Failures](../playbooks/dns/dns-resolution-failures.md), [Cannot Reach Private Endpoint](../playbooks/connectivity/cannot-reach-private-endpoint.md) |

## See Also

- [Troubleshooting Home](../index.md)
- [Playbooks](../playbooks/index.md)
- [First 10 Minutes](../first-10-minutes/index.md)
- [DNS Resolution Failures](../playbooks/dns/dns-resolution-failures.md)
- [Cannot Reach Private Endpoint](../playbooks/connectivity/cannot-reach-private-endpoint.md)
