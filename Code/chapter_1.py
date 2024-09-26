# import ISLP
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import subplots
# import numpy as np
import pandas as pd

df2 = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ALL_CSV_FILES/College.csv")
df3 = df2.rename({'Unnamed: 0': 'College'}, axis=1)
df3 = df3.set_index('College')
df = df3
df.head()


df.dtypes  # output shows that Private is a string instead of Boolean
