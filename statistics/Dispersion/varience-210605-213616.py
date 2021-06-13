# The average of the squared differences from the Mean.



# To calculate the variance follow these steps:
# 1. Work out the Mean (the simple average of the numbers)
# 2. Then for each number: subtract the Mean and square the result (the squared difference).
# 3. Then work out the average of those squared differences. 




# 30
# Find out the Mean, the Variance, and the Standard Deviation.

# Your first step is to find the Mean:  600 , 470, 170,  430, 300
# Mean	=	600+470+170+430+300 / 5 = 394 



# Second, Now we calculate each dog's difference from the Mean:
# 206, 76, -224, 36, -94
# 42436+5776+50176+1296+8836





# To calculate the Variance, take each difference, square it, and then average the result:

# Variance
# σ2	
# var =	 108520/5 = 21704
# So the Variance is 21704







# But there is a small change with Sample Data

# Our example has been for a Population (the 5 dogs are the only dogs we are interested in).

# But if the data is a Sample (a selection taken from a bigger Population), then the calculation changes!

# When you have "N" data values that are:

# The Population: divide by N when calculating Variance (like we did)
# A Sample: divide by N-1 when calculating Variance

# All other calculations stay the same, including how we calculated the mean.

# Example: if our 5 dogs are just a sample of a bigger population of dogs, we divide by 4 instead of 5 like this:

# Sample Variance = 108,520 / 4 = 27,130







# import statistics

# # sample = [600 , 470, 170,  430, 300]
# sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98]

# print("Variance:", statistics.variance(sample))





# import statistics

# # sample = [1, 1.3, 1.2, 1.9, 2.5, 2.2]
# sample = [600 , 470, 170,  430, 300]
# m = statistics.mean(sample)

# print("Variance:", statistics.variance(sample, xbar=m))
# print("Variance:", statistics.variance(sample))





# StatisticsError
# import statistics

# sample = []

# print("Variance:", statistics.variance(sample))





# Python program to demonstrate variance()
# from statistics import variance
# from fractions import Fraction as fr

# # tuple of positive numbers
# data1 = (11, 3, 4, 5, 7, 9, 2)

# # tuple of negative numbers
# data2 = (-1, -2, -4, -7, -19, -12)

# # tuple of mixed range numbers
# data3 = (-1, 3,- 4, 55, -27, 19, 2)

# # tuple of fractional numbers
# data4 = (fr(1,2), fr(44,12), fr(10,3), fr(2,3))


# print('variance of positive numbers:', variance(data1))
# print('variance of negative numbers:', variance(data2))
# print('variance of mixed range numbers:', variance(data3))
# print('variance of fractional numbers:', variance(data4))
