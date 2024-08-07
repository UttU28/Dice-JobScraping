import os, yaml
import pypyodbc as odbc
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

databaseServer = os.getenv('databaseServer')
databaseName = os.getenv('databaseName')
databaseUsername = os.getenv('databaseUsername')
databasePassword = os.getenv('databasePassword')
print(databaseServer, databaseName, databaseUsername)


connectionString = f'Driver={{ODBC Driver 17 for SQL Server}};Server=tcp:{databaseServer},1433;Database={databaseName};Uid={databaseUsername};Pwd={databasePassword};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

def addNewJobSQL(jobID, title, location, company, description, dateUpdated):
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
        return True
        # print(f"Data inserted successfully for {jobID}")
    except: 
        print("Error in Adding Data")
        return False

# Example usage
# executeAllSQL('1d2013e7-baa2-4f99-bd47-36de708e00f5', 'DevOps Databricks Engineer - Azure @ Remote', 'US', 'Aroha Technologies', 'Position:1min (Workspaces, Unity Catalog, Volumes, Ext volumes, etc.)', 1721504740, 1721504740)
