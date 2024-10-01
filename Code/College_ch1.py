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
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)
ax0 = college.plot.hist(column=['Personal'])
ax1 = college.plot.hist(column=['Books'])
ax2 = college.plot.hist(column=['Outstate'])
ax3 = college.plot.hist(column=['Expend'])

fig.tight_layout()
plt.show()

# This one works finally
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)
ax0.hist(x=college['Personal'])
ax0.set_title('Histogram of Personal')

ax1.hist(x=college['Books'])
ax1.set_title('Histogram of Books')

ax2.hist(x=college['Outstate'])
ax2.set_title('Histogram of Outstate')

ax3.hist(x=college['Expend'])
ax3.set_title('Histogram of Expend')

fig.tight_layout()
plt.show()


#  Brief Summary of the dataset
#  The dataset gives an overview of the dataset and it's variables
