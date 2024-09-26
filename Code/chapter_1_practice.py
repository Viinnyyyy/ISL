# Modules to be installed

from matplotlib.pyplot import subplots
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Using numpy
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

x + y

x = np.array([[1, 2], [3, 4]])
x.ndim
x.dtype

np.array([['a', 2], [3, 4]]).dtype

np.array

# Reshaping lists into a 2 by 3 matrix
x = np.array([1, 2, 3, 4, 5, 6])
print('beginning x:\n', x)
x_reshape = x.reshape((2, 3))
print('reshaped x:\n', x_reshape)


# Changing and modifying lists
print('x_reshape before we modify x_reshape:\n', x_reshape)
x_reshape[0, 0] = 5
print('x_reshape after we modify its top left element:\n', x_reshape)
print('x after we modify top left element of x_reshape:\n', x)


# Tuples are immutable
my_tuple = (1, 2, 3)
my_tuple[0] = 2  # Gives an error when ran


# Random generator that changes anytime it is run
print(np.random.normal(size=50))

# Random using a default_rng to promote repeatability
rng = np.random.default_rng(1999)
print(rng.normal(scale=10, size=2))
rng2 = np.random.default_rng(1999)
print(rng2.normal(scale=10, size=2))

# compute mean, std and variance with numpy

rng = np.random.default_rng(3)
y = rng.standard_normal(10)

# mean
np.mean(y), y.mean()  # both modes work well to give the same output

# variance
np.var(y), y.var(), np.mean((y - y.mean()) ** 2)

# standard deviation
np.sqrt(np.var(y)), np.std(y)

# creating a 10 x 3 matrix of random numbers
X = rng.standard_normal((10, 3))
X

X.mean(axis=0), X.mean(0)  # the same output

# %% [markdown]
# VISUALS AND GRAPHICS

# %matplotlib inline  # to plot inline
fig, ax = subplots(figsize=(8, 8))
a = rng.standard_normal(100)
b = rng.standard_normal(100)
ax.plot(a, b)
plt.show()  # shows plot

# A slightly expanded form of fig, ax = subplots(figsize=(8, 8))

output = subplots(figsize=(8, 8))
fig = output[0]
ax = output[1]

# Plotting with matplotlib to create plots
fig, ax = subplots(figsize=(8, 8))
ax.plot(a, b, 'o')

# plotting a scatterplot with the same dataset
fig, ax = subplots(figsize=(8, 8))
ax.scatter(a, b, marker='o')
plt.show()

fig, ax = subplots(figsize=(8, 8))
ax.scatterplot(x, y, marker='o')
ax.set_xlabel("This is the x-axis")
ax.set_ylabel("This is the y-axis")
ax.set_title("Plot of X against Y")
fig.set_size_inches(12, 3)
fig
plt.show()

fig, axes = subplots(nrows=2, ncols=3, figsize=(15, 5))

axes[0, 1].plot(x, y, 'o')
axes[1, 2].scatter(x, y, marker='+')
fig


seq1 = np.linspace(0, 10, 11)
seq1

"Hello World"[3:6]
"Hello World"[slice(3, 6)]

A = np.array(np.arange(16)).reshape((4, 4))
A
A[1, 2]  # RC format [row, column]

# code  1
A[[1, 3]]  # retrieves the second and fourth rows
#  this still boils down to the RC format above
#  So to retrieve columns,

#  code 2
A[:, [1, 3]]  # this retrives the second and fourth columns
#  x[[sr:er], [sc: ec]]
#  sr --> start row, er --> end row, sc --> start column, ec --> end compile

#  To select the 2nd and 4th row and column as a subset
#  we select the 2nd and 4th row as normal then subset the 2nd and 4th column
#  Almost like we combine code 1 and 2 in tandem

A[[1, 3]][:, [1, 3]]

# Going through this stress is all but unnecessary most times. Why?
# Numpy saves our asses with the .ix_ filter

idx = np.ix_([1, 3], [1, 3])
A[idx]  # gives the same output. Not necessarily faster.

# Check the n-order time of the following


# Boolean indexing

keepRows = np.zeros(A.shape[0], bool)
keepRows

keepRows[[1, 3]] = True
keepRows

# to confirm that this is the same as 1, 0 matrix,

np.all(keepRows == np.array([0, 1, 0, 1]))

# Although the np.all() code and the np.zero() code read same boolean output
# numpy treats them differently as will be seen in the codes below

A[np.array([0, 1, 0, 1])]
#  array([[0, 1, 2, 3],
#      [4, 5, 6, 7],
#      [0, 1, 2, 3],
#      [4, 5, 6, 7]])

A[keepRows]
# array([[ 4,  5,  6,  7],
#      [12, 13, 14, 15]])

keepColumns = np.zeros(A.shape[1], bool)
keepColumns[[0, 2, 3]] = True
idx_col = np.ix_(keepRows, keepColumns)
A[idx_col]


