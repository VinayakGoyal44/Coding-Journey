#variables are used to store data in memory. In Python, you can create a variable by assigning a value to it using the equals sign (=).
a= ("hello",1,"hi") #this is a tuple. A tuple is a collection of data types that are ordered and immutable.
#here we can relate it with maths that a is a set and hello,1,hi are its elements. 
#here hello, 1 are diff data types. hello is string and 1 is integer.
print(a)
#we have to add double quote in string because if we dont then if someone wrote hello as a variable then how the python distinguish it
#none and true are also different data types. None is a special data type that represents the absence of a value, while True is a boolean value that represents truth.
b= None
print(b)
c= False
print(c)
#we can add two variables only if their data type is same.
d=8
e=10
print(d+e) 
f= "hello"
g= "world"
print(f+g) #here we can add two strings but it will not add space between them. If we want to add space then we have to add it manually.
h=False
print(c+h) #true+false=1+0=1. In python, true is represented as 1 and false is represented as 0. 
print("the type of a is ", type(a))
print("the type of b is ", type(b))
print("the type of c is ", type(c))
print("the type of d is ", type(d))
print("the type of e is ", type(e))
print("the type of f is ", type(f))
print("the type of g is ", type(g))
print("the type of h is ", type(h))
i= 3.14
print("the type of i is ", type(i)) 
j= 2+3j
print("the type of j is ", type(j)) #j is a complex number.
list1= [1,2,["Vinayak"],2.5] #list is a collection of data types. it is mutable
print("the type of list1 is ", type(list1))
dict1= {"name":"Vinayak","age":18} #dict is a collection of key-value pairs. it is mutable
print("the type of dict1 is ", type(dict1))
print(dict1) #ek sath map kr diya 2 elements ko. name is key and Vinayak is value. age is key and 18 is value.