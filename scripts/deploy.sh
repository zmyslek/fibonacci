#!/bin/bash
# Replace placeholders with YOUR values
FUNCTION_APP_NAME="fibonacci-function"  # Must be globally unique
STORAGE_ACCOUNT_NAME="fibonaccistorage$(date +%s)"  # Random suffix
REDIS_NAME="fibonacci-cache"

# Deploy Azure Function
func azure functionapp publish $FUNCTION_APP_NAME --python

# Create Blob Storage
az storage account create \
  --name $STORAGE_ACCOUNT_NAME \
  --resource-group fibonacci \
  --location "North Europe" \
  --sku Standard_LRS

az storage container create \
  --name "results" \
  --account-name $STORAGE_ACCOUNT_NAME

# Create Redis Cache (if needed)
az redis create \
  --name $REDIS_NAME \
  --resource-group fibonacci \
  --location "North Europe" \
  --sku Basic \
  --vm-size C1