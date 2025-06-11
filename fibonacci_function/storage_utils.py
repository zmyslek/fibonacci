import os
from azure.storage.blob import BlobServiceClient

def save_to_blob(blob_name, data, container_name="fibonacci-results"):
    connection_string = os.getenv("AzureWebJobsStorage")
    if not connection_string:
        raise ValueError("AzureWebJobsStorage connection string is missing or malformed.")
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Ensure container exists (optional, but recommended)
    try:
        container_client.create_container()
    except Exception:
        # Container may already exist, ignore error
        pass

    # Upload blob, overwrite if exists
    container_client.upload_blob(blob_name, data, overwrite=True)
