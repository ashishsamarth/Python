import pandas as pd
# Method to create dataframe with based on multiple and conditions
# argument: _col_names should preferably be a list
# argument: _conditions should preferably be a list
# It has to be a 1:1 mapping of _col_name and condition and is sequence sensitive
# Do not convert is to a static method
def create_df_from_filtered_data_multiple_and_conditions(self, _col_names, _conditions):
    try:
        if len(_col_names) == len(_conditions):
            _filter_con = []
            for _idx in range(len(_col_names)):
                _filter_con.append('(self.my_df[\'' + _col_names[_idx] + '\'] == \'' + _conditions[_idx] + '\')')
            delta = '(self.my_df.loc[' + ' & '.join(_ for _ in _filter_con) + '])'
            _filtered_data_set = eval(delta)
            return pd.DataFrame(_filtered_data_set)
    except:
        print("Unexpected-Condition-In-Method")