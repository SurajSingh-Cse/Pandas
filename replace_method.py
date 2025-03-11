import pandas as pd

data=pd.read_csv("surajj.csv")

#replace method: used to replace value
#print(data.replace(to_replace='Male',value='Men')) #"male" values  replace to "Men"
print(data.replace({'Male':'Men'})) #shortcut way to replace
print(data.replace([1,2,3,4,5,6,7,8,9,10,11,12,13,14],0)) #id number replace to zero

#replace values using list:
print(data.replace([1,2,3,4,5,6,7,8,9,10,11,12,13,14],[15,16,17,18,19,20,21,22,23,24,25,26,27,28])) 

print(data.replace({"Sex":'[A-Za-z]'},0, regex=True)) #replace particular colums values using dictionary
 
