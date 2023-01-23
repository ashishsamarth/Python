import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish Samarth//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

# Default behaviour of head() - It prints the top 5 rows of DataFrame
print(_my_df.tail())
print()
print('-------------------------------------------------------------')

# We can use an optional argument to limit the number of rows to override the default behavior
print(_my_df.tail(n=3))
print()
print('-------------------------------------------------------------')

# Another way to print 'all' rows of the DataFrame
print(_my_df.tail(n=len(_my_df)))
print()
print('-------------------------------------------------------------')

# Output
'''
    Name         Sex  Age  Height (in)  Weight (lbs)
13  Neil         "M"   36           75           160
14  Omar         "M"   38           70           145
15  Page         "F"   31           67           135
16  Quin         "M"   29           71           176
17  Ruth         "F"   28           65           131

-------------------------------------------------------------
'''