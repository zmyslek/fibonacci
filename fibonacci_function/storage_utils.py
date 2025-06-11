from azure.storage.blob import BlobServiceClient
import json

blob_client = BlobServiceClient.from_connection_string(
    "<YOUR_BLOB_CONNECTION_STRING>"
)

def save_to_blob(n: int, result):
    """Save Fibonacci(n) to Blob Storage."""
    blob_name = f"fibonacci/{n}.json"
    container_client = blob_client.get_container_client("results")
    container_client.upload_blob(
        name=blob_name,
        data=json.dumps({"n": n, "result": str(result)}),
        overwrite=True
    )