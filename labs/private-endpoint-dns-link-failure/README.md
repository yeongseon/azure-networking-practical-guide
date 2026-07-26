# Private endpoint DNS link failure lab substrate

This lab substrate supports the future live-Azure experiment for ZLR-networking-02. It creates the file layout, deployment template, and operator runbook needed to reproduce a missing private DNS zone link without fabricating any evidence.

## Status

- Authoring only: no deployment, fault injection, or evidence capture has been executed in this change.
- `evidence/` contains placeholders only.
- `docs/assets/troubleshooting/private-endpoint-dns-link-failure/` contains placeholders only.

## Topology summary

- Client VM: `vm-client02`
- Private DNS zone: `privatelink.blob.core.windows.net`
- Virtual network link: `link-vnet-lab02`
- Fault injection: delete `link-vnet-lab02` from `privatelink.blob.core.windows.net`, confirm broken name resolution from `vm-client02`, then recreate the link and validate recovery.

## Directory contents

- `main.bicep` — deploys the lab substrate into an existing resource group.
- `main.parameters.json` — placeholder parameters for a future live deployment.
- `scripts/reproduce.sh` — deploy, inject the DNS-link failure, and validate recovery.
- `scripts/cleanup.sh` — delete the lab resource group.
- `evidence/README.md` — placeholder describing what to capture later.

## Prerequisites

- Azure CLI authenticated to the target subscription.
- Permission to create resource groups, virtual networks, private endpoints, private DNS zones, and virtual machines.
- A unique storage account name for the deployment parameters.
- A secure password value supplied at runtime for the lab VM.

## 1) Create the resource group and deploy the substrate

Update `main.parameters.json` before running the deployment, or override `storageAccountName` and `adminPassword` on the command line.

```bash
az group create \
    --name $RG \
    --location $LOCATION

az deployment group create \
    --resource-group $RG \
    --template-file labs/private-endpoint-dns-link-failure/main.bicep \
    --parameters @labs/private-endpoint-dns-link-failure/main.parameters.json \
    --parameters storageAccountName=$STORAGE_ACCOUNT_NAME adminPassword=$ADMIN_PASSWORD
```

| Command | Purpose |
| --- | --- |
| `az group create` | Create the resource group that will hold the lab assets. |
| `--name $RG` | Sets the lab resource group name. |
| `--location $LOCATION` | Sets the Azure region for the resource group. |
| `az deployment group create` | Deploy the Bicep substrate into the resource group. |
| `--resource-group $RG` | Targets the existing lab resource group. |
| `--template-file labs/private-endpoint-dns-link-failure/main.bicep` | Points to the substrate template. |
| `--parameters @labs/private-endpoint-dns-link-failure/main.parameters.json` | Loads the baseline parameter file. |
| `--parameters storageAccountName=$STORAGE_ACCOUNT_NAME adminPassword=$ADMIN_PASSWORD` | Overrides the placeholder storage account name and secure VM password. |

Expected live result later: a VNet, a `blob` private endpoint, the `privatelink.blob.core.windows.net` zone, the `link-vnet-lab02` VNet link, and the client VM `vm-client02`.

## 2) Confirm the healthy baseline before fault injection

```bash
az network private-dns link vnet show \
    --resource-group $RG \
    --zone-name privatelink.blob.core.windows.net \
    --name link-vnet-lab02

az vm run-command invoke \
    --resource-group $RG \
    --name vm-client02 \
    --command-id RunShellScript \
    --scripts "nslookup $STORAGE_ACCOUNT_NAME.blob.core.windows.net"
```

| Command | Purpose |
| --- | --- |
| `az network private-dns link vnet show` | Read the current private DNS VNet link state before injecting the fault. |
| `--resource-group $RG` | Scopes the lookup to the lab resource group. |
| `--zone-name privatelink.blob.core.windows.net` | Selects the blob private-link DNS zone. |
| `--name link-vnet-lab02` | Selects the VNet link that will later be deleted. |
| `az vm run-command invoke` | Runs a command inside `vm-client02` without requiring a public IP. |
| `--name vm-client02` | Selects the client VM that consumes the private endpoint. |
| `--command-id RunShellScript` | Uses the Linux shell run-command channel. |
| `--scripts "nslookup $STORAGE_ACCOUNT_NAME.blob.core.windows.net"` | Runs `nslookup` from the client VM to establish the healthy baseline. |

Capture the real output under `evidence/` during the live run. Do not invent or pre-populate any lookup output in this scaffold.

## 3) Inject the DNS-link failure

Delete the virtual network link `link-vnet-lab02` from the private DNS zone `privatelink.blob.core.windows.net`.

