--------------------------------------------------------------------------------------------------------------------------------------------------------------
Python keywords are unique words reserved with defined meanings and functions that we can only apply for those functions
You dont need to import any keyword into your program because they're permanently present.

However Python built in methods and classes are different. Built-in methods and classes are constantly present.

Assigning a particular meaning to Python keywords means you can't use them for other purposes in our code. 
You'll get a message of SyntaxError if you attempt to do the same

If you attempt to assign anything to a built-in method or type, you will not receive a SyntaxError message

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Python contains the following keywords

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    False	await	    else	    import	    pass
    None	break	    except	    in	        raise
    True	class	    finally	    is	        return
    and	    continue	for	        lambda	    try
    as	    def	        from	    nonlocal	while
    assert	del	        global	    not	        with
    async	elif	    if	        or	        yield

--------------------------------------------------------------------------------------------------------------------------------------------------------------
To get the complete list of python keywords, you can use the following library

    # import keyword library
    import keyword

    # run dir() {python3 built-in} function on the libray
    # to get a list of attributes and methods

    print(f'Here is the complete list of attribues and methods of keyword library \n\n {dir(keyword)}')
    print('-'*60)

    # To get the list of all keywords in python 3

    print(f'Here is the current list of reserved keywords: \n\n{keyword.kwlist}')

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output
    Here is the complete list of attribues and methods of keyword library 

    ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
    'iskeyword', 'kwlist', 'main']
    ------------------------------------------------------------
    Here is the current list of reserved keywords: 

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
    'else', 'except', 'finally', 'for',     'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
    'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Value Keywords: True, False, None

--------------------------------------------------------------------------------------------------------------------------------------------------------------

Note: True is 1 and False is 0
e.g.

    print( 4 == 4 )             :   True
    print( 6 > 9 )              :   False
    print( True or False )      :   True    (Based on the OR condition)
    print( 9 <= 28 )            :   True    (Based on the OR condition)
    print( 6 > 9 )              :   False
    print( True and False )     :   False   (Based on the AND condition)

**********************
None is a Python keyword that means "nothing." 
None is known as nil, null, or undefined in different computer languages

Note: If a function does not have a return value, It will give None as the default output.
e.g.

    print( None == 0 )          :   False
    print( None == " " )        :   False
    print( None == False )      :   False

    A = B = None
    print( A == B )             :   True

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Operator Keywords: and, or, not, in, is

--------------------------------------------------------------------------------------------------------------------------------------------------------------

__AND Keyword__

Truth Table for 'AND'

    X	    Y	        X and Y
    True----True	    True
    False---True	    False
    True----False	    False
    False---False	    False

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__OR Keyword__

Truth Table for 'OR'

    X	    Y	        X or Y
    True----True	    True
    True----False	    True
    False---True	    True
    False---False	    False

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__NOT Keyword__

Truth Table for 'NOT'

    X	        not X
    True	    False
    False	    True

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__IN Keyword__

The in keyword of Python is a robust confinement checker, also known as a membership operator.
If you provide it an element to seek and a container or series to seek into, it will give True or False, depending on if that given element was located in the 
given container

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Define a variable to have a string
    _my_spyder_var = 'Python is awesome'

    # Checking membership using 'in' operator for lowercase 'p'
    print(f"Is p present in the string :-  {'p' in _my_spyder_var}")

    # Checking membership using 'in' operator for lowercase 'P'
    print(f"Is P present in the string :-  {'P' in _my_spyder_var}")

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output

    Is p present in the string :-  False
    Is P present in the string :-  True


--------------------------------------------------------------------------------------------------------------------------------------------------------------
__IS Keyword__

The 'is' keyword is used to check the identification of objects. The '==' operation is used to determin where two arguments are identical.
The 'is' keyword determines where two arguments related to the unique object.
When the objects are the same, it results in True, else a False.

e.g.

    print( True is True )           : #Output   True
    print( False is True )          : #Output   False
    print( None is not None )       : #Output   False
    print( (9 + 5) is (7 * 2) )     : #Output   True


    print( [] == [] )               : #Output   True
    print( [] is [] )               : #Output   False
    print( {} == {} )               : #Output   True
    print( {} is {} )               : #Output   False
    print( set() == set()  )        : #Output   True
    print( set() is set()  )        : #Output   False

