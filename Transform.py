#Filtering Data based on Columns

# Importing data from a JSON file
# using 'pd' as an instance/ alias for Pandas functionalities
import pandas as pd
df_customerSouth = pd.read_json('DataSources\CleansedData\Customer_South_Cleansed.json')
# filtering data based on the indicies of rows and columns
# the following expression will print for a number less than the defined range of rows (first argument) 
# and columns (second argument) specifications, i.e. first 2 rows and first 4 columns
print(df_customerSouth.iloc[1:3,1:5]);

print("The data frame has " + str(len(df_customerSouth.index)) + " rows and "
      + str(len(df_customerSouth.columns)) + " columns.");

# Select columns 'Customer ID', 'Customer Name', and 'City'
df_filtered = df_customerSouth.filter(items=['Customer ID', 'Customer Name', 'City'], axis=1)
print(df_filtered.head())


# Select columns that contain the substring 'Name'
df_filtered1 = df_customerSouth.filter(like='Name', axis=1) # 'Customer Name'
print(df_filtered1.head())


# Select columns that start with 'Cust' and end with 'ID'
df_filtered2 = df_customerSouth.filter(regex='^Cust.*ID$', axis=1) # 'Customer ID'
print(df_filtered2.head())

#Filtering Data based on Rows
# printing all customers with names terminating with the substring: 'an'
df_customer1 = df_customer[df_customer['Customer Name'].str.contains('an$')]
print(df_customer1) 


# customer names starting with 'Th' and ending with 'an'
df_customer2 = df_customer[df_customer['Customer Name'].str.match(r'^Th.*an$')];
print(df_customer2)


# Create a new column with the last 5 characters of 'Customer ID' as integers
df_customer['CustomerIDlast5'] = df_customer['Customer ID'].str.slice(-5).astype(int)
# Use the query method to filter based on this new column
df_customer4 = df_customer.query('CustomerIDlast5 > 20000')
print(df_customer4) # printing the result on the console


# printing records by the states with names starting with "Cal"
 
df_states2 = df_customer.query('State.str.slice(0, 3) == "Cal"')
print(df_states2) # the output here is congruent to an erstwhile example. 

#Calculated Fields - Apply()

# Apply with result_type='expand'
df_result = df_order[['Discount', 'Profit']].head().apply(hike, axis=1, result_type='expand')
print(df_result)

# Using result_type='broadcast'
# "lambda x:1" is a anonymous function that returns the integer value '1' for each placeholder in the range of columns' # size. 
df_result_broadcast = df_order[['Discount', 'Profit']].head().apply(lambda x: 1, axis=1, result_type='broadcast')
print("Broadcast:\n", df_result_broadcast)

#Aggregating and Summarizing Data

print(df_order.groupby('Order ID').mean(numeric_only=True));
# numeric_only = True; this parameter ensures that columns with only  # numeric values are considered; this is an explicit specification. 

# printing the minimum values for each ‘Customer ID’:
print(df_order.groupby('Customer ID')['Profit'].min());

# Let us calculate maximum profit gained from each customer
print(df_order.groupby('Customer ID').agg({'Profit':'max'}));

## application of an anonymous function
# following a sales exercise, incrementing all 'Quantity' values by 5.
print(df_order.head().groupby('Product ID').agg({'Quantity': lambda x: x + 5}));
## application of an anonymous function
# following a sales exercise, incrementing all 'Quantity' values by 5.
print(df_order.head().groupby('Product ID').agg({'Quantity': lambda x: x + 5}));