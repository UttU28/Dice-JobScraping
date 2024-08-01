#!/bin/bash
# Use the above data in the below, use RBAC to set the role as contributor for that suscription
# az ad sp create-for-rbac -n "spn-aca-azure-pipelines" --role Contributor --scope /subscriptions/e4cf2944-5342-4787-b990-418828e5555539bfc
# {
#   "appId": "6ae75f68-d956-4829-a902-1e86d195555598201",
#   "password": "vei8Q~tStpzTRKzDr2sPpAFUciprZJjWtvm55555vha_I",
#   "tenant": "8e2dc2c8-cb38-4b25-91cf-cca9277555558bd6a",
#   "displayName": "spn-aca-azure-pipelines",
# }

# az login --service-principal --username 6ae75f68-d956-4829-a902-1e86d195555598201 --password vei8Q~tStpzTRKzDr2sPpAFUciprZJjWtvm55555vha_I --tenant 8e2dc2c8-cb38-4b25-91cf-cca9277555558bd6a

# KEY VAULT
# az keyvault create --name thisdicekeyvault --resource-group thisresourcegroup
# az role assignment create --role "Key Vault Secrets User" --assignee "appIDHere" --scope "/subscriptions/subscriptionHere/resourceGroups/thisresourcegroup/providers/Microsoft.KeyVault/vaults/thisdicekeyvault"


# CREATE MANAGED IDENTITY
az identity create --resource-group thisresourcegroup --name thismyidentity
# GET THE ID
az identity show --resource-group thisresourcegroup --name thismyidentity --query id --output tsv
# SET PERMSISSION FOR THAT IDENTITY
az identity show --resource-group thisresourcegroup --name thismyidentity --query principalId --output tsv
az keyvault set-policy --name thisdicekeyvault --resource-group thisresourcegroup --object-id idFromAbove --secret-permissions get

az container show --resource-group thisresourcegroup --name thiscontainerinstancemaybe