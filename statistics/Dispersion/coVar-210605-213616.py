# The coefficient of variation (CV) is a relative measure of variability that indicates 
# the size of a standard deviation in relation to its mean. It is a standardized, 
# unitless measure that allows you to compare variability between disparate groups and characteristics. 
# It is also known as the relative standard deviation (RSD).





# How to Calculate the Coefficient of Variation
# CV = Standard deviation / Mean 




# For example, a pizza restaurant measures its delivery time in minutes. 
# The mean delivery time is 20 minutes and the standard deviation is 5 minutes.
# CV= 5/20 = 0.25



from scipy.stats import variation 
import numpy as np
  
arr = np.random.randn(5, 5)
  
print ("array : \n", arr)
  
# rows: axis = 0, cols: axis = 1
  
print ("\nVariation at axis = 0: \n", variation(arr, axis = 0))
  
print ("\nVariation at axis = 1: \n", variation(arr, axis = 1))