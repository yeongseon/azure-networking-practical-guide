---
content_sources:
  diagrams:
  - id: operations-create-vnet-and-subnets-flow
    type: flowchart
    source: mslearn-adapted
    description: Runbook flow
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-cli
    - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-subnet
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-cli
    verified: false
  - claim: Core Azure networking guidance on this page should remain traceable to
      the listed sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-cli
    verified: false
---

# Create VNet and Subnets

Create a VNet and subnet baseline with clear address ownership and validation evidence.

## Prerequisites

- Azure CLI is installed and authenticated with permission to read and change the target networking resources.
- Required variables such as `RG`, `LOCATION`, `VNET_NAME`, and resource-specific names are set before running commands.
- The intended source, destination, protocol, port, DNS name, and rollback owner are known.
- A maintenance window is approved for production path changes.

## When to Use

A workload needs a new spoke VNet with application and private endpoint subnets.

<!-- diagram-id: operations-create-vnet-and-subnets-flow -->
```mermaid
flowchart TD
    A[Confirm path intent] --> B[Capture current state]
    B --> C[Apply network change]
    C --> D[Validate route DNS and security]
    D --> E[Record rollback evidence]
```

## Procedure

1. Confirm approved address space and non-overlap.
2. Create the VNet and initial subnets.
3. Associate NSG and route table resources only after their intended rules are reviewed.
4. Validate the address prefixes and subnet inventory.

### Command sequence

```bash
az group create \
    --name $RG \
    --location $LOCATION \
    --output json

az network vnet create \
    --resource-group $RG \
    --name $VNET_NAME \
    --location $LOCATION \
    --address-prefixes 10.60.0.0/16 \
    --subnet-name $SUBNET_NAME \
    --subnet-prefixes 10.60.1.0/24 \
    --output json
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$LOCATION` | Azure region for regional networking resources. |
| `$VNET_NAME` | Virtual network being created, linked, or inspected. |
| `$SUBNET_NAME` | Subnet being created, delegated, secured, or tested. |
| `--name` | Identifies the target Azure networking resource. |
| `--location` | Selects the Azure region for creation or lookup. |
| `--output` | Controls output format for review or automation. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--address-prefixes` | Defines VNet address ranges. |
| `--subnet-name` | Names the subnet created with a VNet. |
| `--subnet-prefixes` | Defines subnet address ranges. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

## Verification

```bash
az network vnet show \
    --resource-group $RG \
    --name $VNET_NAME \
    --query "{name:name,addressSpace:addressSpace.addressPrefixes,subnets:subnets[].name}" \
    --output json
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$VNET_NAME` | Virtual network being created, linked, or inspected. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--name` | Identifies the target Azure networking resource. |
| `--query` | Filters output to the evidence operators need. |
| `--output` | Controls output format for review or automation. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

Confirm from the actual source network that DNS, route, security rule, and service response match the intended design.

## Rollback / Troubleshooting

```bash
az network vnet delete \
    --resource-group $RG \
    --name $VNET_NAME
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$VNET_NAME` | Virtual network being created, linked, or inspected. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--name` | Identifies the target Azure networking resource. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

- If validation fails, stop further changes and capture current route, NSG, DNS, and Activity Log evidence.
- Roll back the smallest changed control first: rule, route, DNS link, peering flag, or private endpoint connection.
- Escalate when policy, capacity, provider circuit, or private endpoint approval state blocks the documented path.

## See Also

- [Network Design Baseline](../best-practices/network-design-baseline.md)
- [Monitor Network Paths](monitor-network-paths.md)
- [Troubleshooting Playbooks](../troubleshooting/playbooks/index.md)

## Sources

- [Quick Create Cli](https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-cli)
- [Virtual Network Manage Subnet](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-subnet)
