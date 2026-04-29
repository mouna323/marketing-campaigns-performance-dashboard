#import libraries
import pandas as pd
import snowflake.connector

#show the table date to create same in snowflake
df=pd.read_csv('C:\\Users\\Mounaipconfig\\Desktop\\new_job\\snowflake_Sql\\marketing_campaign_dataset.csv')
print(df.info())
print(df.columns)

# Connect to Snowflake /conn = connection to Snowflake database
conn=snowflake.connector.connect(
    user='MOUNA92',
    password='Dbtraining@2026',
    account='ZAJUNLK-KZ51773',
    warehouse='COMPUTE_WH',
    database='MARKETING_DB;',
    schema='MARKETING'
)
#test connection
print("Connected to Snowflake")


#create cursor /object used to send  SQL commands to snowflake and  executeit and fetch(return) results from the database
cursor=conn.cursor()

# Upload file(with put)
cursor.execute("""
PUT file://C:/Users/Mounaipconfig/Desktop/new_job/snowflake_Sql/marketing_campaign_dataset.csv
@MARKETING_DB.MARKETING.LOAD_FILE
""")

# Load data(copy data to created table with snowflake)
cursor.execute("USE DATABASE MARKETING_DB")
cursor.execute("USE SCHEMA MARKETING")
cursor.execute("""
COPY INTO MARKETING_DB.MARKETING.MARKETING_CAMPAIGN
FROM @MARKETING_DB.MARKETING.LOAD_FILE/marketing_campaign_dataset.csv
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER=1 FIELD_OPTIONALLY_ENCLOSED_BY='"')
""")

print("Data loaded successfully!")

cursor.execute("""
PUT file://C:/Users/Mounaipconfig/Desktop/new_job/snowflake_sql/marketing_campaign_dataset.csv
@MARKETING_DB.MARKETING.LOAD_FILE
AUTO_COMPRESS=TRUE
""")