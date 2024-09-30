import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots

Auto_nan = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ISL/ALL_CSV_FILES/Auto.csv")
Auto_nan.head()
Auto_nan.isna().count()

np.unique(Auto_nan['horsepower']).sum()  # this shows the '?' in the data
Auto_nan.isna().sum()  # there is no na data here. Then why am I seeing a '?' there?

Auto_nan.sum()  # The 'horsepower' column is adding all the characters and it seems not to be a number
Auto_nan.dtypes  # horsepower is definitely an object class

# Converts the column to integer after changing '?' to Nan and removing it
