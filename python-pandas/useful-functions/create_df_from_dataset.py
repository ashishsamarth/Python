import pandas as pd
# Method to create a dataframe from a dataset
# Argument to this method is: - Dataset
def create_df_from_dataset(self, _dataset):
    # create a dataframe using the user provided dataset
    self.my_df = pd.DataFrame(_dataset)
    # return Dataframe
    return self.my_df