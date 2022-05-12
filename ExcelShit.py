import pandas as pd
from datetime import *
import numpy as np


my = pd.read_excel('sampledatafoodsales.xlsx', sheet_name="FoodSales")
#print all the Chocolate Chips that order in April
result = my[(my['OrderDate'].dt.month == 4) & (my['Product'] == 'Chocolate Chip')]

#print all the Potato Chips that have TotalPrice > 100
result = my[(my['Product'] == 'Potato Chips') & (my['TotalPrice'] > 100.0)]

#print all the Carrots from New York or Los Angeles that have totalprice >10
result = my[(my['Product'] == 'Carrot') & ((my['City'] == 'New York') | (my['City'] == 'Los Angeles')) & (my['TotalPrice'] >50)]
#sort the Product alphabetically
result.sort_values(by = 'City', inplace = True, ascending = True)

#add new column
my['TestComfirmed'] = ['Comfirmed' if i >50 else 'Uncomfirmed' for i in my.Quantity]

print(my)
