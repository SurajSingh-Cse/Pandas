import pandas as pd
df=pd.read_csv("table.csv")

#loc: it is used to insert perticular rows in dataset
print(df.loc[0])
print(df.loc[1])
print(df.loc[[0,2]]) #multiple rows
print(df.loc[4,"gender"]) #in 4th row gender colums value 
print(df.loc[0:5,"mark"]) # target a specific colums values

#iloc: it is used to print desire values(label indexing)
print(df.iloc[[0]])
print(df.iloc[:,1])   #all rows 1th colums print

