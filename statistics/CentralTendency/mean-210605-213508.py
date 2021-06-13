# Central Value
# When you have two or more numbers it is nice to find a value for the "center".


# Example: what is the central value for 3 and 7?
# (3+7) / 2 = 10/2 = 5




# Example: what is the central value of 3, 7 and 8?
# Answer: We calculate it by adding 3, 7 and 8 and then dividing the results by 3 
# (because there are 3 numbers):(3+7+8) / 3 = 18/3 = 6




# The Mean
# How to find the mean
# The mean is the average of the numbers.
# Add up all the numbers, then divide by how many numbers there are.


# Example 1: What is the Mean of these numbers? 6, 11, 7




# Example 2: Look at these numbers:
# 3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29




# Example 3: Find the mean of these numbers:
# 3, −7, 5, 13, −2




# Example: Birthday Activities
# Uncle Bob wants to know the average age at the party, to choose an activity.
# There will be 6 kids aged 13, and also 5 babies aged 1.




# What is the mean of the numbers 8, 9, 13 and 18?




# Sam scored the following grades in his end of year exams: What was his mean grade?
# Math: 51%, Eng:62%, Sci:70%, Geo: 39%, Hist:81%, Eco:57%




# A booklet has 12 pages with the following numbers of words: 
# 271, 354, 296, 301, 333, 326, 285, 298, 327, 316, 287 and 314.
# What is the mean number of words per page?




# What is the mean of these numbers: 12, -1, 8, 2, -10, 0, -5, 3, 20, -2




# The mean of 15 numbers is 12. An extra number is included and the mean increases to 13. 
# What is the extra number? The mean of 15 numbers = 12 ⇒ The total of 15 numbers = 15 × 12 = 180



# The average mark scored by 29 students in a science test was 56%. 
# John was sick, so sat the test late and scored 71%. 
# Including John's, what was the new value of the mean mark?






# Importing the statistics module
# import numbers
# import statistics
# # list of positive integer numbers
# data = [1, 3, 4, 5, 7, 9, 2]
# x = statistics.mean(data)
# # Printing the mean
# print("Mean is :", x)





# Python program to demonstrate mean()
# from statistics import mean
# from fractions import Fraction as fr

# # tuple of positive numbers
# data1 = (11, 3, 4, 5, 7, 9, 2)

# # tuple of negative numbers
# data2 = (-1, -2, -4, -7, -19, -12)

# # tuple of mixed range numbers
# data3 = (-1, 3,- 4, 55, -27, 19, 2)

# # tuple of fractional numbers
# data4 = (fr(1,2), fr(44,12), fr(10,3), fr(2,3))

# # dictionary of set of values
# data5 = {1:'one', 2:'two', 3:'three'}

# print('Mean of positive numbers:', round(mean(data1),2))
# print('Mean of negative numbers:', mean(data2))
# print('Mean of mixed range numbers:', mean(data3))
# print('Mean of fractional numbers:', mean(data4))
# print('Mean of dictionary:', mean(data5))





# TypeError
# from statistics import mean
# data = {'one':1, 'two':2, 'three':3}
# print(mean(data))





# Mean in numpy()
# pip install numpy
# import numpy

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = numpy.mean(speed)

# print(x)

