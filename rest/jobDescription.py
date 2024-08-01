import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timezone

def bhaiTimeKyaHai(watch):
    watch = datetime.strptime(watch, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
    timeHai = int(watch.timestamp())
    return timeHai

def getJobDescription(jobID):
    url = f"https://www.dice.com/job-detail/{jobID}"
    response = requests.get(url)

    if response.status_code == 200:
        htmlContent = response.text
    else:
        print(f"Failed to retrieve the webpage. For: {url}, Status code: {response.status_code}")
        return False

    soup = BeautifulSoup(htmlContent, 'html.parser')
    # print(soup)
    scriptTag = soup.select('script#__NEXT_DATA__')[0].text
    data = json.loads(scriptTag)
    thisData = data["props"]["pageProps"]["initialState"]["api"]["queries"][f'getJobById("{jobID}")']["data"]

    jobDescription = thisData["description"]
    datePosted = bhaiTimeKyaHai(thisData["datePosted"])
    dateUpdated = bhaiTimeKyaHai(thisData["dateUpdated"])
    jobDescription = BeautifulSoup(jobDescription, 'html.parser').prettify()
    jobDescription = BeautifulSoup(jobDescription, 'html.parser').get_text().split("\n")
    jobDescription = " \n".join([element.strip() for element in jobDescription if element != ''])
    return jobDescription, datePosted, dateUpdated
