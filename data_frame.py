import pandas as pd
 
 #empty dataframe:
empty=pd.DataFrame()
print(empty)

#dataframe creating using list:
lst=['a','b','c','d','e'] #list
df=pd.DataFrame(lst)
print(df)

lst=pd.DataFrame([[1,2,3,4],[2,3,4,5]])
print(lst)


#using dictionary create dataframe:
dict={'id':[11,22,33,44],'name':["suraj","reeni","ashirwad","raman"]}
df1=pd.DataFrame(dict)
print(df1)

#list of dictionary:
lst_dict=[{'a':11,'b':22},{'a':33,'b':44}] #in a list create dictionary
df2=pd.DataFrame(lst_dict)
print(df2)

lst_dict2=[{'a':11,'b':22},{'a':33,'b':44},{'a':66}]
df3=pd.DataFrame(lst_dict2)
print(df3)

#create "dataframe" with help of dictionary in "series"
dict3={'ID':pd.Series([1,2,3,4,5,6]),'name':pd.Series(["su","vi","ku","mo","pa","ji"])}
df4=pd.DataFrame(dict3)
print(df4)