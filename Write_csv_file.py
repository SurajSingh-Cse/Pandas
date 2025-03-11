import pandas as pd

data=pd.read_csv("people-100.csv",header=None) #remove header
print(data)

data1=pd.read_csv("people-100.csv",header=1) #change header which is covert data 1 is header 
print(data1)

data2=pd.read_csv("people-100.csv",names=['A','B','C','D','E','F','G','H','I'])  #CHANGE HEADING NAME IN CSV FILE
print(data2)
 
 #head method:
data3=pd.read_csv("people-100.csv")
print(data3.head())  #head methods print 5 rows in csv file
print(data3.head(1)) #print only one row  
print(data3.head(8)) #print 8 rows begin with

#tail method:
data4=pd.read_csv("people-100.csv")
print(data4.tail()) #print ending with 5rows
print(data4.tail(8)) #print ending with 8 rows

#dtype argument:
data5=pd.read_csv("people-100.csv", dtype={"Index":'float64'}) #dtype parameter change datatype of perticular colum
print(data5)

#use below as a parameter:
#true_values=['yes'] :its covert" yes->true" and "true->yes" 
#false_values=['No'] : its convert "No value->False"
