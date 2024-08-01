import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import ContainerClient
from dotenv import load_dotenv
load_dotenv()

dirRoot = os.path.dirname(os.path.abspath(__file__))

databaseServer = os.getenv('databaseServer')
databaseName = os.getenv('databaseName')
databaseUsername = os.getenv('databaseUsername')
databasePassword = os.getenv('databasePassword')
print(databaseServer, databaseName, databaseUsername, databasePassword)
databaseServer = 'dice-sql.database.windows.net'
databaseName = 'dice_sql_database'
databaseUsername = 'iAmRoot'
databasePassword = 'Qwerty@213'

blobConnectionString = "DefaultEndpointsProtocol=https;AccountName=dicestorage02;AccountKey=0vcVtp1m+lDHV8cfEA622y+IxcQimHDnfTyC+m1S9y4KicQuVd2ogHCwrAborZgYPQRWvG8C557G+AStHHrT9g==;EndpointSuffix=core.windows.net"
databaseContainer = 'dice-data'

# connectionString = f'Driver={{ODBC Driver 17 for SQL Server}};Server=tcp:{databaseServer},1433;Database={databaseName};Uid={databaseUsername};Pwd={databasePassword};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
jobDataFile, rawDataFile = os.getenv('jobDataFile'), os.getenv('rawDataFile') 
print(jobDataFile, rawDataFile)

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