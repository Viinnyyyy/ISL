# import ISLP
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots
# import numpy as np
import pandas as pd

college2 = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ISL/ALL_CSV_FILES/College.csv")
college3 = college2.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college2.set_index('College')
college = college2
college.head()


college.dtypes  # output shows that Private is a string instead of Boolean
college.describe()

# Plotting using pandas plotting scatter matrix
fig, ax = subplots(figsize=(8, 8))
cols = ['Top10perc', 'Apps', 'Enroll']
pd.plotting.scatter_matrix(college[cols])
plt.show()

fig, ax = subplots(figsize=(8, 8))
college.boxplot('Outstate', by='Private', ax=ax)
plt.show()

college['Top10perc'].unique()
college['Elite'] = pd.cut(college['Top10perc'], [
                          0, 50, 100], labels=['No', 'Yes'])
# We are using [0, 50, 100] instead of [0, 0.5, 1]

college['Elite'].value_counts()
college['Elite']

fig, ax = subplots(figsize=(8, 8))
college.boxplot('Outstate', by='Elite', ax=ax)
plt.show()

college[['Top10perc', 'Elite']].head()


# To show
fig, ax = subplots(figsize=(8, 8))
plt.subplots(2, 2)
college.hist('Apps', color='red', bins=10, ax=ax)
plt.show()
