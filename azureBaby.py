import os
import yaml
from azure.storage.blob import ContainerClient

dirRoot = os.path.dirname(os.path.abspath(__file__))

def loadConfig():
    with open(dirRoot + "/config.yaml", "r") as yamlFile:
        return yaml.load(yamlFile, Loader=yaml.FullLoader)

config = loadConfig()
connectionString = config['connectionString']
containerName = config['containerName'] 
jobDataFile, rawDataFile = config['jobDataFile'], config['rawDataFile'] 

def uploadTheFiles():
    containerClient = ContainerClient.from_connection_string(connectionString, containerName)
    for fileName in [jobDataFile, rawDataFile]:
        blobClient = containerClient.get_blob_client(fileName)
        if blobClient.exists():
            blobClient.delete_blob()
        with open(fileName, 'rb') as data:
            blobClient.upload_blob(data)
            print(f"{fileName}, Uploaded Successfully")

def downloadTheFiles():
    containerClient = ContainerClient.from_connection_string(connectionString, containerName)
    for fileName in [jobDataFile, rawDataFile]:
        blobClient = containerClient.get_blob_client(fileName)
        with open(file=os.path.join(dirRoot, fileName + '1'), mode="wb") as sample_blob:
            download_stream = blobClient.download_blob()
            sample_blob.write(download_stream.readall())
            print(f"{fileName}, Download Successfully")

# print(config)