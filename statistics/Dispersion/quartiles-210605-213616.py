# Quartiles are the values that divide a list of numbers into quarters


# How to find 
# Put the list of numbers in order
# Then cut the list into four equal parts
# The Quartiles are at the "cuts“





# 9
# Example: 5,7,4,4,6,2,8
# Put them in order: 2,4,4,5,6,7,8
# cut the list into quarters:


# Result:
# Quartile 1 (Q1): 4
# Quartile 2 (Q2) which is also the Median: 5
# Quartile 3 (Q3): 7





# Sometimes a "cut" is between two numbers. The Quartile is the average of the two numbers.

# 10
# Example: 1,3,3,4,5,6,6,7,8,8
# Numbers are already in order


# In case of quartile 2, half way between 5 and 6: Q2 = (5+6)/2 = 5.5

# Result:
# Quartile 1 (Q1): 3
# Quartile 2 (Q2) which is also the Median: 5.5
# Quartile 3 (Q3): 7






# Interquartile Range
# 11
# The "Interquartile Range" is from Q1 to Q3:



# 11a
# Example: 2,4,4,5,6,7,8

# The Interquartile Range is:
# Q3 − Q1 = 7 − 4 = 3




# 12
# What are the quartiles for the following set of numbers?
# a = [8, 11, 20, 10, 2, 17, 15, 5, 16, 15, 25, 6]
# print(sorted(a))


# 2, 5, 6,| 8, 10, 11,| 15, 15, 16, |17, 20, 25
# Q1 = 
# Q2 =
# Q3 = 





# median()
# Import the numpy library as np
# import numpy as np
# data = [32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 
#         89, 91, 92, 93, 96, 97,101, 105, 112, 116]
# # First quartile (Q1)
# Q1 = np.median(data[:10])
# # Third quartile (Q3)
# Q3 = np.median(data[10:])
# # Interquartile range (IQR)
# IQR = Q3 - Q1
# print(IQR)





# quantile()
# import numpy as np  
# # 1D array 
# arr = [20, 2, 7, 1, 34]

# print("arr : ", arr) 
# print("Q1 quantile of arr : ", np.quantile(arr, .25))
# print("Q2 quantile of arr : ", np.quantile(arr, .50))
# print("Q3 quantile of arr : ", np.quantile(arr, .75))

# IQR = np.quantile(arr, .75) - np.quantile(arr, .25)
# print(IQR)







# 15
# Box and Whisker plot 
# A Box Plot is also known as Whisker plot is created to display the summary of the set 
# of data values having properties like minimum, first quartile, median, third quartile 
# and maximum. In the box plot, a box is created from the first quartile to the 
# third quartile, a verticle line is also there which goes through the box at the median. 
# Here x-axis denotes the data to be plotted while the y-axis shows the frequency distribution




# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt


# data = [20, 2, 7, 1, 34]

# fig = plt.figure(figsize= (10,7))

# # creating plot
# plt.boxplot(data)

# # show plot
# plt.show()




