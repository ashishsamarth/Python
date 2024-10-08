--------------------------------------------------------------------------------------------------------------------------------------------------------------
What are python literals?
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Python Literals can be defined as data that is given in a variable or constant.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.  String Literals

There are two types of Strings supported in Python:

a.  Single-line String- Strings that are terminated within a single-line are known as Single line Strings       
    e.g.        text1='Python' 

b.  Multi-line String - A piece of text that is written in multiple lines is known as multiple lines string     

e.g. 

    text1='hello\    
    user'    
    print(text1)

    str2='''welcome  
    to  
    SSSIT'''    
    print str2        


--------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.  Numeric Literals

Numeric Literals are immutable. Numeric literals can belong to following four different numerical types.

    Int(signed integers)    :   Numbers( can be both positive and negative) with no fractional part.eg: 100
    Long(long integers)     :   Integers of unlimited size followed by lowercase or uppercase L eg: 87032845L
    float(floating point)   :   Real numbers with both integer and fractional part eg: -26.2
    Complex(complex)        :   In the form of a+bj where a forms the real part and b forms the imaginary part of the complex 
                                number. eg: 3.14j


    x = 0b10100 #Binary Literals            
    y = 100 #Decimal Literal   
    z = 0o215 #Octal Literal  
    u = 0x12d #Hexadecimal Literal  
      
    #Float Literal  
    float_1 = 100.5   
    float_2 = 1.5e2  
      
    #Complex Literal   
    a = 5+3.14j  
      
    print(x, y, z, u)                   #Output:    20 100 141 301
    print(float_1, float_2)             #Output:    100.5 150.0
    print(a, a.imag, a.real)            #Output:    (5+3.14j) 3.14 5.0

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.  Boolean literals

A Boolean literal can have any of the two values: True or False

e.g.

    x = (1 == True)  
    y = (2 == False)  
    z = (3 == True)  
    a = True + 10  
    b = False + 10  
  
    print("x is", x)    #Output:   x is True
    print("y is", y)    #Output:   y is False
    print("z is", z)    #Output:   z is False
    print("a:", a)      #Output:   a is 11
    print("b:", b)      #Output:   b is 10

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4.  Special Literals

Python contains one special literal i.e., None
None is used to specify to that field that is not created. It is also used for the end of lists in Python.

e.g.

    val1=10    
    val2=None    
    print(val1)     #Output: 10
    print(val2)     #Output: None

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5.  Literal Collections

Python provides the four types of literal collection such as List literals, Tuple literals, Dict literals, and Set literals

--------------------------------------------------------------------------------------------------------------------------------------------------------------
a.  __Lists__:  List contains items of different data types. Lists are mutable i.e., modifiable. The values stored in List are separated by comma(,) and 
enclosed within square brackets([]). We can store different types of data in a List.

e.g.

    list=['John',678,20.4,'Peter']    
    list1=[456,'Andrew']    
    print(list)                     #Output:  ['John',678,20.4,'Peter']
    print(list + list1)             #Output:  ['John',678,20.4,'Peter',456,'Andrew']

--------------------------------------------------------------------------------------------------------------------------------------------------------------
b.  __Dictionary__: Python dictionary stores the data in the key-value pair. It is enclosed by curly-braces {} and each pair is separated by the commas(,).

e.g.

    dict = {'name': 'Peter', 'Age':18,'Roll_nu':101}
    print(dict)                                             #Output:{'name': 'Peter', 'Age': 18, 'Roll_nu': 101}

--------------------------------------------------------------------------------------------------------------------------------------------------------------
c.  __Tuple__:  Python tuple is a collection of different data-type. It is immutable which means it cannot be modified after creation. It is enclosed by the 
parentheses () and each element is separated by the comma(,).

e.g.    
        
    tup = (10,20,"Dev",[2,3,4])
    print(tup)                      #Output: (10, 20, 'Dev', [2, 3, 4])

--------------------------------------------------------------------------------------------------------------------------------------------------------------
d.  __Set__:    Python set is the collection of the unordered dataset. It is enclosed by the {} and each element is separated by the comma(,).Its and 
un-ordered collection

e.g.    
        
    set = {'apple','grapes','guava','papaya'} 
    print(set)                                  #Output: {'guava', 'apple', 'papaya', 'grapes'}