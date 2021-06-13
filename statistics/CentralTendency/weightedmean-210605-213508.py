# A weighted mean is a kind of average. 
# Instead of each data point contributing equally to the final mean, 
# some data points contribute more “weight” than others. 
# If all the weights are equal, then the weighted mean equals the arithmetic mean 
# Weighted means are very common in statistics, especially when studying populations.




# Example:
# The numbers 1, 2, 3 and 4 have weights 0.1, 0.2, 0.3 and 0.4 respectively.
# What is the weighted mean?
# Answer: Weighted Mean
# = 0.1 × 1 + 0.2 × 2 + 0.3 × 3 + 0.4 × 4
# = 0.1 + 0.4 + 0.9 + 1.6
# = 3.0
# multiply number and weights / sum(weights)




# Example:
# The numbers 1, 2, 3, 4, 5 and 6 have weights 0.5, 0.1, 0.1, 0.1, 0.1 and 0.1 respectively.
# What is the weighted mean?
# Answer: Weighted Mean
# = 0.5 × 1 + 0.1 × 2 + 0.1 × 3 + 0.1 × 4 + 0.1 × 5 + 0.1 × 6
# = 0.5 + 0.2 + 0.3  + 0.4 + 0.5 + 0.6
# = 2.5





# The numbers 40, 45, 80, 75 and 10 have weights 1, 2, 3, 4 and 5 respectively.
# What is the weighted mean?





# The numbers 90, 35, 20, 55, 70 and 75 have weights 6, 5, 4, 2, 2 and 1 respectively.
# What is the weighted mean?







# weights = [14.424, 14.421, 14.417, 14.413, 14.41]
# values = [3058.0, 8826.0, 56705.0, 30657.0, 12984.0]
# weighted_average = sum(weight * value for weight, value in zip(weights, values)) / sum(weights)
# print(weighted_average)



# ab = zip(weights, values)
# print(list(ab))





# import numpy as np
# weights = [14.424, 14.421, 14.417, 14.413, 14.41] 
# values = [3058.0, 8826.0, 56705.0, 30657.0, 12984.0]
# weighted_avg = np.average(values, weights=weights) 
# print(weighted_avg)