```bash
az network private-dns link vnet delete \
    --resource-group $RG \
    --zone-name privatelink.blob.core.windows.net \
    --name link-vnet-lab02 \
    --yes
```

| Command | Purpose |
| --- | --- |
| `az network private-dns link vnet delete` | Removes the VNet link to reproduce the DNS-link failure. |
| `--resource-group $RG` | Scopes the deletion to the lab resource group. |
| `--zone-name privatelink.blob.core.windows.net` | Identifies the private DNS zone that owns the link. |
| `--name link-vnet-lab02` | Identifies the link being deleted for the fault injection. |
| `--yes` | Suppresses the interactive delete confirmation. |

## 4) Observe the broken resolution from `vm-client02`

```bash
az vm run-command invoke \
    --resource-group $RG \
    --name vm-client02 \
    --command-id RunShellScript \
    --scripts "nslookup $STORAGE_ACCOUNT_NAME.blob.core.windows.net"
```

| Command | Purpose |
| --- | --- |
| `az vm run-command invoke` | Runs the post-fault DNS lookup inside the client VM. |
| `--resource-group $RG` | Scopes the run-command call to the lab resource group. |
| `--name vm-client02` | Selects the VM that should now show broken name resolution. |
| `--command-id RunShellScript` | Uses the shell run-command channel. |
| `--scripts "nslookup $STORAGE_ACCOUNT_NAME.blob.core.windows.net"` | Re-runs the storage FQDN lookup after deleting the zone link. |

During the live run, save the actual failed `nslookup` evidence under `evidence/` and later capture the matching Portal artifacts under `docs/assets/troubleshooting/private-endpoint-dns-link-failure/`.

## 5) Recreate the link and validate recovery

```bash
az network private-dns link vnet create \
    --resource-group $RG \
    --zone-name privatelink.blob.core.windows.net \
    --name link-vnet-lab02 \
    --virtual-network vnet-lab02 \
    --registration-enabled false

az network watcher test-connectivity \
    --resource-group $RG \
    --source-resource $(az vm show --resource-group $RG --name vm-client02 --query id --output tsv) \
    --dest-address $STORAGE_ACCOUNT_NAME.blob.core.windows.net \
    --dest-port 443
```

| Command | Purpose |
| --- | --- |
| `az network private-dns link vnet create` | Recreates the deleted VNet link so private resolution can recover. |
| `--resource-group $RG` | Scopes the create operation to the lab resource group. |
| `--zone-name privatelink.blob.core.windows.net` | Selects the DNS zone to relink. |
| `--name link-vnet-lab02` | Reuses the original VNet-link name during recovery. |
| `--virtual-network vnet-lab02` | Reattaches the client VNet to the private DNS zone. |
| `--registration-enabled false` | Keeps autoregistration disabled for the service zone link. |
| `az network watcher test-connectivity` | Validates end-to-end recovery from `vm-client02` to the storage FQDN. |
| `az vm show` | Retrieves the resource ID for `vm-client02` so the connectivity test can use the VM as its source. |
| `--source-resource $(az vm show --resource-group $RG --name vm-client02 --query id --output tsv)` | Supplies the client VM resource ID as the source for connectivity testing. |
| `--query id` | Extracts only the VM resource ID from the `az vm show` result. |
| `--output tsv` | Emits the VM resource ID as plain text for command substitution. |
| `--dest-address $STORAGE_ACCOUNT_NAME.blob.core.windows.net` | Targets the storage blob endpoint FQDN. |
| `--dest-port 443` | Verifies HTTPS reachability after DNS recovery. |

Follow the connectivity test with another `nslookup` from `vm-client02` and capture the real restored output during the live run.

## 6) Cleanup

```bash
az group delete \
    --name $RG \
    --yes \
    --no-wait
```

| Command | Purpose |
| --- | --- |
| `az group delete` | Deletes the entire lab resource group after validation. |
| `--name $RG` | Selects the lab resource group to remove. |
| `--yes` | Suppresses the interactive delete confirmation. |
| `--no-wait` | Returns immediately while Azure continues the deletion asynchronously. |

## Deferred until live Azure execution

- Deploy the substrate into a disposable resource group.
- Capture the healthy `nslookup` from `vm-client02`.
- Delete `link-vnet-lab02` from `privatelink.blob.core.windows.net`.
- Capture the failed `nslookup` from `vm-client02`.
- Recreate the link and capture `az network watcher test-connectivity` plus the recovered `nslookup`.
- Save CLI evidence in `evidence/` and Portal screenshots in `docs/assets/troubleshooting/private-endpoint-dns-link-failure/`.
