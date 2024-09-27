--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python DataTypes__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Python Data Types are used to define the type of a variable. It defines what type of data we are going to store in a variable. The data stored in memory can 
be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters.

A data type represents a kind of value and determines what operations can be done on it. Numeric, non-numeric and Boolean (true/false) data are the most obvious
 data types. However, each programming language has its own classification largely reflecting its programming philosophy.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Types of Python Data Types
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Data Type 	    Examples
Numeric 	    int, float, complex
String 	        str (text sequence type)
Sequence 	    list, tuple, range
Binary 	        bytes, bytearray, memoryview
Mapping 	    dict
Boolean 	    bool
Set 	        set, frozenset
None 	        NoneType

![Github Image](/Assets/Python-Data-Types.PNG)

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python Numeric Data Type__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Python numeric data types store numeric values. Number objects are created when you assign a value to them.Python supports four different numerical types and 
each of them have built-in classes in Python library, called int, bool, float and complex respectively

a. int (signed integers)
b. float (floating point real values)
c. complex (complex numbers)

Python's standard library has a built-in function type(), which returns the class of the given object. 
A complex number is made up of two parts - real and imaginary. They are separated by '+' or '-' signs. The imaginary part is suffixed by 'j' which is the 
imaginary number. The square root of -1 (−1−−−√), is defined as imaginary number. Complex number in Python is represented as x+yj, where x is the real part, 
and y is the imaginary part

![Github Image](/Assets/Python-Numeric-Data-Types.PNG)

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python String Data Type__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Python string is a sequence of one or more Unicode characters, enclosed in single, double or triple quotation marks (also called inverted commas).
Python strings are immutable which means when you perform an operation on strings, you always produce a new string object of the same type, rather than 
mutating an existing string.
As long as the same sequence of characters is enclosed, single or double or triple quotes don't matter.

A string in Python is an object of str class. It can be verified with type() function.

A string is a non-numeric data type. Obviously, we cannot perform arithmetic operations on it. However, operations such as slicing and concatenation can be done.
Python's str class defines a number of useful methods for string processing. Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes
 starting at 0 in the beginning of the string and working their way from -1 at the end.

The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator in Python.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python Sequence Data Type__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Sequence is a collection data type. It is an ordered collection of items. Items in the sequence have a positional index starting with 0. It is conceptually 
similar to an array in C or C++. There are following three sequence data types defined in Python.

a. List Data Type
b. Tuple Data Type
c. Range Data Type

Python sequences are bounded and iterable - Whenever we say an iterable in Python, it means a sequence data type (for example, a list).

**Python List Data Type**
Python Lists are the most versatile compound data types. A Python list contains items separated by commas and enclosed within square brackets ([]). To some 
extent, Python lists are similar to arrays in C. One difference between them is that all the items belonging to a Python list can be of different data type 
where as C array can store elements related to a particular data type.

A list in Python is an object of list class. We can check it with type() function.
The values stored in a Python list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working 
their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.

**Python Tuple Data Type**
Python tuple is another sequence data type that is similar to a list. A Python tuple consists of a number of values separated by commas. Unlike lists, however,
 tuples are enclosed within parentheses (...).
A tuple is also a sequence, hence each item in the tuple has an index referring to its position in the collection. The index starts from 0.
In Python, a tuple is an object of tuple class

As in case of a list, an item in the tuple may also be a list, a tuple itself or an object of any other Python class
To form a tuple, use of parentheses is **optional**. Data items separated by comma without any enclosing symbols are treated as a tuple by default.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed i.e. lists are mutable, 
while tuples are enclosed in parentheses ( ( ) ) and cannot be updated (immutable). Tuples can be thought of as read-only lists.

**Python Range Data Type** 
A Python range is an immutable sequence of numbers which is typically used to iterate through a specific number of items.
It is represented by the Range class. The constructor of this class accepts a sequence of numbers starting from 0 and increments to 1 until it reaches a 
specified number. Here is the description of the parameters used −

