import pandas as pd


df=pd.DataFrame({"id":[1,2,3,4],
                 "class":[9,8,5,11]})
df1=pd.DataFrame({"id":[1,2,3,4],
                 "name":['A','B','C','D']})

print(pd.merge(df,df1,on='id')) #marge two dataset 
