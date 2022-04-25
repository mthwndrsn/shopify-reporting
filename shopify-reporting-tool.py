import pandas as pd
import numpy as np

###
## import data
###

orders = pd.read_csv(r'C:\Users\Matt\data\shopify\orders_export_1.csv')
customers = pd.read_csv(r'C:\Users\Matt\data\shopify\customers_export_1.csv')
# import mailchimp data and join on email

###
# merge data sets
###

###
# Clean up data
###
orders['Paid at'] = pd.to_datetime(orders['Paid at'])


# setup seperate column for year
# setup seperate column for month

###
# key metric calcs
###
aov = orders['Total'].mean()
revenue = orders['Total'].sum()
# order count =
total_customers = orders['Email'].nunique()
# total repeat orders


# BLOCK
groupby_month = orders.groupby('Paid at').sum()


# Order Metrics
print(f'Average Order Value = ${aov}')
print(f'Total store revenue = ${revenue}')
print(f'Total customers = {total_customers}')

print('Grouped by Month' + str(groupby_month))
