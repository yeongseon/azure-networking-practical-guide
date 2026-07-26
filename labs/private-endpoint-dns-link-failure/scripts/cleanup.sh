#!/usr/bin/env bash

set -euo pipefail

: "${RG:?Set RG to the lab resource group name}"

az group delete \
    --name "$RG" \
    --yes \
    --no-wait
