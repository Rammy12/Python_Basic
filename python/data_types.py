"""
Data types are the classification or categorization of data items.
It represents the kind of value that tells what operations can be performed on a particular data.
Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

Following are the standard or built-in data type of Python:

Numeric
Sequence Type
Boolean
Set
Dictionary

"""
#  Integer Data Type
a = 5
print("Type of a: ", type(a))
#  Integer Data Type
b = 5.0
print("\nType of b: ", type(b))
#  Integer Data Type
c = 2 + 4j
print("\nType of c: ", type(c))

"""
Sequence Type

In Python, sequence is the ordered collection of similar or different data types.
Sequences allows to store multiple values in an organized and efficient fashion.
There are several sequence types in Python
String
List
Tuple

"""
# Creating a String
# with single Quotes
String1 = 'Welcome to the Python'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String2 = "I'm a Rammy"
print("\nString with the use of Double Quotes: ")
print(String2)
print(type(String2))

# Creating a String
# with triple Quotes
String3 = '''I'm a Rammy and I live in a world of "Programming"'''
print("\nString with the use of Triple Quotes: ")
print(String3)
print(type(String3))

# Creating String with triple
# Quotes allows multiple lines
String4 = '''Love
is
Life'''
print("\nCreating a multiline String: ")
print(String4)