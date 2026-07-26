#!/usr/bin/env bash

set -euo pipefail

: "${RG:?Set RG to the lab resource group name}"
: "${LOCATION:?Set LOCATION to an Azure region, for example eastus2}"
: "${STORAGE_ACCOUNT_NAME:?Set STORAGE_ACCOUNT_NAME to a globally unique storage account name}"
: "${ADMIN_PASSWORD:?Set ADMIN_PASSWORD to a secure VM password}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

az group create \
    --name "$RG" \
    --location "$LOCATION"

az deployment group create \
    --resource-group "$RG" \
    --template-file "$LAB_DIR/main.bicep" \
    --parameters @"$LAB_DIR/main.parameters.json" \
    --parameters storageAccountName="$STORAGE_ACCOUNT_NAME" adminPassword="$ADMIN_PASSWORD"

az network private-dns link vnet delete \
    --resource-group "$RG" \
    --zone-name privatelink.blob.core.windows.net \
    --name link-vnet-lab02 \
    --yes

az vm run-command invoke \
    --resource-group "$RG" \
    --name vm-client02 \
    --command-id RunShellScript \
    --scripts "nslookup $STORAGE_ACCOUNT_NAME.blob.core.windows.net"

az network private-dns link vnet create \
    --resource-group "$RG" \
    --zone-name privatelink.blob.core.windows.net \
    --name link-vnet-lab02 \
    --virtual-network vnet-lab02 \
    --registration-enabled false

SOURCE_VM_ID="$(az vm show --resource-group "$RG" --name vm-client02 --query id --output tsv)"

az network watcher test-connectivity \
    --resource-group "$RG" \
    --source-resource "$SOURCE_VM_ID" \
    --dest-address "$STORAGE_ACCOUNT_NAME.blob.core.windows.net" \
    --dest-port 443
