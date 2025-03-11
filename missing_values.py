#find the missing values in data sets and change name missing values

import pandas as pd

#na_values: parameter used to covert  missing values as a  "NaN"
print(pd.read_csv("suraj.csv",na_values={'not available','no values'})) 

#keep_default_na=False: it is used for default values as it before
print(pd.read_csv("suraj.csv",keep_default_na=False))

#keep_default_na=True: this argument change missing values to the "NaN"
print(pd.read_csv("suraj.csv",keep_default_na=True)) 

#na_filter=False:it is indicate (datasets) there is no missing values
print(pd.read_csv("people-100.csv",na_filter=False))

#isnull method : used to check if null values in dataset it gives true else it gives false
data=pd.read_csv("people-100.csv")
print(data.isnull())

#sum():count the missing value it use with isnull method
data1=pd.read_csv("suraj.csv")
print(data1.isnull().sum().sum()) #total null values define

#notnull method: used to check null and not null values.
#True indicate notnull values and False indicate null values
print(data1.notnull())
print(data1.notnull().sum()) # to check colums and find not null values
print(data1.notnull().sum().sum()) #to check total notnull values

#dropna method :used to remove "NaN"values row and colums
print(data1.dropna(axis=1))