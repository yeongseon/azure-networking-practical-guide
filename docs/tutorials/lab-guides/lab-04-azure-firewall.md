---
content_sources:
  diagrams:
  - id: lab-04-azure-firewall
    type: flowchart
    source: mslearn-adapted
    mslearn_url: https://learn.microsoft.com/en-us/azure/firewall/overview
    based_on:
    - https://learn.microsoft.com/en-us/azure/firewall/deploy-cli
    - https://learn.microsoft.com/en-us/azure/firewall/firewall-diagnostics
validation:
  az_cli:
    last_tested: null
    cli_version: null
    result: not_tested
  bicep:
    last_tested: null
    result: not_tested
content_validation:
  status: verified
  last_reviewed: '2026-05-23'
  reviewer: agent
  core_claims:
  - claim: This page uses Microsoft Learn as the primary source basis for its Azure-specific
      guidance.
    source: https://learn.microsoft.com/en-us/azure/firewall/overview
    verified: true
---
# Lab 04: Azure Firewall

Deploy Azure Firewall with a simple spoke subnet, force egress through the firewall using a route table, and validate both allowed and denied traffic so teams can learn how routing and firewall policy interact in practice.

## Lab Metadata

| Field | Value |
|---|---|
| Difficulty | Advanced |
| Estimated Duration | 75-105 minutes |
| Focus | Azure Firewall deployment, UDR-based egress control, diagnostics, deny troubleshooting |
| Tooling | Azure CLI, Network Watcher, Log Analytics optional |

## Prerequisites

- Permission to create Azure Firewall, public IPs, route tables, and a test VM.
- A workspace ID if you want to stream logs to Log Analytics during the lab.
- A resource group such as `$RG=rg-net-lab04` and location such as `$LOCATION=koreacentral`.
- Budget awareness: Azure Firewall incurs hourly and data-processing charges. Tear down promptly after the lab.

## Architecture Diagram

<!-- diagram-id: lab-04-azure-firewall -->
```mermaid
flowchart TD
    Workload[Spoke VM] --> UDR[Route Table 0.0.0.0/0]
    UDR --> Firewall[Azure Firewall]
    Firewall --> Internet[Internet]
    Firewall --> Logs[Firewall logs]
    Ops[Operator] --> Firewall
```

## Step-by-Step Instructions

### Step 1: Create the VNet, subnets, and public IP

```bash
az group create \
    --name $RG \
    --location $LOCATION

az network vnet create \
    --resource-group $RG \
    --name vnet-fw-lab04 \
    --location $LOCATION \
    --address-prefixes 10.140.0.0/16 \
    --subnet-name AzureFirewallSubnet \
    --subnet-prefixes 10.140.1.0/24

az network vnet subnet create \
    --resource-group $RG \
    --vnet-name vnet-fw-lab04 \
    --name workload \
    --address-prefixes 10.140.2.0/24

az network public-ip create \
    --resource-group $RG \
    --name pip-fw04 \
    --sku Standard \
    --allocation-method Static
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$LOCATION` | Azure region for regional networking resources. |
| `--name` | Identifies the target Azure networking resource. |
| `--location` | Selects the Azure region for creation or lookup. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--address-prefixes` | Defines VNet address ranges. |
| `--subnet-name` | Names the subnet created with a VNet. |
| `--subnet-prefixes` | Defines subnet address ranges. |
| `--vnet-name` | Selects the virtual network containing the subnet or peering. |
| `--sku` | Azure CLI option used to scope or shape the network operation. |
| `--allocation-method` | Azure CLI option used to scope or shape the network operation. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

This layout mirrors the minimum production pattern of firewall plus workload subnet.

#### Why this step matters

- Validate firewall policy, route table next hop, DNS behavior, and egress logs before continuing.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 2: Create the firewall and firewall policy

```bash
az network firewall policy create \
    --resource-group $RG \
    --name fwp-lab04 \
    --location $LOCATION

az network firewall create \
    --resource-group $RG \
    --name fw-lab04 \
    --location $LOCATION \
    --firewall-policy fwp-lab04

