# How far, on average, all values are from the middle



# In three steps:
# 1. Find the mean of all values
# 2. Find the distance of each value from that mean (subtract the mean from each value, ignore minus signs)
# 3. Then find the mean of those distances





# Example: the Mean Deviation of 3, 6, 6, 7, 8, 11, 15, 16
# Step 1: Find the mean:
# Mean =   (3 + 6 + 6 + 7 + 8 + 11 + 15 + 16) / 8   =   72/8   = 9

# Step 2: Find the distance of each value from that mean:
# Value	Distance from 9
#     3	    6
#     6   	3
#     6	    3
#     7	    2
#     8	    1
#     11	2
#     15	6
#     16	7

# Step 3. Find the mean of those distances:
# Mean Deviation =   (6 + 3 + 3 + 2 + 1 + 2 + 6 + 7) / 8   =   30/8   = 3.75


# So, the mean = 9, and the mean deviation = 3.75





# Formula:
# Mean Deviation =  Σ|x − μ| / N



# Example1: the Mean Deviation of 3, 6, 6, 7, 8, 11, 15, 16
# Step 1: Find the mean
# Step 2: Find the Absolute Deviations
#   x     |x − μ|
# Step 3. Find the Mean Deviation





# Example2: You and your friends have just measured the heights of your dogs (in millimeters)
# x = 600,470,170,430,300
# mean = 1970 / 5 = 394
# distance : 206 + 76 + 224 + 36 + 94









# from statistics import mean

# # # my_list = [7, 5, 1, 2, 10, 3]
# my_list = [600,470,170,430,300]
# # my_list = [3, 6, 6, 7, 8, 11, 15, 16]
# print("Original list:", my_list)
# res = []
# # getting mean
# mean_val = mean(my_list)

# for el in my_list:
#     # getting deviation
#     res.append(abs(el - mean_val))

# print("Mean deviation:", mean(res))





# from numpy import mean, abs

# my_list = [3, 6, 6, 7, 8, 11, 15, 16]
# res = mean(abs(my_list - mean(my_list)))
# print("Mean deviation:", res)
