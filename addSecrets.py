import os
from time import sleep
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv

client_id = os.environ['clientID']
client_secret = os.environ['clientSecret']
tenant_id = os.environ['tenantID']
keyVaultName = os.environ["KEY_VAULT_NAME"]

keyVaultName = "thisdicekeyvault"
KVUri = f"https://{keyVaultName}.vault.azure.net"
credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
client = SecretClient(vault_url=KVUri, credential=credential)


# thisDict = {
#     'database': 'dice_sql_database',
#     'username': 'iAmRoot',
#     'password': 'Qwerty@213',
#     'connectionString': 'DefaultEndpointsProtocol=https;AccountName=dicestorage01;AccountKey=iIl/9k0FD6bMLck2NRkLLEtUTQ6p7v0UUk6v/bG5Aotxc+rmmAH5o10Pt0NArA21lZkHX7AFNFdb+ASt7i9zKA==;EndpointSuffix=core.windows.net',
#     'containerName': 'dice-data',
#     'jobDataFile': 'jobData.json',
#     'rawDataFile': 'rawData.json'
# }

def getMe(thisSecret):
    return client.get_secret(thisSecret)