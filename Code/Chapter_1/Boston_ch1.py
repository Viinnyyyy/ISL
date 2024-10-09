import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots
# import statistics as st

Boston3 = pd.read_csv(
    '/Users/mac/Documents/ISL_with_Python/ISL/ALL_CSV_FILES/Boston.csv')
Boston3.head()

# Superfacial inspection of the dataset to confirm file integrity
Boston3.describe(), Boston3.isna().sum(), Boston3.columns, Boston3.sum()
Boston3.shape  # This is a dataset with 504 rows and 14 columns
Boston3.isnull().sum()
Boston3.dtypes

# ['Boston', 'crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'lstat', 'medv']

# crim: per capita crime rate by town.
# zn: proportion of residential land zoned for lots over 25,000 sq.ft.
# indus: proportion of non-retail business acres per town.
# chas: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
# nox: nitrogen oxides concentration (parts per 10 million).
# rm: average number of rooms per dwelling.
# age: proportion of owner-occupied units built prior to 1940.
# dis: weighted mean of distances to five Boston employment centres.
# rad: index of accessibility to radial highways.
# tax: full-value property-tax rate per $10,000.
# ptratio: pupil-teacher ratio by town.
# lstat: lower status of the population (percent).
# medv: median value of owner-occupied homes in $1000s.

np.unique(Boston3['indus'])
# Straighaway, I see an unnamed column. Technically, it is a columnn named 'Unnamed : 0'
# Renaming the column to Boston

Boston2 = Boston3.rename({'Unnamed: 0': 'Boston'}, axis=1)
Boston2.set_index('Boston')
Boston2.head()

# Scatterplot to show relationship and trend among the columns
pd.plotting.scatter_matrix(Boston2[['crim', 'zn', 'indus', 'chas', 'nox']])
pd.plotting.scatter_matrix(Boston2[['crim', 'rm', 'age', 'dis', 'rad']])
pd.plotting.scatter_matrix(
    Boston2[['crim', 'tax', 'ptratio', 'lstat', 'medv']])
plt.show()


# There is a sharp increase of crime rate with tax=600 and the pupil-teacher ratio being 20.48.
# With a population of people that had their houses valued at $1000 medv, there is a subtle decline in the crime
# There is a slight increase with the age
# There is a decline with the distance to the
# Crime raye shots up when there is a rad of 24
#
# Then again, when you look at it, the overall crime data is heavily left skewed as there are a lot
# of low crime rate places and very few increased crime rate with a maximum of 88.97
#
# When there is no zn, there is an increased crime rate that dissipates immediately after.
#
# There is increased crimerate where there is no charles river.

# Crimerate count around the charles river
Boston2.chas[Boston2['chas'] == 0].value_counts()
Boston2.chas[Boston2['chas'] == 0]
# takes about 470 of the 505 datasets.


# select the rows that has the maximum crime, ptratio and tax rates
Boston2[Boston2.crim == Boston2.crim.max()]
Boston2[Boston2.ptratio == Boston2.ptratio.max()]
Boston2[Boston2.tax == Boston2.tax.max()]

# select the rows that has the minimum crime, ptratio and tax rates
Boston2[Boston2.crim == Boston2.crim.min()]
Boston2[Boston2.ptratio == Boston2.ptratio.min()]
Boston2[Boston2.tax == Boston2.tax.min()]

Boston2.medv.min()
Boston2.columns[Boston2['medv'].min()]
Boston2.columns(Boston2.isin(Boston2.medv.min()).any())
Boston2.head()

Boston2.ptratio.median()  # the median pupil-teacher ratio was 19:1

# select the columns that has the minimum medv
Boston2[Boston2.medv == Boston2.medv.min()]
Boston2[Boston2.crim == Boston2.crim.min()]
Boston2[Boston2.medv == Boston2.medv.max()]
Boston2[Boston2.crim == Boston2.crim.min()]
Boston2[Boston2.medv == Boston2.medv.median()]
Boston2[Boston2.crim == Boston2.crim.min()]

#  The lowest medv has a high crime rate and the column with the row with the lowest crime rate
#  has a high medv. The highest medv from the dataset has the indus and tax column directly
#  reducing the crime rate.
#  zn also plays a role too as an increase in zn leads to reduced crime rate.
#
# select the columns that has the minimum medv and compare it to the maximum crime rate
Boston2[Boston2.medv == Boston2.medv.min()]
Boston2[Boston2.crim == Boston2.crim.max()]
Boston2[Boston2.medv == Boston2.medv.max()]
Boston2[Boston2.crim == Boston2.crim.max()]
Boston2[Boston2.medv == Boston2.medv.median()]
Boston2[Boston2.crim == Boston2.crim.max()]


# Finding the rows that have rooms of 7

Boston2[Boston2.rm >= 7]
Boston2.crim[Boston2.rm >= 7].min()
# Finding the rows that have rooms of 8

Boston2[Boston2.rm >= 8]
Boston2.crim[Boston2.rm >= 8].unique()
# The rooms do not seem to give any form of information concerning the workings of the crime rate
