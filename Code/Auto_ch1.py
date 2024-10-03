import matplotlib.pyplot as plt
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
Auto_nan = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ISL/ALL_CSV_FILES/Auto.data", na_values=['?'], sep='\\s+')
Auto = Auto_nan.dropna()
Auto_nan.isna().sum()

Auto.shape, Auto_nan.shape

# It is important to note that when working with .csv files, you show the na_values as '?' as opposed
# to using the ['?'] for the .data
Auto_nan = pd.read_csv(
    "/Users/mac/Documents/ISL_with_Python/ISL/ALL_CSV_FILES/Auto.csv", na_values='?', sep=',')
Auto = Auto_nan.dropna()
Auto_nan.isna().sum()
Auto.isna().sum()
Auto.shape, Auto_nan.shape

# For qualitative predictors, we have the 'cylinders', 'year', 'origin', 'name'
# For the quantitative, the 'displacement' 'horsepower' 'weight' 'acceleration'

# The range of the quantitative datasets are found by subtracting the max from the mean value
range_displacement = np.max(
    Auto['displacement']) - np.min(Auto['displacement'])
range_horsepower = np.max(Auto['horsepower']) - np.min(Auto['horsepower'])
range_weight = np.max(Auto['weight']) - np.min(Auto['weight'])
range_acceleration = np.max(
    Auto['acceleration']) - np.min(Auto['acceleration'])

print('Displacement Range is:', range_displacement)
print('horsepower Range is:', range_horsepower)
print('weight Range is:', range_weight)
print('acceleration Range is:', range_acceleration)

# The mean of all the quantitative columns
mean_displacement = np.mean(Auto['displacement'])
mean_horsepower = np.mean(Auto['horsepower'])
mean_weight = np.mean(Auto['weight'])
mean_acceleration = np.mean(Auto['acceleration'])

print('Displacement mean is:', mean_displacement)
print('horsepower mean is:', mean_horsepower)
print('weight mean is:', mean_weight)
print('acceleration mean is:', mean_acceleration)


# The standard deviation of all the quantitative columns
std_displacement = np.std(Auto['displacement'])
std_horsepower = np.std(Auto['horsepower'])
std_weight = np.std(Auto['weight'])
std_acceleration = np.std(Auto['acceleration'])

print('Displacement std is:', std_displacement)
print('horsepower std is:', std_horsepower)
print('weight std is:', std_weight)
print('acceleration std is:', std_acceleration)


# This is to duplicate the Auto dataset sortof and to remove the 9th to the 84th column
Auto_no10_85 = Auto
Auto_no10_85.drop(Auto.index[9:84], inplace=True)
Auto_no10_85.head()
Auto_no10_85.shape

# Comparing the difference when we removed the 10th to the 85th row
range_no10_85_displacement = np.max(
    Auto_no10_85['displacement']) - np.min(Auto['displacement'])
range_no10_85_horsepower = np.max(
    Auto_no10_85['horsepower']) - np.min(Auto['horsepower'])
range_no10_85_weight = np.max(Auto_no10_85['weight']) - np.min(Auto['weight'])
range_no10_85_acceleration = np.max(
    Auto_no10_85['acceleration']) - np.min(Auto['acceleration'])

print('Displacement range_no10_85 is:', range_no10_85_displacement)
print('horsepower range_no10_85 is:', range_no10_85_horsepower)
print('weight range_no10_85 is:', range_no10_85_weight)
print('acceleration range_no10_85 is:', range_no10_85_acceleration)

# The mean of all the quantitative columns
mean_no10_85_displacement = np.mean(Auto_no10_85['displacement'])
mean_no10_85_horsepower = np.mean(Auto_no10_85['horsepower'])
mean_no10_85_weight = np.mean(Auto_no10_85['weight'])
mean_no10_85_acceleration = np.mean(Auto_no10_85['acceleration'])

print('Displacement mean_no10_85 is:', mean_no10_85_displacement)
print('horsepower mean_no10_85 is:', mean_no10_85_horsepower)
print('weight mean_no10_85 is:', mean_no10_85_weight)
print('acceleration mean_no10_85 is:', mean_no10_85_acceleration)


# The standard deviation of all the quantitative columns
std_no10_85_displacement = np.std(Auto_no10_85['displacement'])
std_no10_85_horsepower = np.std(Auto_no10_85['horsepower'])
std_no10_85_weight = np.std(Auto_no10_85['weight'])
std_no10_85_acceleration = np.std(Auto_no10_85['acceleration'])

print('Displacement std_no10_85 is:', std_no10_85_displacement)
print('horsepower std_no10_85 is:', std_no10_85_horsepower)
print('weight std_no10_85 is:', std_no10_85_weight)
print('acceleration std_no10_85 is:', std_no10_85_acceleration)

# Plots the range between the normal dataset and when the columns have been removed
fig, ax = plt.subplots()
labels = ["Normal acceleration", "No 10-85 acceleration rows", "Normal displacement", "No 10-85 displacement rows",
          "Normal horsepower", "No 10-85 horsepower rows", "Normal weight", "No 10-85 weight rows"]
columns = [range_acceleration, range_no10_85_acceleration, range_displacement, range_no10_85_displacement,
           range_horsepower, range_no10_85_horsepower, range_weight, range_no10_85_weight]
plt.bar(labels, columns)
ax.tick_params(axis='x', rotation=87)
plt.show()
plt.bar()
