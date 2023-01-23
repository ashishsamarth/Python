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