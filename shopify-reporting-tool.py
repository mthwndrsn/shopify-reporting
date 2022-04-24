import pandas as pd
import numpy as np


orders = pd.read_csv(r'C:\Users\Matt\data\shopify\orders_export_1.csv')
customers = pd.read_csv(r'C:\Users\Matt\data\shopify\customers_export_1.csv')
# import mailchimp data and join on email


# key metric calcs
aov = orders['Total'].mean()
revenue = orders['Total'].sum()
# order count =
total_customers = orders['Email'].nunique()
# total repeat orders


# BLOCK
groupby_month = orders.groupby('Paid at').sum()


# Order Metrics
print('Average Order Value = $' + str(aov))
print('Total store revenue = $' + str(revenue))
print('Total customers = ' + str(total_customers))

print('Grouped by Month' + str(groupby_month))
