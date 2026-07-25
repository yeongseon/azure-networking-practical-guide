---
content_sources:
  diagrams:
    - id: lab-01-hub-spoke-topology
      type: flowchart
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview
      based_on:
        - https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/network-topology-and-connectivity
validation:
  az_cli:
    last_tested:
    result: not_tested
  bicep:
    last_tested:
    result: not_tested
---
# Lab 01: Hub-Spoke Topology

Build a small hub-spoke landing zone with shared services, peering, route validation, and basic connectivity testing so teams can understand how central transit works before adding private endpoints or hybrid links.

## Lab Metadata

| Field | Value |
|---|---|
| Difficulty | Intermediate |
| Estimated Duration | 60-90 minutes |
| Focus | Hub-spoke design, peering, route validation, shared services placement |
| Tooling | Azure CLI, Network Watcher, Log Analytics optional |

## Prerequisites

- An Azure subscription with permission to create VNets, subnets, network watcher resources, and virtual machines.
- Azure CLI 2.60 or later or Azure Cloud Shell.
- Quota for at least three small test VMs or alternative test endpoints.
- A region variable such as `$LOCATION=koreacentral` and a clean resource group name such as `$RG=rg-net-lab01`.

## Architecture Diagram

<!-- diagram-id: lab-01-hub-spoke-topology -->
```mermaid
flowchart TD
                Admin[Operator VM] --> Hub[Hub VNet]
                Hub --> Bastion[Bastion or Jump Subnet]
                Hub --> Shared[Shared Services
DNS and Firewall Placeholder]
                Hub --> SpokeA[Spoke A
App subnet]
                Hub --> SpokeB[Spoke B
Data subnet]
                SpokeA --> WorkloadA[VM App01]
                SpokeB --> WorkloadB[VM Data01]
```

## Step-by-Step Instructions

### Step 1: Create the resource group and core VNets

```bash
az group create \
    --name $RG \
    --location $LOCATION

az network vnet create \
    --resource-group $RG \
    --name vnet-hub-lab01 \
    --location $LOCATION \
    --address-prefixes 10.110.0.0/16 \
    --subnet-name GatewaySubnet \
    --subnet-prefixes 10.110.0.0/24

az network vnet create \
    --resource-group $RG \
    --name vnet-spoke-app-lab01 \
    --location $LOCATION \
    --address-prefixes 10.111.0.0/16 \
    --subnet-name app \
    --subnet-prefixes 10.111.1.0/24

az network vnet create \
    --resource-group $RG \
    --name vnet-spoke-data-lab01 \
    --location $LOCATION \
    --address-prefixes 10.112.0.0/16 \
    --subnet-name data \
    --subnet-prefixes 10.112.1.0/24
```

| Command | Purpose |
|---------|---------|
| `az group create` | Creates the resource group that holds all lab resources. |
| `--name $RG` | Names the resource group. |
| `--location $LOCATION` | Sets the Azure region for the group. |
| `az network vnet create` | Creates a virtual network with an initial subnet. |
| `--resource-group $RG` | Places the VNet in the lab resource group. |
| `--name vnet-hub-lab01` | Names the virtual network. |
| `--location $LOCATION` | Sets the Azure region for the VNet. |
| `--address-prefixes 10.110.0.0/16` | Sets the VNet address space. |
| `--subnet-name GatewaySubnet` | Creates an initial subnet with this name. |
| `--subnet-prefixes 10.110.0.0/24` | Sets the initial subnet's address range. |

Use non-overlapping prefixes and reserve space in the hub for future DNS, firewall, and gateway services.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 2: Add optional shared-services subnets in the hub

```bash
az network vnet subnet create \
    --resource-group $RG \
    --vnet-name vnet-hub-lab01 \
    --name shared-services \
    --address-prefixes 10.110.10.0/24

az network vnet subnet create \
    --resource-group $RG \
    --vnet-name vnet-hub-lab01 \
    --name ingress \
    --address-prefixes 10.110.20.0/24
```

| Command | Purpose |
|---------|---------|
| `az network vnet subnet create` | Adds a subnet to an existing virtual network. |
| `--resource-group $RG` | Scopes the operation to the lab resource group. |
| `--vnet-name vnet-hub-lab01` | Names the parent virtual network. |
| `--name shared-services` | Names the new subnet. |
| `--address-prefixes 10.110.10.0/24` | Sets the subnet's address range. |

