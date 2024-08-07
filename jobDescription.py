import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timezone
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def bhaiTimeKyaHai(watch):
    try:
        watch = datetime.strptime(watch, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        timeHai = int(watch.timestamp())
        return timeHai
    except Exception as e:
        logger.error(f"Error converting time: {watch}", exc_info=e)
        return None

def getJobDescription(jobID):
    url = f"https://www.dice.com/job-detail/{jobID}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Failed to retrieve the webpage. URL: {url}, Error: {e}", exc_info=e)
        return False

    try:
        htmlContent = response.text
        soup = BeautifulSoup(htmlContent, 'html.parser')
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
    except Exception as e:
        logger.error(f"Error processing job description for jobID: {jobID}", exc_info=e)
        return False
