import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots

Boston3 = pd.read_csv('ALL_CSV_FILES/Boston.csv')
Boston3.head()

# Superfacial inspection of the dataset to confirm file integrity
Boston3.describe(), Boston3.isna().sum(), Boston3.columns, Boston3.sum()
Boston3.shape  # This is a dataset with 504 rows and 14 columns
Boston3.isnull().sum()
Boston3.dtypes

# ['Boston', 'crim', 'zn', 'indu s', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'lstat', 'medv']

np.unique(Boston3['indus'])
# Straighaway, I see an unnamed column. Technically, it is a columnn named 'Unnamed : 0'
# Renaming the column to Boston

Boston2 = Boston3.rename({'Unnamed: 0': 'Boston'}, axis=1)
Boston2 = Boston2.set_index('Boston')
Boston2.head()

# Scatterplot to show relationship and trend among the columns
pd.plotting.scatter_matrix(Boston2[['crim', 'zn', 'indu s', 'chas', 'nox']])
pd.plotting.scatter_matrix(Boston2[['crim', 'rm', 'age', 'dis', 'rad']])
pd.plotting.scatter_matrix(
    Boston2[['crim', 'tax', 'ptratio', 'lstat', 'medv']])
plt.show()


# There is a sharp increase of crime rate with tax=600 and the pupil-teacher ratio being 20.48.
# With medv, there is a subtle decline in the crim
# There is a slight increase with the age
# There is a decline with the dis
# Crime raye shots up when there is a rad of 24
#
# Then again, when you look at it, the overall crime data is heavily left skewed as there are a lot
# of low crime rate places and very few increased crime rate with a maximum of 88.97
