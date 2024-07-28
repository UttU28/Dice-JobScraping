Create a Azure DevOps pipeline for building the docker file from the Dockerfile present in the repo, triggered manually, 
It should create all the resources in the "thisresourcegroup" resource group having service connection named "dicePipeline" .
acrName: "thisacr"
imageName: "dicecontainer"
version: "v1"

create resource group
Checkout hte repo
build the docker file
create ACR 
push to ACR
