#Data Cleansing

# Read the CSV file into a DataFrame
import pandas as pd
df_cust = pd.read_csv('DataSources\Customer_East_Raw.txt')
# Identify missing values using isnull()
Status_missing = df_cust.isnull()
print("Columns with missing values:\n",Status_missing)
missing_values = df_cust.isnull().sum()
print("Missing values count:\n", missing_values)
# Identify non-missing values using notnull()
Status_non_missing = df_cust.notnull()
print("Columns with non missing values:\n",Status_non_missing)
non_missing_values = df_cust.notnull().sum()
print("Non-missing values:\n", non_missing_values)
#Drop columns with missing values using drop()
df_dropped_columns = df_cust.drop(columns=["Segment"], axis=1)  
print("DataFrame after dropping columns with missing values:\n", df_dropped_columns)
#Drop rows with missing values using dropna()
df_dropped_rows = df_cust.dropna()
print("DataFrame after dropping rows with missing values:\n", df_dropped_rows)
# Fill missing values in the "Segment" column with a specific value (e.g., NA for missing Segment)
df_filled_with_value = df_cust["Segment"].fillna('NA')
print("Filled with value:\n", df_filled_with_value)
# Fill missing values in the "Segment" column with the value from the previous row
df_filled_forward = df_cust["Segment"].ffil()
print("Filled forward:\n", df_filled_forward)
# Fill missing values in the "Segment" column with the value from the next row
df_filled_backward = df_cust["Segment"].bfill()
print("Filled backward:\n", df_filled_backward)
# Replace specific values in the "Segment" column
df_replaced = df_filled_backward["Segment].replace('Home Office', 'Home-Office')
print("Replaced values:\n", df_replaced)

import pandas as pd
df_order = pd.read_csv('DataSources\Orders_Details_Raw.txt', header=0, sep = ",")
# To display the data types of Profit column
print("Data types before conversion:",df_order["Profit"].dtype)
 
# Convert the "Profit" column to string data type
df_order["Profit"] = df_order["Profit"].astype(str)
print("Data types after conversion:",df_order["Profit"].dtype)
 
# Convert "Order Date" to datetime
print("Data type of Order Date before conversion:",df_order["Order Date"].dtypes)
df_order['Order Date'] = pd.to_datetime(df_order['Order Date'], format='%Y-%m-%d')
print("Data type of Order Date before conversion:",df_order["Order Date"].dtypes)
 
# Extract Year, Month and Day
df_yr = df_order["Order Date"].dt.year
df_m = df_order["Order Date"].dt.month
df_d = df_order["Order Date"].dt.day
print("Extracted Year:",df_yr)
print("Extracted Month:",df_m)
print("Extracted Day:",df_d)
 
# Convert "Quantity" to numeric
df_order["Quantity"] = df_order["Quantity"].astype(str)
print("Data type of Quantity before conversion:",df_order["Quantity"].dtypes)
df_order["Quantity"] = pd.to_numeric(df_order["Quantity"])
print("Data type of Quantity after conversion:",df_order["Quantity"].dtypes)
 
# Convert data types automatically based on their values
df1_order = df_order.convert_dtypes()
print(df1_order.dtypes)

import pandas as pd
df_Prod = pd.read_excel('DataSources\Product_Data_Raw.xlsx')
print(df_Prod)
# Identify duplicate rows
duplicate_rows = df_Prod.duplicated()
print("Duplicate rows:\n", duplicate_rows)
# Count the number of duplicate rows
num_duplicates = duplicate_rows.sum()
print("Number of duplicate rows:", num_duplicates) 
# Display only the duplicate rows
duplicate_data = df_Prod[duplicate_rows]
print("Duplicate rows:\n", duplicate_data)
# Remove duplicate rows
no_duplicates = df_Prod.drop_duplicates()
print("DataFrame without duplicates:\n", no_duplicates)
actual_rows = no_duplicates.shape[0]
print("Number of rows:", actual_rows)
# Remove leading and trailing whitespace from specified columns
df_Prod['Sub-Category'] = df_Prod['Sub-Category'].str.strip()
df_Prod['Product ID'] = df_Prod['Product ID'].str.lstrip()
df_Prod['Category'] = df_Prod['Category'].str.rstrip()
print("Without leading and trailing whitespace:",df_Prod['SubCategory'],df_Prod['Product ID'],df_Prod['Category'])

import pandas as pd
df_Cust = pd.read_json('DataSources\Customer_South_Raw.json')
print(df_Cust)
df_Upper = df_Cust['Customer ID'].str.upper()
print("Customer ID:",df_Upper)
df_Title = df_Cust['Segment'].str.title()
print("Segment:",df_Title)

import pandas as pd
# Create a DataFrame with a datetime column
data = {'Order Date': ['2023-11-25', '2022-12-20', '2021-01-15']}
df = pd.DataFrame(data)
# Convert the "Order Date" column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
# Format the dates as "Month Day, Year"
df['Formatted Date'] = df['Order Date'].dt.strftime('%B %d, %Y')
print(df)

import pandas as pd
import datetime
# Create a Timestamp representing a specific date and time
timestamp = pd.Timestamp('2023-11-25 12:34:56')
print("Time data created:",timestamp)
print(type(timestamp))
timestamp_1 = pd.Timestamp(year=2023, month=11, day=25)
timestamp_2 = datetime.datetime(2023, 11, 25)
print("Example1:",timestamp_1)
print("Example2:",timestamp_2)
#Extaction of Time components
df_h = timestamp.hour
df_m = timestamp.minute
df_s = timestamp.second
print("Extracted hour:",df_h)
print("Extracted minutes:",df_m)
print("Extracted second:",df_s)