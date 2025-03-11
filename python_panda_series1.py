import pandas as pd

#list
sri=[12,24,36,48,"suraj","reeni"]
print(sri)

#create Series
print(pd.Series(sri))

#other method creating series:
sri1=pd.Series([11,22,33,44,"wow","mamaearth"])
print(sri1)

#empty Series:
empty=pd.Series([])
print(empty) 

#index in series:
sri2=pd.Series([11,22,33,44],index=["a","b","c","d"])
print(sri2)

#change datatype in series:
sri3=pd.Series([11,22,33,44],index=["a","b","c","d"],dtype=float)
print(sri3)

#single series scalar:
scalar=pd.Series(2,index=[1,2,3])
print(scalar)

#series create using dictionary:
dict=pd.Series({'a':11,'b':22,'c':33})
print(dict) 

#access series value:
sri4=pd.Series([11,22,33,44])
print(sri4[0])
print(sri4[2])
print(sri4[3])

#slicing in series:
print(sri4[0:2]) #using index number

#max value in series 
print(max(sri4)) #44-output
print(min(sri4)) #11-output

#condition operator use:
print(sri4[sri4 > 11])
print(sri4[sri4 < 44])


#Arithmatic Operation  of Series
s1=pd.Series([1,2,3,4,5])
print(s1)
s2=pd.Series([5,4,3,2,1])
print(s2)
#addition:
print(s1+s2)
#substraction
print(s1-s2)
#division:
print(s1/s2)
#multiplication:
print(s1*s2)
#squre 
print(s1**2)
print(s2**3)

#if series1 is not equal to series2 than:
s3=pd.Series([111,222,333,444,555])
s4=pd.Series([111,222,333,444,555,666,777,888])
print(s3+s4) #it is possible