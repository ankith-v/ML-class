# The Median
# The Median is the "middle" of a sorted list of numbers.
# 10 11 13 15 16 23 26  ---- middle number is 15




# How to Find the Median Value:
# To find the Median, place the numbers in value order and find the middle
# Ex: Find the median of 12, 3, 5
# Put them in order: 3, 5, 12
# the middle is 5, so median is 5




# Example: 3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29
# When we put those numbers in order we have:
# 3, 5, 7, 12, 13, 14, 21, 23, 23, 23, 23, 29, 39, 40, 56




# Two Numbers in the Middle
# In that case we find the middle pair of numbers, and then find the value that 
# is halfway between them. This is easily done by adding them together and dividing by two.


# Example: 3, 13, 7, 5, 21, 23, 23, 40, 23, 14, 12, 56, 23, 29
# When we put those numbers in order we have:

# 3, 5, 7, 12, 13, 14, 21, 23, 23, 23, 23, 29, 40, 56
# In this example the middle numbers are 21 and 23.

# To find the value halfway between them, add them together and divide by 2:
# 21 + 23 = 44
# then 44 ÷ 2 = 22
# So the Median in this example is 22.




# Example: There are 45 numbers
# 45 plus 1 is 46, then divide by 2 and we get 23
# So the median is the 23rd number in the sorted list.




# Example: There are 66 numbers
# 66 plus 1 is 67, then divide by 2 and we get 33.5
# 33 and a half? That means that the 33rd and 34th numbers in the sorted list are the two middle numbers.
# So to find the median: add the 33rd and 34th numbers together and divide by 2.




# What is the median of the numbers 4, 2, 11, 6, 2 ?




# What is the median of the numbers 3, 11, 6, 5, 4, 7, 12, 3 and 10 




# What is the median of the numbers 4, 2, 11, 6, 2, 9 ?




# What is the median of the numbers 75, 83, 69, 56, 71, 80, 65, 67, 77 and 44 ?
# Put the numbers in order first: 44, 56, 65, 67, 69, 71, 75, 77, 80, 83




# A booklet has 12 pages with the following numbers of words:  
# 271, 354, 296, 301, 333, 326, 285, 298, 327, 316, 287 and 314. 
# What is the median number of words per page?
# 271,285,287,296,298,301,314,316,326,327,333,354




# What is the median of the squares of the first ten natural numbers?
# 1,4,9,16,25,36,49,64,81,100




# What is the median of the first eleven prime numbers?
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31




# π = 3.141592653589793238462643383...
# What is the median of the first 12 digits of π?
# ordered - 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 8, 9





# median()
# import statistics
# data = [2, -2, 3, 6, 9, 4, 5, -1]
# print("Median of data is:", statistics.median(data))


# print(sorted(data))


# from statistics import median
# data = []
# print("Median of data is:", median(data))





# Median in numpy()
# import numpy

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = numpy.median(speed)

# print(x)

