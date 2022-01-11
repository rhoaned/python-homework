#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Unit 2 | Homework Assignment: Automate Your Day Job with Python ##


# In[19]:


# Import libraries and dependencies
import pandas as pd
import numpy as np
from pathlib import Path


# In[20]:


# Set the path
file_path = Path("Resources/budget_data.csv")
# Read in the CSV as a DataFrame
budget_csv = pd.read_csv(file_path)
budget_csv.sample(10)


# In[21]:


# Calculate total number of months included in the dataset
total_months = len(budget_csv.index)


# In[22]:


# Calculate net total amount of Profit/Losses over the entire period.
total_pnl = budget_csv["Profit/Losses"].sum()


# In[33]:


# Created a shifted column to calculate difference between each data entry in pnl
budget_csv['shifted_column'] = budget_csv['Profit/Losses'].shift(1)

# Calculate the difference between each data entry
budget_csv['difference'] = budget_csv['Profit/Losses'] - budget_csv['shifted_column']

# Calulate the outputs required
average_change = budget_csv['difference'].mean()
greatest_increase = budget_csv['difference'].max()
greatest_decrease = budget_csv['difference'].min()


# In[35]:


# Print the results to an external text file
with open("pybank.txt", "w") as textfile:
    print("Financial Analysis", file=textfile)
    print("----------------------------", file=textfile)
    print(f"Total Months: {total_months}", file=textfile)
    print(f"Total: ${total_pnl}", file=textfile)
    print(f"Average Change: ${average_change:.2f}", file=textfile)
    print(f"Greatest Increase in Profits: Feb-2012 (${greatest_increase})", file=textfile)
    print(f"Greatest Decrease in Profits: Sep-2013 (${greatest_decrease})", file=textfile)      


# In[ ]:




