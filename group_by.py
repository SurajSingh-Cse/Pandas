import pandas as pd
df=pd.read_csv("table.csv")
gr1=df.groupby(by="gender")
print(gr1) #it is return dataframe group by obj
print(gr1.groups)  #devide group by male and female

#devide group
for gender,df in gr1:
    print(gender)  
    print(df) 

#list
print(list(gr1)) 

#dictionary
print(dict(list(gr1))) 

print(gr1.sum())  #sum calculate

#print(gr1.mean()) #get mean

print(gr1.describe()) 
