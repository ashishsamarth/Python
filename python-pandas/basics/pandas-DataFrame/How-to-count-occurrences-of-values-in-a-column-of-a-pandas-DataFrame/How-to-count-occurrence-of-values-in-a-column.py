# Count occurrences of elements in a pandas Data Frame
import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish Samarth//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

print('-------------------------------------------------------------')
print('Original Dataframe: ')
print(_my_df)
print('-------------------------------------------------------------')
print()

# To get the occurence of a value in a column
# use grouby() with size()
print('Count value of occurence by value: ')
print(_my_df.groupby(['Sex']).size())
print('-------------------------------------------------------------')
print()

# To get the occurence of a value in a column
# use grouby() with size()
_my_df_Series=_my_df.groupby(['Sex']).size()
print('Count value of occurence by value: ')
print(_my_df_Series, type(_my_df_Series))

# Output
'''
-------------------------------------------------------------
Original Dataframe: 
    Name         Sex  Age  Height (in)  Weight (lbs)
0   Alex         "M"   41           74           170
1   Bert         "M"   42           68           166
2   Carl         "M"   32           70           155
3   Dave         "M"   39           72           167
4   Elly         "F"   30           66           124
5   Fran         "F"   33           66           115
6   Gwen         "F"   26           64           121
7   Hank         "M"   30           71           158
8   Ivan         "M"   53           72           175
9   Jake         "M"   32           69           143
10  Kate         "F"   47           69           139
11  Luke         "M"   34           72           163
12  Myra         "F"   23           62            98
13  Neil         "M"   36           75           160
14  Omar         "M"   38           70           145
15  Page         "F"   31           67           135
16  Quin         "M"   29           71           176
17  Ruth         "F"   28           65           131
-------------------------------------------------------------

Count value of occurence by value: 
Sex
       "F"     7
       "M"    11
dtype: int64
-------------------------------------------------------------

Count value of occurence by value: 
Sex
       "F"     7
       "M"    11
dtype: int64 <class 'pandas.core.series.Series'>
'''