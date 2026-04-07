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

```mermaid
flowchart LR
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

This layout mirrors the minimum production pattern of firewall plus workload subnet.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
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

Wait for provisioning to finish before moving on. Firewall deployment can take several minutes.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
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

This is the critical forced-tunneling pattern to validate in later steps.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
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

Adjust the destination to a test target you control, or use an application-rule variant for FQDN-based allowlists.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
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

The route check proves the workload really sends internet traffic to the firewall, not directly to the internet.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
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

The goal is to see both routing evidence and firewall decision evidence in one workflow.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

## Validation Steps

- [ ] The workload subnet uses a route table with `0.0.0.0/0` pointing to the firewall private IP.
- [ ] Effective routes on the workload NIC show VirtualAppliance for internet-bound traffic.
- [ ] Firewall diagnostics record allow or deny actions during your tests.
- [ ] You can explain whether a failure was caused by routing, rule logic, or the destination service.

## Cleanup Instructions

```bash
az group delete --name $RG --yes --no-wait
```

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
