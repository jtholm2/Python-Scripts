#ensure to pip install azure-storage-common, azure-storage-blob, azure-storage-queue, azure-storate-file
#For more info: https://github.com/Azure/azure-storage-python
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

blob_service_client = BlobServiceClient.from_connection_string("enter connection string to storage container here")

container_client = blob_service_client.get_container_client("pythontesting")

blobList = container_client.list_blobs()

for blob in blobList:
    print(blob['name'])
