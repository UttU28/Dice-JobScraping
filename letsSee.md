I have a Data Scraping project that uses Selenium and BS4 to scrape the data and upload it to SQL using ODBC Driver in Lunix environment running on Python 3.8.3. 
I made a container for it using DOcker and installed all the prereq and when I run It locally, it starts scraping the data , uploads it and quits. Works perfectly.


Now I want the container to be run every 20 minutes using Azure Services. How can I achieve what I want in Azure Cloud. thanks

Ill provide some information here, give me commands with the values here thanks

RG Name: thisTestRG
RegName: thisTestRegistry


az acr login --name thisTestRegistry