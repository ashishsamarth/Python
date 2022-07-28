# Method to add a delimiter as suffix
# Note:- This was added for understanding, however their are pre-built functions in pandas for this task
def suffix_delim(self, _tgt_col_name, _delim):
    self.my_df[_tgt_col_name] = self.my_df[_tgt_col_name].astype(str) + _delim