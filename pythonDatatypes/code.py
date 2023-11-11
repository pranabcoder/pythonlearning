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

"""	
Rules for declaring variables in Python
1. Name can contain alpha-numerical characters and underscore.
2. Name should start with a letter or an underscore.
3. Keyword should not be used as variable name.
4. Variable name is case sensitive.
"""
# Example
x1 = 5
address1 = "India"
# address 1 = "India" -> invalid syntax
# address$1 = "India" -> invalid syntax
# _x1 = 5 -> valid

# Difference between identifier and keywords
""" 
When we say identifier, it is nothing but the name of a variable, function, class, 
module or object which will be used in our program.

When we say keyword, it is nothing but the reserved words in Python.
These keywords are used to define the syntax and structure of the Python language.
"""
price = 9.99
# price of item = 12.5 -> invalid syntax
# 1x = 5 -> invalid syntax
# while = 10  -> invalid syntax

# Python Data Types
"""	
Numeric - > int, float, complex, bool
Sequence - > list, tuple, string, bytes, bytearray, range
Set -> set, frozenset
Dictionary -> dict

Difference between list and tuple
List is mutable, tuple is immutable.
We can change the value of a list, but we cannot change the value of a tuple.
String is also immutable. it is sequence of characters.
bytes is immutable sequence of bytes. its value is 0 to 255.
bytearray is mutable sequence of bytes. its value is 0 to 255.
Set is unordered collection of unique items.
frozenset is immutable set. it is also unordered collection of unique items.Its value cannot be changed.
Dictionary is unordered collection of key value pairs.
"""	
# Check Memory consume by variable
x = 12378906578901234567890
print(x.__sizeof__())
y = -17
print(y.__sizeof__())

""" Maximum data types in python are immutable. So, instead of modifying the value of a variable,
it prefers creating a new data object and then assigning it to the variable."""

# Floating Point number
a = 13.25
b = - 17.66
c = 12.59
d = -12.59
print("{:.2e}".format(c))
print("{:.2e}".format(d))

