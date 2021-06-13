# Harmonic Mean (also known as Contrary mean) is one of several kinds of average 
# and in particular one of the Pythagorean means. Usually used in situations 
# when average rates are desired.


# The harmonic mean is:the reciprocal of the average of the reciprocals: 
# To get the reciprocal of a number, we divide 1 by the number.




# HM = n / (1/a) + (1/b) + (1/c) + .....



# Example: What is the harmonic mean of 1, 2 and 4?
# The reciprocals of 1, 2 and 4 are:
# 1/1  = 1,    1/2  = 0.5,    1/4  = 0.25

# Now add them up:
# 1 + 0.5 + 0.25 = 1.75

# Divide by how many:
# Average =  1.75/3

# The reciprocal of that average is our answer:
# Harmonic Mean =  3/1.75  = 1.714 (to 3 places)





# example of calculating the harmonic mean
# from scipy.stats import hmean

# # define the dataset
# data = [0.11, 0.22, 0.33, 0.44, 0.55, 0.66, 0.77, 0.88, 0.99]

# # calculate the mean
# result = hmean(data)

# # print('Harmonic Mean: %.3f' % result)
# print('Harmonic Mean:', result)






# working of harmonic_mean() function

# Import statistics module
# import statistics

# # list of positive real valued numbers
# data = [1, 3, 5, 7, 9]
# # data = [0.11, 0.22, 0.33, 0.44, 0.55, 0.66, 0.77, 0.88, 0.99]

# # using harmonic mean function to calculate
# print("Harmonic Mean is % s " % (statistics.harmonic_mean(data)))

