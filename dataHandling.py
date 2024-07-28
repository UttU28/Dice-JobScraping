import os, yaml
import pypyodbc as odbc
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

server = os.getenv('server')
database = os.getenv('database')
username = os.getenv('username')
password = os.getenv('password')

connectionString = f'Driver={{ODBC Driver 17 for SQL Server}};Server=tcp:{server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

def addNewJobSQL(jobID, title, location, company, description, datePosted, dateUpdated):
    try:
        conn = odbc.connect(connectionString)
        cursor = conn.cursor()
        
        sql = '''
            INSERT INTO allData (id, title, location, company, description, datePosted, dateUpdated, myStatus, decisionTime) 
            VALUES (?, ?, ?, ?, ?, ?, ?, 'pending', NULL);
        '''
        params = (jobID, title, location, company, description.encode('utf-8'), datePosted, dateUpdated)
        cursor.execute(sql, params)

        timestamp = int(datetime.now(timezone.utc).timestamp())
        sql = '''
            INSERT INTO myQueue (id, title, timeOfArrival) 
            VALUES (?, ?, ?);
        '''
        cursor.execute(sql, (jobID, title, timestamp))
        conn.commit()
        cursor.close()
        conn.close()
        return True
        # print(f"Data inserted successfully for {jobID}")
    except: 
        print("Error in Adding Data")
        return False

# Example usage
# executeAllSQL('1d2013e7-baa2-4f99-bd47-36de708e00f5', 'DevOps Databricks Engineer - Azure @ Remote', 'US', 'Aroha Technologies', 'Position:1min (Workspaces, Unity Catalog, Volumes, Ext volumes, etc.)', 1721504740, 1721504740)
