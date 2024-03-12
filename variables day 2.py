#Day_2 # ---->swapping of variables
#Eg-1
a=7
b=5
print(a,b)
temp = a
a = b
b = temp
print(a,b)
b = b,a
print("a =", a  )
print("a =", a)
print(a,b)
a = a + b
b = a - b
a = a - b
print(a,b)
a = a * b
b = a / b
a = a / b
print(a,b)
# id()---> used to find the memory address of the variable a = 7 b = 9 print(id(a)) print(id(b))
 #----->keywords
 #keywords are reserved words which provides special meaning to
 #compiler or interpretor
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

 #to check if the string is keyword or not print(keyword.iskeyword("sai"))#flase
 # ----> literals
 #literal is the constant value assigned to a variable
 #A variable is considers to be constant whwn it ois defines
 #in caps
a=78#variable
A=78#consant
 #hash() ---->it creates a hash value for constant datatypes and provides error for non constant datatypes
n1 = 89+7j
print(hash(n1))
f1 = [7,8,9]
print(hash(f1))
#error --->list is non-constant or mutable datatype
#---->operator
#operators are symbols which is used to perfrom various operations
#b/w 2 or more operands
#arthamatic
#logical
#relational or comparison
 #bitwise
 #identity
 #membership
 #to do armatic--->+,-,*,/,%,**,?
 #ex:1
a=8
b=9
c=7
#print(a+b+c)
# input() ---> used to get the runtime input
n1=input("enter the value")
#print(n1)
#input() ----> used to get runtime values of all datatypes
n1=eval(input("enter the value"))
#print(type(n1))
a=4
b=2
#print(a/2)
# is used to get the quotient value
#print(a%b)#is used to get the reminder value
# --->float division
a=765433
b=19
#print(a//b)#->the output will be inn integer & output  will be based onfloor value

#---->assignment
a=5
a+=2
print(a)

a=30
a-=5
print(a)
#---->bitwise
a=7
b=4
print(a&b)
#---->logical
#and,not,or
a=6
#print(a>3 and a<10)
#print(a>7 and a<10)
#print(not(a<8 and a<10))

  
 
 







 


