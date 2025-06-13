import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Your Key Vault URL
KEY_VAULT_URL = "https://fibonaccikeyvaultt.vault.azure.net/"

# Name of the secret you stored
SECRET_NAME = "StorageConnectionString"

def get_secret(secret_name):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
    retrieved_secret = client.get_secret(secret_name)
    return retrieved_secret.value

# Authenticate using DefaultAzureCredential
# This works with Azure CLI login, managed identity, VS Code, etc.
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)

# Retrieve the secret
retrieved_secret = client.get_secret(SECRET_NAME)
connection_string = retrieved_secret.value

print("Connection string from Key Vault:", connection_string)
