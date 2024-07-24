from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json, os
from datetime import datetime, timezone
from tqdm import tqdm

# Custom Library Imports - Ensure these paths are correct based on your project structure
from dataScraping.jobDescription import *
from dataScraping.dataHandling import *

contentOut = ["security clearance", "security-clearance", "8+", "9+", "10+", "11+", "12+"]
contentIn = ["devops", "pipeline", "pipelines", "azure", "aws", "cloud", "cloud engineer", "cloud developer", "terraform", "ansible", "cicd", "ci-ci", "ci/cd", "kubernetes", "flask", "django", "FastAPI", "ETL"]


def scrapeTheJobs():
    def checkRequirementMatching(taroText, shouldBe, shouldNot):
        for temp1 in shouldBe:
            if temp1 in taroText:
                for temp2 in shouldNot:
                    if temp2 in taroText:
                        return False
                return True
        return False

    def writeTheJob(jobID, title, location, company):
        rawFilePath = 'rawData.json'
        rawData, jobsData = {},{}
        if os.path.exists(rawFilePath):
            with open(rawFilePath, 'r', encoding='utf-8') as jsonFile:
                rawData = json.load(jsonFile)
        else: rawData = {}

        jsonFilePath = 'jobData.json'
        if os.path.exists(jsonFilePath):
            with open(jsonFilePath, 'r', encoding='utf-8') as jsonFile:
                jobsData = json.load(jsonFile)
        else: jobsData = {}

        if jobID not in rawData:
            currentTime = int(datetime.now(timezone.utc).timestamp())
            jobsData[jobID] = currentTime
            rawData[jobID] = currentTime
            jdData = getJobDescription(jobID)
            with open(rawFilePath, 'w', encoding='utf-8') as jsonFile: json.dump(rawData, jsonFile, ensure_ascii=False, indent=4)
            if jdData:
                description, datePosted, dateUpdated = jdData
                checkRequirements = checkRequirementMatching(description, contentIn, contentOut)
                if checkRequirements:
                    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile: json.dump(jobsData, jsonFile, ensure_ascii=False, indent=4)
                    return addNewJobSQL(jobID, title, location, company, description, datePosted, dateUpdated)
        return False
            

    options = Options()
    # options.headless = True
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-dev-shm-usage")  # Disable popup blocking
    options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    options.add_argument("--disable-infobars")  
    # options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
    driver = webdriver.Chrome(options=options)

    jobKeyWords = ['DevOps', 'Azure devops', 'azure data']
    exampleElements = []
    passCount = 0

    
    for jobKeyWord in jobKeyWords:
        try:
            print(jobKeyWord.replace(' ','%20'))
            driver.get(f"https://www.dice.com/jobs?q={jobKeyWord.replace(' ','%20')}&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=100&filters.postedDate=ONE&filters.employmentType=CONTRACTS&filters.easyApply=true&language=en")
            try:
                print("Fetching Data")
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.card.search-card')))
            except Exception as e:
                print("Nai  Mila")
            sleep(1)
            pageSource = driver.page_source
            soup = BeautifulSoup(pageSource, 'html.parser')

            exampleElements.extend(soup.select('div.card.search-card'))
        except: print("Asuvidha k liye khed hai")

    driver.quit()

    for exampleElement in tqdm(exampleElements, desc="Processing Jobs"):
        try:
            if exampleElement.find('div', {'data-cy': 'card-easy-apply'}):
                jobID = exampleElement.select('a.card-title-link')[0].get('id').strip()
                location = exampleElement.select('span.search-result-location')[0].text.strip()
                title = exampleElement.select('a.card-title-link')[0].text.strip()
                company = exampleElement.select('[data-cy="search-result-company-name"]')[0].text.strip()
                if writeTheJob(jobID, title, location, company):
                    passCount += 1
        except: print("Asuvidha k liye khed hai")

    print(f"\n\n\nPASS COUNT = {passCount}")

if __name__ == "__main__":
    scrapeTheJobs()
    # schedule.every(15).minutes.do(scrapeTheJobs)

    # while True:
    #     schedule.run_pending()
    #     sleep(1)