A blank dictionary or list or set is the same as another blank one. However, they aren't identical entities because they are stored independently in memory. 
This is because both the list, set and the dictionary are changeable

    print( '' == '' )  
    print( '' is '' )  
    print( () == () )  
    print( () is () )  
    print( frozenset() == frozenset())
    print( frozenset() is frozenset())

A blank string or tuple or frozenset is same as the another one and also they are identical because these are not mutable.

    A = 'a'
    B = 'a'
    print(A == B)                   : #Output   True
    print(A is B)                   : #Output   True

    A = B ='a'
    print(A == B)                   : #Output   True
    print(A is B)                   : #Output   True


--------------------------------------------------------------------------------------------------------------------------------------------------------------
# nonlocal keyword

--------------------------------------------------------------------------------------------------------------------------------------------------------------
Nonlocal keyword usage is fairly analogous to global keyword usage. 

The keyword nonlocal is designed to indicate that a variable within a function that is inside a function, i.e., a nested function is just not local to it, mplying that it is located in the outer function. 

We must define a non-local parameter with nonlocal if we ever need to change its value under a nested function. Otherwise, the nested function creates a local variable using that title

e.g.

    # Create a function
    def the_outer_function():
        # Define a local variable
        var = 10  
        # Create another function inside the outer function
        def the_inner_function():  
            # Define a new variable with keyword - nonlocal
            nonlocal var  
            var = 14  
            print("The value inside the inner function: ", var)
        
        # Call the inner function
        the_inner_function()  
        print("The value inside the outer function: ", var)  

    # call the outher function
    the_outer_function()  

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output
    The value inside the inner function:  14
    The value inside the outer function:  14

--------------------------------------------------------------------------------------------------------------------------------------------------------------

the_inner_function() is placed inside the_outer_function in this case.
Var is not a global variable.As a result, if we wish to change it inside the the_inner_function(), we should declare it using nonlocal
As a result, the variable was effectively updated within the nested the_inner_function

Now see the variation without the nonlocal keyword

    # Display usage without nonlocal keyword
    def the_outer_function():
        # Define a local variable
        var = 10  
        # Create another function inside the outer function
        def the_inner_function():
            # Define a new variable with in the inner function
            var = 14  
            print("Value inside the inner function: ", var)  
        # Call the inner function
        the_inner_function()  
        print("Value inside the outer function: ", var)  
    # call the outher function  
    the_outer_function()  

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output
    Value inside the inner function:  14
    Value inside the outer function:  10

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Iteration Keywords: for, while, break, continue

The iterative process and looping are essential programming fundamentals. To generate and operate with loops, Python has multiple keywords. These would be utilized and observed in almost every Python program.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__FOR Keyword__

The for loop is by far the most popular loop in Python. It's built by blending two Python keywords. They are for and in

e.g.
    for i in range(15):
        print( i + 4, end = " ") 

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Output
    4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__WHILE Keyword__

Python's while loop employs the term while and functions similarly to other computer languages' while loops. 
The code block after the while phrase will be repeated until the condition following the while keyword is false.

e.g.

    # looping from 1 to 15  
    i = 0 # initial condition  
    while i < 15:  
            
        # When i has value 9, loop will jump to next iteration using continue. It will not print  
        if i == 9:  
            i += 3
        else:  
            # when i is not equal to 9, adding 2 and printing the value  
            print( i + 2, end = " ")  
                
        i += 1

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output
    2 3 4 5 6 7 8 9 10 15 16 

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__BREAK Keyword__
If you want to quickly break out of a loop, employ the break keyword. We can use this keyword in both for and while loops.

e.g.

    for i in range(15):   
        print( i + 4, end = " ")     
        # breaking the loop when i = 9  
        if i == 9:  
            break     
    print()

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output
    4 5 6 7 8 9 10 11 12 13

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__CONTINUE Keyword__
The continue keyword, enables you to quit performing the present loop iteration and go on to the subsequent one

 e.g.

    # looping from 1 to 15  
    i = 0 # initial condition  
    while i < 15:  
            
        # When i has value 9, loop will jump to next iteration using continue. It will not print  
        if i == 9:  
            i += 3  
            continue  
        else:  
            # when i is not equal to 9, adding 2 and printing the value  
            print( i + 2, end = " ")  
                
        i += 1

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output
    2 3 4 5 6 7 8 9 10 14 15 16

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exception Handling Keywords: try, except, raise, finally and assert

--------------------------------------------------------------------------------------------------------------------------------------------------------------

