
"""
session 6 python essentials

PANDAS

import: import pandas as pd 

DF = dataframe

myDF = pd.read_csv("path")
myDF = pd.read_excel("path")

myDF.head(n) will show the first n rows of data 

.shape method 
.dtypes method

NEXT CLEAN THE DATA 

will return a list of trues and falses:
.isnull()
put this with .sum() and you can find out if there are nulls:
myDF.isnull().sum()

this will fill in all null values with the mean of their respective numerical columns. inplace will naturally be false, but switching it to true will update your DF.
myDF.fillna(myDF.mean(), inplace=True)

myDF.dropna(inplace=True)



import pandas as pd
plasticWaste = pd.read_csv("PATH HERE")

# will display first n rows of data 
plasticWaste.head(10)

# will display number of rows and columns 
plasticWaste.shape

# will show DATA TYPES

plasticWaste.dtypes
"""