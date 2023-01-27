'''
Docstring Comments
Python docstrings provide a convenient way to provide a help documentation with Python modules, 
functions, classes, and methods. The docstring is then made available via the __doc__ attribute.
'''

# Following is a simple add function with a multiline comment which serve's as its documentation
def f_add(a,b):
    ''' Function to add two numbers
 Add real numbers with this function'''
    return (a+b)

print(f_add.__doc__)
# Output
'''
 Function to add two numbers
 Add real numbers with this function
'''