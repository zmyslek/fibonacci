# Configuration
$FunctionAppName = "fibonaccii"
$ResourceGroup = "fibonacci"
$Location = "North Europe"
$StorageAccountName = "fibonaccistore$(Get-Random -Minimum 1000 -Maximum 9999)"

# Deploy Function
func azure functionapp publish $FunctionAppName --python

# Create Storage Account (if not exists)
az storage account create `
  --name $StorageAccountName `
  --resource-group $ResourceGroup `
  --location $Location `
  --sku Standard_LRS

# Create container for results
az storage container create `
  --name "results" `
  --account-name $StorageAccountName