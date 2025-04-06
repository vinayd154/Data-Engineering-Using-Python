********************Loading data into Excel file********************
import pandas as pd
#Extracting data from MongoDB
from pymongo import MongoClient
conn=MongoClient("localhost")
db=conn["sample_super_store"]
coll=db['Customer_Central_Transformed']
records=coll.find({},{"_id":0})
print(records)
data=[]
for rec in records:
    data.append(rec)
df_customer_central=pd.DataFrame(data)
#Extracting data from MySQL 
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="sample_super_store")
cur = con.cursor()
cur.execute("SELECT * FROM Customer_West_Transformed")
data=[]
for row in cur:
    data.append(row)
field_names = []
for i in cur.description:
    field_names.append(i[0]) 
cur.close()
con.close()   
df_customer_west=pd.DataFrame(data,columns=field_names)
#Extracting data from text file
df_customer_east=pd.read_table(r"DataSources\TranformedData\Customer_East_Transformed.txt",sep=',')
#Extracting data from text file
df_customer_south=pd.read_json(r"DataSources\TranformedData\Customer_South_Transformed.json")
#Combining data
df_customers=pd.concat([df_customer_central,df_customer_west,df_customer_east,df_customer_south])
#Loading data to excel file with a specific sheet name
df_customers.to_excel(r"DataSources\Destination\Customer_Details.xlsx",index=False,sheet_name='customer_data')

#Loading data into json file

import pandas as pd
#Extracting data from MongoDB
from pymongo import MongoClient
conn=MongoClient("localhost")
db=conn["sample_super_store"]
coll=db['Customer_Central_Transformed']
records=coll.find({},{"_id":0})
data=[]
for rec in records:
    data.append(rec)
df_customer_central=pd.DataFrame(data)
#Extracting data from MySQL 
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="", database="sample_super_store")
cur = con.cursor()
cur.execute("SELECT * FROM Customer_West_Transformed")
data=[]
for row in cur:
    data.append(row)
cur.close()
con.close()   
df_customer_west=pd.DataFrame(data,columns=['Customer ID','Customer Name','Segment','Country','City','State','Postal Code','Region'
])
#extracting data from text file
df_customer_east=pd.read_table(r"DataSources\TranformedData\Customer_East_Transformed.txt",sep=',')
#extracting data from JSON file
df_customer_south=pd.read_json(r"DataSources\TranformedData\Customer_South_Transformed.json")
#Combining data
df_customers=pd.concat([df_customer_central,df_customer_west,df_customer_east,df_customer_south],ignore_index=True)
#Loading data to JSON file
df_customers.to_json(r"DataSources\Destination\Customer_details.json",orient='index')
