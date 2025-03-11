import pandas as pd
df=pd.read_csv("table.csv")

#interpolate method used to fill missing value
print(df)
print(df.interpolate())  #only fill numeric value 
print(df.interpolate(limit=1))  #we can set limit missing value

