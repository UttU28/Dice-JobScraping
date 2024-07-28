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





Create an Azure DevOps pipeline code for creating ACR in the "testPipeline" resource group having subscribtion id "dac952c9-dd98-4242-8793-26290d7a297d"
login to acr using service principal "dicePipeline"  