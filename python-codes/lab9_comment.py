#This code analyzes customer data by filtering for attributes like marital status, 
#income, and age, and calculates the average income for younger customers.

# Importing necessary libraries
import pandas as pd
import numpy as np

# Loading the data from an Excel file
df = pd.read_excel('marketing_campaign.xlsx')

# Displaying marital status of all customers
print('Marital status of all customers')
print(df['marital_status'])

# Displaying the 3rd and 5th columns for rows indexed from 30 to 50
print('\n3rd and 5th column from row indices 30-50:')
print(df.iloc[30:51, [2, 4]])

# Displaying Registration Date and Income columns for all customers
print('\nRegistration Date and Income:')
print(df.loc[:, ['reg_date', 'income']])

# Filtering and displaying customers with marital status "YOLO"
print('\nCustomers with Marital Status YOLO:')
print(df[df['marital_status'] == 'YOLO'])

# Finding and displaying the oldest customers based on birth year
print('\nOldest Customers:')
print(df[df['birth_year'] == np.min(df['birth_year'])])

# Filtering and displaying customers with a PhD or Master’s degree
print('\nPHD or Master Customers:')
print(df[(df.education == 'PhD') | (df.education == 'Master')])

# Filtering and displaying customers with income over 100,000 and fewer than 10 store purchases
print('\nRecords for customers whose income is over 100000 with fewer than 10 store purchases:')
print(df[(df.income > 100000) & (df.store_purchases < 10)])

# Filtering and displaying single or divorced customers born before 1980
print('\nSingle or divorced customers with birth_year before 1980:')
print(df[((df.marital_status == 'Single') | (df.marital_status == 'Divorced')) & (df.birth_year < 1980)])

# Setting the customer ID as the index for easier data retrieval by ID
df.set_index(['id'], inplace=True)

# Displaying income, birth year, and store purchases for customers with IDs 22 and 11178
print('\nIncome, birth year, and store purchases for Customers 22 and 11178:')
print(df.loc[[22, 11178], ['income', 'birth_year', 'store_purchases']])

# Calculating the average income for customers born after the average birth year
r = np.mean(df.income[df.birth_year > np.mean(df['birth_year'])])
print('\nAverage Income of Customers who are younger than the average:', round(r, 1))