These subnets are placeholders for later labs and make the topology closer to a real landing zone.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 3: Create bidirectional peerings

```bash
HUB_ID=$(az network vnet show --resource-group $RG --name vnet-hub-lab01 --query id --output tsv)
APP_ID=$(az network vnet show --resource-group $RG --name vnet-spoke-app-lab01 --query id --output tsv)
DATA_ID=$(az network vnet show --resource-group $RG --name vnet-spoke-data-lab01 --query id --output tsv)

az network vnet peering create \
    --resource-group $RG \
    --name hub-to-app \
    --vnet-name vnet-hub-lab01 \
    --remote-vnet $APP_ID \
    --allow-vnet-access true \
    --allow-forwarded-traffic true

az network vnet peering create \
    --resource-group $RG \
    --name app-to-hub \
    --vnet-name vnet-spoke-app-lab01 \
    --remote-vnet $HUB_ID \
    --allow-vnet-access true \
    --use-remote-gateways false

az network vnet peering create \
    --resource-group $RG \
    --name hub-to-data \
    --vnet-name vnet-hub-lab01 \
    --remote-vnet $DATA_ID \
    --allow-vnet-access true \
    --allow-forwarded-traffic true

az network vnet peering create \
    --resource-group $RG \
    --name data-to-hub \
    --vnet-name vnet-spoke-data-lab01 \
    --remote-vnet $HUB_ID \
    --allow-vnet-access true
```

| Command | Purpose |
|---------|---------|
| `az network vnet show` | Retrieves a virtual network's properties. |
| `--resource-group $RG` | Scopes the query to the lab resource group. |
| `--name vnet-hub-lab01` | Identifies the virtual network to read. |
| `--query id` | Extracts only the resource ID from the response. |
| `--output tsv` | Emits the value as plain text for shell capture. |
| `az network vnet peering create` | Creates a peering link between two virtual networks. |
| `--name hub-to-app` | Names the peering link. |
| `--vnet-name vnet-hub-lab01` | Sets the local VNet that owns the peering. |
| `--remote-vnet $APP_ID` | References the remote VNet by resource ID. |
| `--allow-vnet-access true` | Allows traffic between the peered VNets. |
| `--allow-forwarded-traffic true` | Allows traffic forwarded from outside the remote VNet. |
| `--use-remote-gateways false` | Does not route through the remote VNet's gateway. |

Keep notes about which side would use remote gateways in a real design. This lab uses simple peering first.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 4: Deploy small test VMs or use existing test endpoints

```bash
az vm create \
    --resource-group $RG \
    --name vm-app01 \
    --image Ubuntu2204 \
    --size Standard_B1s \
    --vnet-name vnet-spoke-app-lab01 \
    --subnet app \
    --admin-username azureuser \
    --generate-ssh-keys \
    --public-ip-address ""

az vm create \
    --resource-group $RG \
    --name vm-data01 \
    --image Ubuntu2204 \
    --size Standard_B1s \
    --vnet-name vnet-spoke-data-lab01 \
    --subnet data \
    --admin-username azureuser \
    --generate-ssh-keys \
    --public-ip-address ""
```

| Command | Purpose |
|---------|---------|
| `az vm create` | Creates a virtual machine in the specified subnet. |
| `--resource-group $RG` | Places the VM in the lab resource group. |
| `--name vm-app01` | Names the virtual machine. |
| `--image Ubuntu2204` | Sets the OS image. |
| `--size Standard_B1s` | Selects a small burstable VM size. |
| `--vnet-name vnet-spoke-app-lab01` | Attaches the VM to this virtual network. |
| `--subnet app` | Places the VM's NIC in this subnet. |
| `--admin-username azureuser` | Sets the administrator account name. |
| `--generate-ssh-keys` | Generates SSH key pair for authentication. |
| `--public-ip-address ""` | Creates the VM without a public IP (private only). |

Private-only VMs make validation closer to a production pattern.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 5: Inspect effective routes and verify cross-spoke reachability

