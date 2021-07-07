###############################################################

# Grouping Pandas
# Pandas dataframe.groupby() function is used to split the data into groups based on some criteria. 
# pandas objects can be split on any of their axes. 
# The abstract definition of grouping is to provide a mapping of labels to group names.

# Use groupby() function to group the data based on the “Team”.

# importing pandas as pd
# import pandas as pd
  
# # Creating the dataframe 
# df = pd.read_csv("nba.csv")
# # Print the dataframe
# print(df)

##############################################################

# Now apply the groupby() function.

# import pandas as pd
  
# df = pd.read_csv("nba.csv")
# # group the data on team value.
# g = df.groupby('Team')
  
# # Let's print the first entries in all the groups formed.
# print(g.first())


# Finding the values contained in the "Boston Celtics" group
# boston = g.get_group('Boston Celtics')
# print(boston)

##############################################################

# Use groupby() function to form groups based on more than one category

# importing pandas as pd
# import pandas as pd

# # Creating the dataframe
# df = pd.read_csv("nba.csv")

# # First grouping based on "Team"
# # Within each team we are grouping based on "Position"
# g = df.groupby(['Team', 'Position'])

# # Print the first value in each group
# print(g.first())

##############################################################
##############################################################

# Pivoting Pandas
# pandas.pivot(index, columns, values) function produces pivot table based on 3 columns 
# of the DataFrame. Uses unique values from index / columns and fills with values.

# Create a simple dataframe
# importing pandas as pd
# import pandas as pd

# # creating a dataframe
# df = pd.DataFrame({'A': ['John', 'Boby', 'Mina'],
# 	'B': ['Masters', 'Graduate', 'Graduate'],
# 	'C': [27, 23, 21]})

# print(df)


# ##############################################################

# # values can be an object or a list
# dfp1 = df.pivot('A', 'B', 'C')      # pandas.pivot(index, columns, values)
# print(dfp1)

# ##############################################################

# # value is a list
# dfp2 = df.pivot(index ='A', columns ='B', values =['C', 'A'])
# print(dfp2)

##############################################################

# Raise ValueError when there are any index, columns combinations with multiple values.
# importing pandas as pd
# import pandas as pd

# # creating a dataframe
# df = pd.DataFrame({'A': ['John', 'John', 'Mina'],
# 	'B': ['Masters', 'Masters', 'Graduate'],
# 	'C': [27, 23, 21]})


# df.pivot('A', 'B', 'C')

##############################################################
##############################################################