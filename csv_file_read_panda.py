import pandas as pd

#read csv file:
var=(pd.read_csv("people-100.csv"))
print(var)
print(pd.read_csv("organizations-100.csv"))

#print saparate row:

print(pd.read_csv("organizations-100.csv",nrows=2))

#print saparate colums:
print(pd.read_csv("organizations-100.csv",usecols=[0,1]))

#skip rows:
print(pd.read_csv("organizations-100.csv",skiprows=1)) 

#we can skip multiple rows:
print(pd.read_csv("organizations-100.csv",skiprows=[1,2,3]))