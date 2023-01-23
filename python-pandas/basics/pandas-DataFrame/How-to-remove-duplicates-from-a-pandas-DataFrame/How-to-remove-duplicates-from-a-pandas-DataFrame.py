# Drop Duplicates using drop_duplicates() method

import pandas as pd
_my_df = pd.read_csv('C://Users//Ashish Samarth//jupyter-notebook//Training//python-modules//pandas//biostats.csv')

print(f'my_df_has_duplicates: \n {_my_df} \n {_my_df.shape}')
print('-------------------------------------------------------------')
print()
print('-------------------------------------------------------------')
print(f'Dropping Duplicates: \n {_my_df.drop_duplicates()} \n {(_my_df.drop_duplicates()).shape}')

