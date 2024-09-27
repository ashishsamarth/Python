--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python_Literals__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Python literals or constants are the notation for representing a fixed value in source code. In contrast to variables, literals (123, 4.3, "Hello") are static
 values or you can say constants which do not change throughout the operation of the program or application

For example, in the following assignment statement.
x = 10  :   
Here 10 is a literal as numeric value representing 10, which is directly stored in memory. However,

y = x*2 :   Here, even if the expression evaluates to 20, it is not literally included in source code.

__Types of Python Literals__

a. Python - Integer Literal
b. Python - Float Literal
c. Python - Complex Literal
d. Python - String Literal
e. Python - List Literal
f. Python - Tuple Literal
g. Python - Dictionary Literal

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python - Integer Literal**
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Any representation involving only the digit symbols (0 to 9) creates an object of int type.

Example: Decimal Literal
x = 10
y = -25
z = 0

Example: Octal Literal
x = 0O34

Example: Hexadecimal Literal
x = 0X1C

Example: Demonstrating Octal & Hexadecimal Notations as Integer

# Using Octal notation
x = 0O34
print ("0O34 in octal is", x, type(x))
# Using Hexadecimal notation
x = 0X1c
print ("0X1c in Hexadecimal is", x, type(x))

Output:
0O34 in octal is 28 <class 'int'>
0X1c in Hexadecimal is 28 <class 'int'>

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python - Float Literal**
--------------------------------------------------------------------------------------------------------------------------------------------------------------
A floating point number consists of an integral part and a fractional part. Conventionally, a decimal point symbol (.) separates these two parts in a literal 
representation of a float.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python - Complex Literal**
--------------------------------------------------------------------------------------------------------------------------------------------------------------
A complex number comprises of a real and imaginary component. The imaginary component is any number (integer or floating point) multiplied by square root of 
"-1". (√ −1). In literal representation (−1−−−√) is representation by "j" or "J". Hence, a literal representation of a complex number takes a form x+yj.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python - String Literal**
--------------------------------------------------------------------------------------------------------------------------------------------------------------
A string object is one of the sequence data types in Python. It is an immutable sequence of Unicode code points. Code point is a number corresponding to a 
character according to Unicode standard. Strings are objects of Python's built-in class 'str'.

String literals are written by enclosing a sequence of characters in single quotes ('hello'), double quotes ("hello") or triple quotes ('''hello''' or 
"""hello""").

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python - List Literal**
--------------------------------------------------------------------------------------------------------------------------------------------------------------
List object in Python is a collection of objects of other data type. List is an ordered collection of items not necessarily of same type. Individual object in 
the collection is accessed by index starting with zero.

Literal representation of a list object is done with one or more items which are separated by comma and enclosed in square brackets [].

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python - Tuple Literal**
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Tuple object in Python is a collection of objects of other data type. Tuple is an ordered collection of items not necessarily of same type. Individual object 
in the collection is accessed by index starting with zero.
Literal representation of a tuple object is done with one or more items which are separated by comma and enclosed in parentheses ().

Example: Tuple Type Literal Without Parenthesis [This is valid]
T1=1,"Ravi",75.50, True
print (T1, type(T1))

Output:
[1, 'Ravi', 75.5, True] <class tuple>

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python - Dictionary Literal**
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Like list or tuple, dictionary is also a collection data type. However, it is not a sequence. It is an unordered collection of items, each of which is a 
key-value pair. Value is bound to key by the ":" symbol. One or more key:value pairs separated by comma are put inside curly brackets to form a dictionary
 object.
Key should be an immutable object. Number, string or tuple can be used as key. Key cannot appear more than once in one collection. If a key appears more than 
once, only the last one will be retained. Values can be of any data type. One value can be assigned to more than one keys.

--------------------------------------------------------------------------------------------------------------------------------------------------------------