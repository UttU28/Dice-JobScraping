# Dice-JobScraping

docker build -t thisName .
docker run thisName

docker build -t utsavmaan28/diceDataScraping:v1 .
docker build -t utsavmaan28/diceDataScraping:v1 .
docker tag utsavmaan28/diceDataScraping:v1 utsavmaan28/diceDataScraping:v1-release
docker push utsavmaan28/diceDataScraping:v1-release



1. Create Pipeline
2. Create Service Principal using
```az ad sp create-for-rbac -n "spn-aca-azure-pipelines" --role Contributor --scope /subscriptions/subID```
3. Add it to the Pipeline Service Connection
4. Create Key Vault, add access for the "spn-aca-azure-pipelines" to the keyvault
5. Add all the secrets and value to the keyvault
6. Create BLOB for rawData and jobData