```bash
APP_NIC=$(az vm show --resource-group $RG --name vm-app01 --query "networkProfile.networkInterfaces[0].id" --output tsv | awk -F/ '{print $NF}')
az network nic show-effective-route-table \
    --resource-group $RG \
    --name $APP_NIC

az network watcher test-connectivity \
    --resource-group $RG \
    --source-resource $(az vm show --resource-group $RG --name vm-app01 --query id --output tsv) \
    --dest-address 10.112.1.4 \
    --dest-port 22
```

| Command | Purpose |
|---------|---------|
| `az vm show` | Retrieves a virtual machine's properties. |
| `--resource-group $RG` | Scopes the query to the lab resource group. |
| `--name vm-app01` | Identifies the VM to read. |
| `--query "networkProfile.networkInterfaces[0].id"` | Extracts the primary NIC resource ID. |
| `--query id` | Extracts only the VM resource ID. |
| `--output tsv` | Emits the value as plain text for shell capture. |
| `az network nic show-effective-route-table` | Shows the effective routes applied to a NIC. |
| `--name $APP_NIC` | Identifies the network interface to inspect. |
| `az network watcher test-connectivity` | Tests reachability between a source and destination. |
| `--source-resource ...` | Sets the source resource (the app VM) for the test. |
| `--dest-address 10.112.1.4` | Sets the destination IP address. |
| `--dest-port 22` | Sets the destination TCP port to probe. |

The goal is to prove that peering plus correct routes equals a reachable path. If not, this becomes a troubleshooting baseline for later labs.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

### Step 6: Introduce a route-table experiment

```bash
az network route-table create \
    --resource-group $RG \
    --name rt-app-lab01 \
    --location $LOCATION

az network route-table route create \
    --resource-group $RG \
    --route-table-name rt-app-lab01 \
    --name route-to-data \
    --address-prefix 10.112.0.0/16 \
    --next-hop-type VnetLocal

az network vnet subnet update \
    --resource-group $RG \
    --vnet-name vnet-spoke-app-lab01 \
    --name app \
    --route-table rt-app-lab01
```

| Command | Purpose |
|---------|---------|
| `az network route-table create` | Creates a user-defined route table. |
| `--resource-group $RG` | Places the route table in the lab resource group. |
| `--name rt-app-lab01` | Names the route table. |
| `--location $LOCATION` | Sets the Azure region. |
| `az network route-table route create` | Adds a route to an existing route table. |
| `--route-table-name rt-app-lab01` | Identifies the parent route table. |
| `--name route-to-data` | Names the route. |
| `--address-prefix 10.112.0.0/16` | Sets the destination prefix the route matches. |
| `--next-hop-type VnetLocal` | Routes matching traffic within the virtual network. |
| `az network vnet subnet update` | Modifies an existing subnet. |
| `--vnet-name vnet-spoke-app-lab01` | Names the parent virtual network. |
| `--name app` | Identifies the subnet to update. |
| `--route-table rt-app-lab01` | Associates the route table with the subnet. |

Although the route is not strictly needed here, the exercise teaches how to validate effective routes and prepares you for a forced-tunneling variant.

#### Why this step matters

- It establishes an observable checkpoint for the lab before you continue.
- It mirrors a real production activity that often appears in troubleshooting tickets.
- Save command output and timestamps so you can compare expected versus actual behavior later.

## Validation Steps

- [ ] All four peering objects show `Connected` state.
- [ ] Effective routes on the app NIC include the data spoke prefix.
- [ ] Connection tests from app to data succeed on the tested port.
- [ ] Diagrams and resource names are updated in your notes before teardown.

## Cleanup Instructions

```bash
az group delete --name $RG --yes --no-wait
```

| Command | Purpose |
|---------|---------|
| `az group delete` | Deletes the resource group and all lab resources. |
| `--name $RG` | Identifies the resource group to delete. |
| `--yes` | Skips the interactive confirmation prompt. |
| `--no-wait` | Returns immediately without waiting for completion. |

Before cleanup, record any private IPs, route table names, or diagnostic screenshots you want to reuse in troubleshooting notes.

## See Also

- [Network Design Baseline](../../best-practices/network-design-baseline.md)
- [Subnet Design Best Practices](../../best-practices/subnet-design-best-practices.md)
- [Peering Basics](../../operations/peering-basics.md)
- [Connectivity Failures](../../troubleshooting/playbooks/connectivity-failures.md)

## Sources

- [virtual-network-peering-overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview)
- [network-topology-and-connectivity](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/network-topology-and-connectivity)
