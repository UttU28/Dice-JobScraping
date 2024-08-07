import os
from azure.storage.blob import ContainerClient
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Define variables
dirRoot = os.path.dirname(os.path.abspath(__file__))
blobConnectionString = os.getenv('blobConnectionString')
databaseContainer = os.getenv('databaseContainer')
jobDataFile = os.getenv('jobDataFile')
rawDataFile = os.getenv('rawDataFile')

def uploadTheFiles():
    containerClient = ContainerClient.from_connection_string(blobConnectionString, databaseContainer)
    for fileName in [jobDataFile, rawDataFile]:
        blobClient = containerClient.get_blob_client(fileName)
        if blobClient.exists():
            blobClient.delete_blob()
            logger.info(f"{fileName} deleted from blob storage.")
        try:
            with open(fileName, 'rb') as data:
                blobClient.upload_blob(data)
                logger.info(f"{fileName} uploaded successfully.")
        except Exception as e:
            logger.error(f"Failed to upload {fileName}: {e}", exc_info=True)

def downloadTheFiles():
    containerClient = ContainerClient.from_connection_string(blobConnectionString, databaseContainer)
    for fileName in [jobDataFile, rawDataFile]:
        blobClient = containerClient.get_blob_client(fileName)
        try:
            with open(os.path.join(dirRoot, fileName), "wb") as sample_blob:
                download_stream = blobClient.download_blob()
                sample_blob.write(download_stream.readall())
                logger.info(f"{fileName} downloaded successfully.")
        except Exception as e:
            logger.error(f"Failed to download {fileName}: {e}", exc_info=True)