idx_mixed = np.ix_([1, 3], keepColumns)
A[idx_mixed]


# LOADING IN DATA

Auto = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ALL_CSV_FILES/Auto.csv")
Auto.head()


Auto2 = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ALL_CSV_FILES/Auto.data", sep='\\s+')
Auto2

Auto["horsepower"]
# we can see that the dtype of the horsepower column is objects instead of integer
np.unique(Auto["horsepower"])
# The last value is seen as '?' which signifies a nan and can produce a string dtype
# the output of .sum() appends all the numbers together as a though a string
Auto["horsepower"].sum()

# to eliminate the nan, we do the following
Auto_nonan = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ALL_CSV_FILES/Auto.data", na_values=['?'], sep='\\s+')
Auto_nonan["horsepower"].sum()

Auto2.shape, Auto.shape, Auto_nonan.shape  # all show a shape of (397, 9)

# Dropping na values
Auto_new = Auto_nonan.dropna()
# This new shape with the dropped na's gives a shape of (392, 9) showing there were 5 na values
Auto_new.shape

Auto = Auto_new  # replaces Auto_new with Auto

# Using rows and columns
Auto.columns  # prints the columns of the Auto dataset

Auto["horsepower"].dtype  # confirms that the horsepower column is numbers only

Auto[:3]
Auto[Auto["year"] > 80]
Auto[['mpg', 'horsepower']]
Auto.index  # We can see that the index is numbered from 0 to 396 giving us 397 although we actually have 392 rows
# We can see that there are skipped files because we dropped na values
#
# Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,
# 9,
#        ...
#        387, 388, 389, 390, 391, 392, 393, 394, 395, 39
# 6],
#       dtype='int64', length=392)

Auto_re = Auto.set_index('name')
Auto_re

Auto_re.columns  # we can see the index is now name
Auto_re.shape  # now, the name column is removed as it is an index

Auto_re.loc[['amc rebel sst', 'ford torino']]  # loc uses the name
Auto_re.iloc[[3, 4]]  # selects the rows
Auto_re.iloc[:, [0, 2, 3]]  # selects the columns
Auto_re.iloc[[3, 4], [0, 2, 3]]  # selects both rows and columns

Auto_re.loc['ford galaxie 500', ['mpg', 'origin']]


#  get the time cost between these two codes
Auto_re.loc[Auto_re['year'] > 80, ['weight', 'origin']]
# Is a lambda function faster and more concise/
Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']]

Auto_re.loc[lambda df: (df['year'] > 80) & (
    df['mpg'] > 30), ['weight', 'origin']]

Auto_re.loc[lambda df: (df['displacement'] > 300) & (df.index.str.contains(
    'ford') | df.index.str.contains('datsun')), ['weight', 'origin']]

# Using for loop
total = 0
for key in [3, 2, 19]:
    total += key

# print(f'Total is {total}')
# print('Total is :'.total)

print(f'Total is: {total}')

total = 0
for value in [2, 3, 19]:
    for weight in [3, 2, 1]:
        total += value * weight

print(f'Total is {total}')

total = 0
for value, weight in zip([2, 3, 19], [0.2, 0.3, 0.5]):
    total += weight * value

print(f'Weighted average is {total}')

# String Formatting
rng = np.random.default_rng(1)
A = rng.standard_normal((127, 5))
M = rng.choice([0, np.nan], p=[0.8, 0.2], size=A.shape)
A += M
D = pd.DataFrame(A, columns=['food', 'bar', 'pickle', 'snack', 'popcorn'])
D[:3]

for col in D.columns:
    template = f'Column "{col}" has {
        (np.isnan(D[col]).mean()): .2%} missing values'
    print(template)

#  Using matplotlib to properly display plots using the Auto dataset
fig, ax = subplots(figsize=(8, 8))
ax.plot(Auto['horsepower'], Auto['mpg'], 'o')
plt.show()  # A downward trend can be observed in the dataset

fig, axes = subplots(ncols=3, figsize=(15, 5))
Auto.plot.scatter('horsepower', 'mpg', ax=axes[1])
plt.show()

Auto.cylinders = pd.Series(Auto.cylinders, dtype='category')
Auto.cylinders.dtype

fig, ax = subplots(figsize=(8, 8))
Auto.boxplot('mpg', by='cylinders', ax=ax)
plt.show()


fig, ax = subplots(figsize=(8, 8))
Auto.hist('mpg', color='red', bins=12, ax=ax)
plt.show()

pd.plotting.scatter_matrix(Auto)
plt.show()

pd.plotting.scatter_matrix(Auto[['mpg', 'displacement', 'weight']])
plt.show()

Auto[['mpg', 'displacement', 'weight']].describe()

Auto['cylinders'].describe()
Auto['mpg'].describe()
