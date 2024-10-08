--------------------------------------------------------------------------------------------------------------------------------------------------------------
What-are-python-variables ?
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Variable is a name that is used to refer to memory location. 
Python variable is also known as an identifier and used to hold value

In Python, we don't need to specify the type of variable because Python is a inferred language and smart enough to get variable type.
Variable names can be a group of both the letters and digits, but they have to begin with a letter or an underscore

It is recommended to use lowercase letters for the variable name. MyVar and myvar both are two different variables

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Identifier Naming:

Variables are the example of identifiers. An Identifier is used to identify the literals used in the program. The rules to name an identifier are given below

1.  The first character of the variable must be an alphabet or underscore ( _ )
2.  All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9)
3.  Identifier name must not be similar to any keyword defined in the language
4.  Identifier names are case sensitive; for example, my name, and MyName is not the same.
        Examples of valid identifiers: a123, _n, n_9, etc.
        Examples of invalid identifiers: 1a, n%4, n 9, etc.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Declaring Variable and Assigning Values

Python does not bind us to declare a variable before using it in the application. It allows us to create a variable at the required time.We don't need to 
declare explicitly variable in Python. When we assign any value to the variable, that variable is declared automatically.The equal (=) operator is used to 
assign value to a variable

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Object References

    It is necessary to understand how the Python interpreter works when we declare a variable. The process of treating variables is somewhat different from many
    other programming languages.Python is the highly object-oriented programming language; that's why every data item belongs to a specific type of class. 
    
    Consider the following example.

    print("Python")         #Output:    Python
    print(type("Python"))   #Output:    <class 'str'>

    -->In Python, variables are a symbolic name that is a reference or pointer to an object. 
    The variables are used to denote objects by that name
    
    Let's understand the example
        a = 50

    The variable a refers to an integer object.
    Suppose we assign the integer value 50 to a new variable b.

    The variable b refers to the same object that a points to because Python does not create another object.
    Let's assign the new value to b. Now both variables will refer to the different objects.

    Python manages memory efficiently if we assign the same variable to two different values.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Object Identity

In Python, every created object identifies uniquely in Python. Python provides the guaranteed that no two objects will have the same identifier. 
The built-in id() function, is used to identify the object identifier. 

Consider the following example.

    a = 50  
    b = a  
    print(id(a))    #Output:    140734982691168
    print(id(b))    #Output:    140734982691168

    # Reassigned variable a  
    a = 500  
    print(id(a))    #Output:    2822056960944

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Variable Names:

Variable names can be any length can have uppercase, lowercase (A to Z, a to z), the digit (0-9), and underscore character(_). 

Consider the following example of valid variables names.

    name = "Devansh"  
    age = 20  
    marks = 80.50  
    
    print(name)     #Output:    Devansh  
    print(age)      #Output:    20
    print(marks)    #Output:    80.5

The multi-word keywords can be created by the following method.

    a.  Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. There is no 
    intervention of whitespace. 
    
        For example - nameOfStudent, valueOfVaraible, etc.
    
    b.  Pascal Case - It is the same as the Camel Case, but here the first word is also capital. 
        For example - NameOfStudent, etc.
    
    c.  Snake Case - In the snake case, Words are separated by the underscore. 
        For example - name_of_student, etc.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multiple Assignment

Python allows us to assign a value to multiple variables in a single statement, which is also known as multiple assignments
We can apply multiple assignments in two ways, either by assigning a single value to multiple variables or assigning multiple values to multiple variables. 

Consider the following example

1.  Assigning single value to multiple variables

e.g.

    x=y=z=50    
    print(x)    #Output:    50
    print(y)    #Output:    50
    print(z)    #Output:    50

--------------------------------------------------------------------------------------------------------------------------------------------------------------
2.  Assigning multiple values to multiple variables:

e.g.

    a,b,c=5,10,15
    print(a)        #Output:    5
    print(b)        #Output:    10
    print(c)        #Output:    15

--------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Python Variable Types

There are two types of variables in Python - Local variable and Global variable. Let's understand the following variables.

**********************
a.  Local Variable  :   Local variables are the variables that declared inside the function and have scope within the function

    # Declaring a function
    def add():  
        # Defining local variables. They has scope only within a function  
        a = 20  
        b = 30  
        c = a + b  
        print("The sum is:", c)  
    
    # Calling a function  
    add()

    # Output:   The sum is: 50

    # Explanation:  we declared a function named add() and assigned a few variables within the function. 
    These variables will be referred to as the local variables which have scope only inside the function. 
    If we try to use them outside the function, we get a following error
        
    add()  
    # Accessing local variable outside the function   
    print(a)  

    # Output:   The sum is: 50
    print(a)
    NameError: name 'a' is not defined
    # We tried to use local variable outside their scope; it threw the NameError.

**********************
b.  Global Variables : Global variables can be used throughout the program, and its scope is in the entire program. We can use global variables inside or outside 
the function. A variable declared outside the function is the global variable by default. Python provides the global keyword to use global variable inside the 
function. If we don't use the global keyword, the function treats it as a local variable. 

Let's understand the following example

e.g.:

    # Declare a variable and initialize it  
    x = 101  
    
    # Global variable in function  
    def mainFunction():  
        # printing a global variable  
        global x  
        print(x)  
        # modifying a global variable  
        x = 'Welcome To Javatpoint'  
        print(x)  
    
    mainFunction()  
    print(x)

    # Output:
    101
    Welcome To Javatpoint
    Welcome To Javatpoint

we declare a global variable x and assign a value to it. Next, we defined a function and accessed the declared variable using the global keyword inside the function. 
Now we can modify its value. Then, we assigned a new string value to the variable x

**********************
c.  Delete a variable : We can delete the variable using the del keyword. The syntax is given below.

    del <variable_name>

In the following example, we create a variable x and assign value to it. We deleted variable x, and print it, we get the error "variable x is not defined". 
The variable x will no longer use in future

e.g.

    # Assigning a value to x  
    x = 6  
    print(x)  
    # deleting a variable.   
    del x  
    print(x)

    6
    Traceback (most recent call last):
        print(x)
    NameError: name 'x' is not defined


    # Maximum Possible Value of an Integer in Python
    Unlike the other programming languages, Python doesn't have long int or float data types. 
    It treats all integer values as an int data type.
    What is the maximum possible value can hold by the variable in Python? 

e.g.

    # A Python program to display that we can store  
    # large numbers in Python  
    
    a = 10000000000000000000000000000000000000000000  
    a = a + 1  
    print(type(a))  
    print (a)

    # Output:
    <class 'int'>
    10000000000000000000000000000000000000000001

--------------------------------------------------------------------------------------------------------------------------------------------------------------
Print Single and Multiple Variables in Python

We can print multiple variables within the single print statement.

    # printing single value   
    a = 5  
    print(a)  

    # Output
    5
    5

    # Printing Multiple Variables
    a = 5
    b = 6

    # printing multiple variables
    print(a,b)  
    # separate the variables by the comma 
    Print(1, 2, 3, 4, 5, 6, 7, 8)   