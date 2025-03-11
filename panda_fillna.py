import pandas as pd

data=pd.read_csv("suraj.csv")

#fillna method: fill the missing value  
print(data.fillna(0))  # 0 is scalar values
print(data.fillna({"Organization Id":"none","Unnamed":"missing"} )) #missing values replace "None" in "Organization Id"
print(data.fillna(method="ffill")) # it is used forward values
print(data.fillna(mathod="bfill")) #it is used backword values
print(data.fillna(0,limit=1)) # set the limit how much colums fill with (0))
print(data.fillna(5, inplace=True))