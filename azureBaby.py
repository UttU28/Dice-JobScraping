import os
from azure.storage.blob import ContainerClient
from dotenv import load_dotenv
load_dotenv()

dirRoot = os.path.dirname(os.path.abspath(__file__))

blobConnectionString = os.getenv('blobConnectionString')
databaseContainer = os.getenv('databaseContainer')

jobDataFile, rawDataFile = os.getenv('jobDataFile'), os.getenv('rawDataFile') 

def uploadTheFiles():
    containerClient = ContainerClient.from_connection_string(blobConnectionString, databaseContainer)
    for fileName in [jobDataFile, rawDataFile]:
        blobClient = containerClient.get_blob_client(fileName)
        if blobClient.exists():
            blobClient.delete_blob()
        with open(fileName, 'rb') as data:
            blobClient.upload_blob(data)
            print(f"{fileName}, Uploaded Successfully")

def downloadTheFiles():
    containerClient = ContainerClient.from_connection_string(blobConnectionString, databaseContainer)
    for fileName in [jobDataFile, rawDataFile]:
        blobClient = containerClient.get_blob_client(fileName)
        with open(file=os.path.join(dirRoot, fileName), mode="wb") as sample_blob:
            download_stream = blobClient.download_blob()
            sample_blob.write(download_stream.readall())
            print(f"{fileName}, Download Successfully")

# print(config)