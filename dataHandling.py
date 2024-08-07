import os
import pypyodbc as odbc
from datetime import datetime, timezone
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Database configuration
databaseServer = os.getenv('databaseServer')
databaseName = os.getenv('databaseName')
databaseUsername = os.getenv('databaseUsername')
databasePassword = os.getenv('databasePassword')

connectionString = f'Driver={{ODBC Driver 17 for SQL Server}};Server=tcp:{databaseServer},1433;Database={databaseName};Uid={databaseUsername};Pwd={databasePassword};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

def addNewJobSQL(jobID, title, location, company, description, datePosted, dateUpdated):
    try:
        conn = odbc.connect(connectionString)
        cursor = conn.cursor()
        
        sql = '''
            INSERT INTO allData (id, title, location, company, description, dateUpdated) 
            VALUES (?, ?, ?, ?, ?, ?);
        '''
        params = (jobID, title, location, company, description.encode('utf-8'), dateUpdated)
        cursor.execute(sql, params)

        conn.commit()
        cursor.close()
        conn.close()
        logger.info(f"Data inserted successfully for jobID: {jobID}")
        return True
    except Exception as e:
        logger.error(f"Error in adding data for jobID: {jobID}", exc_info=e)
        return False