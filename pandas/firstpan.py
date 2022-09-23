"""
Zachary Pajela

My first attempt at pandas

wish me luck 


"""

import pandas as pd 

maindf = pd.read_csv("income_threshold.csv")

#this will print the first 5 records
#print(maindf.head(), "\n")

#this will print the last 5 records
#print(maindf.tail())

#this prints (num of rows, num of columns)
#print(maindf.shape)

#this prints out the columns and their data types. 
#print(maindf.dtypes)