az network firewall ip-config create \
    --resource-group $RG \
    --firewall-name fw-lab04 \
    --name fwconfig \
    --public-ip-address pip-fw04 \
    --vnet-name vnet-fw-lab04
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$LOCATION` | Azure region for regional networking resources. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--name` | Identifies the target Azure networking resource. |
| `--location` | Selects the Azure region for creation or lookup. |
| `--firewall-policy` | Azure CLI option used to scope or shape the network operation. |
| `--firewall-name` | Azure CLI option used to scope or shape the network operation. |
| `--public-ip-address` | Azure CLI option used to scope or shape the network operation. |
| `--vnet-name` | Selects the virtual network containing the subnet or peering. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

Wait for provisioning to finish before moving on. Firewall deployment can take several minutes.

#### Why this step matters

- Validate firewall policy, route table next hop, DNS behavior, and egress logs before continuing.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 3: Deploy a test VM and forced-tunnel route table

```bash
az vm create \
    --resource-group $RG \
    --name vm-egress04 \
    --image Ubuntu2204 \
    --size Standard_B1s \
    --vnet-name vnet-fw-lab04 \
    --subnet workload \
    --admin-username azureuser \
    --generate-ssh-keys \
    --public-ip-address ""

FW_PRIVATE_IP=$(az network firewall ip-config list --resource-group $RG --firewall-name fw-lab04 --query "[0].privateIpAddress" --output tsv)
az network route-table create \
    --resource-group $RG \
    --name rt-workload04 \
    --location $LOCATION

az network route-table route create \
    --resource-group $RG \
    --route-table-name rt-workload04 \
    --name default-to-firewall \
    --address-prefix 0.0.0.0/0 \
    --next-hop-type VirtualAppliance \
    --next-hop-ip-address $FW_PRIVATE_IP

az network vnet subnet update \
    --resource-group $RG \
    --vnet-name vnet-fw-lab04 \
    --name workload \
    --route-table rt-workload04
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$LOCATION` | Azure region for regional networking resources. |
| `$FW_PRIVATE_IP` | Operator-supplied environment variable for this command. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--name` | Identifies the target Azure networking resource. |
| `--image` | Azure CLI option used to scope or shape the network operation. |
| `--size` | Azure CLI option used to scope or shape the network operation. |
| `--vnet-name` | Selects the virtual network containing the subnet or peering. |
| `--subnet` | Azure CLI option used to scope or shape the network operation. |
| `--admin-username` | Azure CLI option used to scope or shape the network operation. |
| `--generate-ssh-keys` | Azure CLI option used to scope or shape the network operation. |
| `--public-ip-address` | Azure CLI option used to scope or shape the network operation. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

This is the critical forced-tunneling pattern to validate in later steps.

#### Why this step matters

- Validate firewall policy, route table next hop, DNS behavior, and egress logs before continuing.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 4: Create allow and deny rule collections

```bash
az network firewall policy rule-collection-group create \
    --resource-group $RG \
    --policy-name fwp-lab04 \
    --name rcg-egress \
    --priority 100

az network firewall policy rule-collection-group collection add-filter-collection \
    --resource-group $RG \
    --policy-name fwp-lab04 \
    --rule-collection-group-name rcg-egress \
    --name allow-web \
    --priority 100 \
    --action Allow

az network firewall policy rule-collection-group collection rule add \
    --resource-group $RG \
    --policy-name fwp-lab04 \
    --rule-collection-group-name rcg-egress \
    --collection-name allow-web \
    --name allow-https \
    --rule-type NetworkRule \
    --ip-protocols TCP \
    --source-addresses 10.140.2.0/24 \
    --destination-addresses 20.42.0.0/16 \
    --destination-ports 443
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--policy-name` | Azure CLI option used to scope or shape the network operation. |
| `--name` | Identifies the target Azure networking resource. |
| `--priority` | Sets NSG rule evaluation order. |
| `--rule-collection-group-name` | Azure CLI option used to scope or shape the network operation. |
| `--action` | Azure CLI option used to scope or shape the network operation. |
| `--collection-name` | Azure CLI option used to scope or shape the network operation. |
| `--rule-type` | Azure CLI option used to scope or shape the network operation. |
| `--ip-protocols` | Azure CLI option used to scope or shape the network operation. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

Adjust the destination to a test target you control, or use an application-rule variant for FQDN-based allowlists.

#### Why this step matters

- Validate firewall policy, route table next hop, DNS behavior, and egress logs before continuing.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 5: Enable diagnostics and inspect evidence

```bash
az monitor diagnostic-settings create \
    --name send-fw-logs \
    --resource $(az network firewall show --resource-group $RG --name fw-lab04 --query id --output tsv) \
    --workspace $WORKSPACE_ID \
    --logs "[{"category":"AzureFirewallNetworkRule","enabled":true},{"category":"AzureFirewallApplicationRule","enabled":true}]"

