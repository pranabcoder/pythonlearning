"""
This code demonstrates how to define and change variables in Python.
It defines variables of different data types such as integer, float, and string.
It also shows how to change the value of a variable and how it affects other variables.
"""



x = 15
price = 9.99
discount = 0.2
result = price * (1 - discount)

# print the value to user
print(result)

name = "Rolf"
name = "Bob"
print(name * 2)

# Changing variable value
a = 25
b = a
print(a)
print(b)
b = 17
print(a)
print(b)

# Python is dynamic typed language
"""	
If you are from C++ or Java, if you are not from those languages, don't worry.
Okay?
Just for those people.I am saying this if you are familiar with C++ and java, you may be knowing that you cannot
declare any variable without without defining its data type like in C, C++ or java.
You have to say integer X, then only you can assign value 25 and to this x you cannot store value 13.75.
This is not allowed in other languages, but in Python it is allowed because we don't have to define the type of a variable.
Just you can simply use the variable. That's how the data types are handled in Python. So Python is dynamically typed language.
"""
x = 25
print(type(x))
x = 13.75
print(type(x))
x = "Rolf"
print(type(x))

x = [1, 2, 3, 4, 5]
print(type(x))


