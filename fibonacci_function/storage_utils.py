import os
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError    
from fibonacci_function.get_secret import get_secret

def save_to_blob(blob_name, data, container_name="fibonacci-results"):
    print(get_secret("StorageConnectionString"))
    connection_string = get_secret("StorageConnectionString")

    if not connection_string:
        raise ValueError("AzureWebJobsStorage connection string is missing or malformed.")
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Ensure container exists (optional, recommended)
    try:
        container_client.create_container()
    except ResourceExistsError:
        pass  # Container already exists, ignore error

    # If data is a string, convert to bytes
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Upload blob, overwrite if exists
    container_client.upload_blob(blob_name, data, overwrite=True)