az network nic show-effective-route-table \
    --resource-group $RG \
    --name $(az vm show --resource-group $RG --name vm-egress04 --query "networkProfile.networkInterfaces[0].id" --output tsv | awk -F/ '{print $NF}')
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$WORKSPACE_ID` | Operator-supplied environment variable for this command. |
| `$NF` | Operator-supplied environment variable for this command. |
| `--name` | Identifies the target Azure networking resource. |
| `--resource` | Azure CLI option used to scope or shape the network operation. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--query` | Filters output to the evidence operators need. |
| `--output` | Controls output format for review or automation. |
| `--workspace` | Azure CLI option used to scope or shape the network operation. |
| `--logs` | Azure CLI option used to scope or shape the network operation. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

The route check proves the workload really sends internet traffic to the firewall, not directly to the internet.

#### Why this step matters

- Validate firewall policy, route table next hop, DNS behavior, and egress logs before continuing.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 6: Test an allow and a deny case

```bash
az network watcher test-connectivity \
    --resource-group $RG \
    --source-resource $(az vm show --resource-group $RG --name vm-egress04 --query id --output tsv) \
    --dest-address 20.42.10.10 \
    --dest-port 443

az monitor log-analytics query \
    --workspace $WORKSPACE_ID \
    --analytics-query "AzureDiagnostics | where TimeGenerated > ago(30m) | where Category has "AzureFirewall" | project TimeGenerated, action_s, msg_s | order by TimeGenerated desc" \
    --timespan PT30M
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `$WORKSPACE_ID` | Operator-supplied environment variable for this command. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--source-resource` | Azure CLI option used to scope or shape the network operation. |
| `--name` | Identifies the target Azure networking resource. |
| `--query` | Filters output to the evidence operators need. |
| `--output` | Controls output format for review or automation. |
| `--dest-address` | Azure CLI option used to scope or shape the network operation. |
| `--dest-port` | Azure CLI option used to scope or shape the network operation. |
| `--workspace` | Azure CLI option used to scope or shape the network operation. |
| `--analytics-query` | Azure CLI option used to scope or shape the network operation. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

The goal is to see both routing evidence and firewall decision evidence in one workflow.

#### Why this step matters

- Validate firewall policy, route table next hop, DNS behavior, and egress logs before continuing.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

## Validation Steps

- [ ] The workload subnet uses a route table with `0.0.0.0/0` pointing to the firewall private IP.
- [ ] Effective routes on the workload NIC show VirtualAppliance for internet-bound traffic.
- [ ] Firewall diagnostics record allow or deny actions during your tests.
- [ ] You can explain whether a failure was caused by routing, rule logic, or the destination service.

## Cleanup Instructions

```bash
az group delete \
    --name $RG \
    --yes \
    --no-wait
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the networking resources. |
| `--name` | Identifies the target Azure networking resource. |
| `--yes` | Confirms a destructive command without prompting. |
| `--no-wait` | Starts an operation and returns before completion. |
| Expected result | Command succeeds and returns resource state, path evidence, or operation status for the change record. |

Before cleanup, record any private IPs, route table names, or diagnostic screenshots you want to reuse in troubleshooting notes.

## See Also

- [Nsg And Firewall Best Practices](../../best-practices/nsg-and-firewall-best-practices.md)
- [Routing Best Practices](../../best-practices/routing-best-practices.md)
- [Configure Udr](../../operations/configure-udr.md)
- [Connectivity Failures](../../troubleshooting/playbooks/connectivity-failures.md)

## Sources

- [overview](https://learn.microsoft.com/en-us/azure/firewall/overview)
- [deploy-cli](https://learn.microsoft.com/en-us/azure/firewall/deploy-cli)
- [firewall-diagnostics](https://learn.microsoft.com/en-us/azure/firewall/firewall-diagnostics)
