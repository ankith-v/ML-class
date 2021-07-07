###############################################################

# importing pandas
# import pandas
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pandas.DataFrame(mydataset)
# print(myvar)

###############################################################

# importing pandas as pd - alias
# import pandas as pd
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)

##############################################################

# check version 
# import pandas as pd
# print(pd.__version__)

##############################################################

# Series - A Pandas Series is like a column in a table.
# Create a simple Pandas Series from a list:
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)

##############################################################

# Labels - If nothing else is specified, the values are labeled with their index number.
# print(myvar[0])

##############################################################

# Create you own labels
# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)


# Return the value of "y":
# print(myvar["y"])

##############################################################

# Create a simple Pandas Series from a dictionary:
# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# Note: The keys of the dictionary become the labels.

##############################################################

# Create a Series using only data from "day1" and "day2":
# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)

##############################################################

# DataFrames - A Pandas DataFrame is a 2 dimensional data structure, 
#              like a 2 dimensional array, or a table with rows and columns
# Series is like a column, a DataFrame is the whole table.

# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# # load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df)


# Locate Row
# Return row 0:
# refer to the row index:
# print(df.loc[0])

# Return row 0 and 1:
# use a list of indexes:
# print(df.loc[[0, 1]])

# Note: When using [], the result is a Pandas DataFrame


##############################################################

# Named Indexes
# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)


# Locate Named Indexes
# Return "day2":
# refer to the named index:
# print(df.loc["day2"])

##############################################################

# Load Files Into a DataFrame
# Load a comma separated file (CSV file) into a DataFrame:
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df)


# By default, when you print a DataFrame, you will only get the first 5 rows, and the last 5 rows

# print(df.to_string())
# Tip: use to_string() to print the entire DataFrame

##############################################################

# Read JSON
# Load the JSON file into a DataFrame:
# import pandas as pd
# df = pd.read_json('data.json')
# print(df) 
# print(df.to_string())


# import pandas as pd

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)
# print(df)

##############################################################

# Pandas - Analyzing DataFrames
# Viewing the Data
# head() - The head() method returns the headers and a specified number of rows, starting from the top

# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head(10))


# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head())



# tail() - The tail() method for viewing the last rows of the DataFrame

# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.tail(10))


# Note: if the number of rows is not specified, the tail() method will return the top 5 rows.
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.tail())

##############################################################

# Info About the Data
# Print information about the data:
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.info())

##############################################################

# Null Values
# The info() method also tells us how many Non-Null values there are present in each column, 
# and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

##############################################################
##############################################################


# Pandas - Cleaning Data
# Data cleaning means fixing bad data in your data set.
# Bad data could be:
# •	Empty cells
# •	Data in wrong format
# •	Wrong data
# •	Duplicates

##############################################################

# import pandas as pd
# df = pd.read_csv('dataC.csv')
# print(df.to_string())


# The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
# The data set contains wrong format ("Date" in row 26).
# The data set contains wrong data ("Duration" in row 7).
# The data set contains duplicates (row 11 and 12).

##############################################################

# Pandas - Cleaning Empty Cells
# Empty Cells - Empty cells can potentially give you a wrong result when you analyze data.
# Remove Rows - One way to deal with empty cells is to remove rows that contain empty cells.

# Return a new Data Frame with no empty cells:
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# new_df = df.dropna()
# print(new_df.to_string())


# Remove all rows with NULL values: using inplace = True
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# df.dropna(inplace = True)
# print(df.to_string())

##############################################################

# Replace Empty Values - The fillna() method allows us to replace empty cells with a value:

# Replace NULL values with the number 130:
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# df.fillna(130, inplace = True)
# print(df.to_string())


# Replace Only For a Specified Columns
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# df["Calories"].fillna(130, inplace = True)
# print(df.to_string())



# Replace Using Mean, Median, or Mode
# Calculate the MEAN, and replace any empty values with it:
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)
# print(df.to_string())

# Calculate the MEDIAN, and replace any empty values with it:
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# x = df["Calories"].median()
# df["Calories"].fillna(x, inplace = True)
# print(df.to_string())

# Calculate the MODE, and replace any empty values with it:
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace = True)
# print(df.to_string())

##############################################################

# Pandas - Cleaning Data of Wrong Format
# row 22 and 26
# Pandas has a to_datetime() method for this

# Convert to date:
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# print(df.to_string())

# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())


# Removing Rows - we can remove the row by using the dropna() method
# df.dropna(subset=['Date'], inplace = True)
# print(df.to_string())

##############################################################

# Pandas - Fixing Wrong Data
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, 
# like if someone registered "199" instead of "1.99".
# In our data set, you can see that in row 7, the duration is 450, 
# but for all the other rows the duration is between 30 and 60.

# Set "Duration" = 45 in row 7:
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# df.loc[7, 'Duration'] = 45
# print(df.to_string())


# To replace wrong data for larger data sets you can create some rules
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 60:
#     df.loc[x, "Duration"] = 60
# print(df.to_string())


# Using numpy 
# import pandas as pd
# import numpy as np
# df = pd.read_csv('dataC.csv')
# df['Duration'] = np.where(df['Duration'] > 120, 120, df['Duration'])
# print(df.to_string())


# Removing Rows
# import pandas as pd
# df = pd.read_csv('dataC.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)
# print(df.to_string())

##############################################################

# Pandas - Removing Duplicates
# In our test data set, we can assume that row 11 and 12 are duplicates
# To discover duplicates, we can use the duplicated() method - returns a Boolean values 

# import pandas as pd
# df = pd.read_csv('dataC.csv')
# print(df.duplicated())


# Removing Duplicates - To remove duplicates, use the drop_duplicates() method

# import pandas as pd
# df = pd.read_csv('dataC.csv')
# df.drop_duplicates(inplace = True)
# print(df.to_string())

##############################################################
##############################################################