a. start: Integer number to specify starting position, (Its optional, Default: 0)
b. stop: Integer number to specify ending position (It's mandatory)
c. step: Integer number to specify increment, (Its optional, Default: 1)    

**Python Bytes Data Type**
The byte data type in Python represents a sequence of bytes. Each byte is an integer value between 0 and 255. It is commonly used to store binary data, such 
as images, files, or network packets. 
We can create bytes in Python using the built-in bytes() function or by prefixing a sequence of numbers with b. 

Consider the following Example:
---------------------------
#Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)  

output:
b'ABCDE'
---------------------------

Using the "b" prefix before a string to automatically create a bytes object −
#Using prefix 'b' to create bytes
b2 = b'Hello'  
print(b2)  

output:
b'Hello'
---------------------------

**Python Bytearray Data Type**
The bytearray data type in Python is quite similar to the bytes data type, but with one key difference: it is mutable, meaning you can modify the values 
stored in it after it is created.
You can create a bytearray using various methods, including by passing an iterable of integers representing byte values, by encoding a string, or by 
converting an existing bytes or bytearray object

Consider the following Example:
---------------------------
#Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value)  

Output: 
bytearray(b'Hello')

---------------------------
#Creating a bytearray by encoding a string
val = bytea rray("Hello", 'utf-8')  
print(val)  

Output:
bytearray(b'Hello')

**Python Memoryview Data Type**
A memoryview is a built-in object that provides a view into the memory of the original object, generally objects that support the buffer protocol, such as
 byte arrays (bytearray) and bytes (bytes). It allows you to access the underlying data of the original object without copying it, providing efficient memory
  access for large datasets.

You can create a memoryview using various methods. These methods include using the memoryview() constructor, slicing bytes or bytearray objects, extracting 
from array objects, or using built-in functions like open() when reading from files.

Consider the following Example:
---------------------------
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

Output:
<memory at 0x00000186FFAA3580>

---------------------------
If you have an array object, you can create a memoryview using the buffer interface as shown below −

import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)

Output:
<memory at 0x0000017963CD3580>

---------------------------
You can also create a memoryview by slicing a bytes or bytearray object −

data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])  
print(view)

Output:
<memory at 0x00000200D9AA3580>

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python Dictionary Data Type__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Python dictionaries are kind of hash table type. A dictionary key can be almost any Python type, but are usually numbers or strings
Python dictionary is like associative arrays or hashes found in Perl and consist of key:value pairs. The pairs are separated by comma and put inside curly 
brackets {}. To establish mapping between key and value, the semicolon':' symbol is put between the two.

Dictionary is an object of the built-in dict class. We can check it with the type() function.
Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).   

Python's dictionary is not a sequence. It is a collection of items but each item (key:value pair) is not identified by positional index as in string, list or 
tuple. Hence, slicing operation cannot be done on a dictionary. Dictionary is a mutable object, so it is possible to perform add, modify or delete actions with
 corresponding functionality defined in dict class.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python Set Data Type__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Set is a Python implementation of set as defined in Mathematics. A set in Python is a collection, but is not an indexed or ordered collection as string, list 
or tuple. An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.
Comma separated items in a set are put inside curly brackets or braces {}. Items in the set collection can be of different data types.

Note that items in the set collection may not follow the same order in which they are entered. The position of items is optimized by Python to perform 
operations over set as defined in mathematics.Python's Set is an object of built-in set class, as can be checked with the type() function

A set can store only immutable objects such as number (int, float, complex or bool), string or tuple. If you try to put a list or a dictionary in the set 
collection, Python raises a **TypeError** .

**Hashing is a mechanism in computer science which enables quicker searching of objects in computer's memory. Only immutable objects are hashable.**

Even if a set doesn't allow mutable items, the set itself is mutable. Hence, add/delete/update operations are permitted on a set object, using the methods in
 built-in set class. Python also has a set of operators to perform set manipulation

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__Python Boolean Data Type__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Boolean type provides two built-in values, True and False. These values are used to determine the given statement true or false. It denotes by the class bool.
 True can be represented by any non-zero value or 'T' whereas false can be represented by the 0 or 'F'