__try__: This keyword is designed to handle exceptions and is used in conjunction with the keyword except to handle problems in the program. When there is some kind of error, the program inside the "try" block is verified, but the code in that block is not executed.


__except__: As previously stated, this operates in conjunction with "try" to handle exceptions.


__finally__: Whatever the outcome of the "try" section, the "finally" box is implemented every time.


__raise__: The raise keyword could be used to specifically raise an exception.


__assert__: This method is used to help in troubleshooting. Often used to ensure that code is correct. Nothing occurs if an expression is interpreted as true; however, if it is false, "AssertionError" is raised. An output with the error, followed by a comma, can also be printed.

e.g.

    # initializing the numbers  
    var1 = 4  
    var2 = 0  
        
    # Exception raised in the try section  
    try:  
        d = var1 // var2 # this will raise a "divide by zero" exception.  
        print(f"d \n")  
    # this section will handle exception raised in try block  
    except ZeroDivisionError:  
        print(f"Except Block: We cannot divide by zero \n")  
    finally:  
        # If exception is raised or not, this block will be executed every time  
        print(f"Finally Block: This is inside finally block \n")  

    print ("Try Block: The value of var1 / var2 is : ")    
    print (var1 / var2)  


--------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Output

    Except Block: We cannot divide by zero 

    Finally Block: This is inside finally block 

    Try Block: The value of var1 / var2 is : 
    Traceback (most recent call last):

    File "C:\Users\Ashish Samarth\untitled5.py", line 17, in <module>
        print (var1 / var2)

    ZeroDivisionError: division by zero

--------------------------------------------------------------------------------------------------------------------------------------------------------------
e.g.

    # initializing the numbers  
    var1 = 4  
    var2 = 0  
        
    # By using assert keyword we will check if var2 is 0  
    assert var2 != 0, "Divide by 0 error"

    # Exception raised in the try section  
    try:  
        d = var1 // var2 # this will raise a "divide by zero" exception.  
        print(f"d \n")  
    # this section will handle exception raised in try block  
    except ZeroDivisionError:  
        print(f"Except Block: We cannot divide by zero \n")  
    finally:  
        # If exception is raised or not, this block will be executed every time  
        print(f"Finally Block: This is inside finally block \n")  

    print ("Try Block: The value of var1 / var2 is : ")    
    print (var1 / var2)  


--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output

    Traceback (most recent call last):

    File "C:\Users\Ashish Samarth\untitled5.py", line 6, in <module>
        assert var2 != 0, "Divide by 0 error"

    AssertionError: Divide by 0 error

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # This is am important functionality of assert, it will stop the execution if the assertion fails and not let the program continue.
    # None of the try, except, finally code blocks got executed.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__pass Keyword__

--------------------------------------------------------------------------------------------------------------------------------------------------------------
A null sentence is called a pass. It serves as a stand-in for something else. 
When it is executed, nothing occurs

Let's say we possess a function that has not been coded yet however we wish to do so in the long term. If we write just this in the middle of code,

    def function_pass( arguments ):
                                   ^
    IndentationError: expected an indented block after function definition on line 1

    IndentationError will be thrown. 
    Rather, we use the pass command to create a blank container.

    def function_pass( arguments ):  
        pass  

    We can use the pass keyword to create an empty class too.
    class passed_class:  
        pass

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__return Keyword__

return expression is used to leave a function and generate a result.
None keyword is returned by default if we don't specifically return a value

e.g.

    def func_with_return():  
        var = 13  
        return var  
    
    def func_with_no_return():  
        var = 10  
    
    print( func_with_return() )  
    print( func_with_no_return() )

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Output
    13
    None

--------------------------------------------------------------------------------------------------------------------------------------------------------------
__del keyword__
--------------------------------------------------------------------------------------------------------------------------------------------------------------
del keyword is used to remove any reference to an object. In Python, every entity is an object. We can use the del command to remove a variable reference.

e.g.

    var1 = var2 = 5  
    del var1  
    print( var2 )
    print('*' * 50) 
    print( var1 )  

--------------------------------------------------------------------------------------------------------------------------------------------------------------
    # output
    5
    **************************************************
    Traceback (most recent call last):

    File "C:\Users\Ashish Samarth\untitled7.py", line 12, in <module>
        print( var1 )

    NameError: name 'var1' is not defined

--------------------------------------------------------------------------------------------------------------------------------------------------------------