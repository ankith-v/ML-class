###########################################################################
# The term broadcasting refers to how numpy treats arrays with different Dimension 
# during arithmetic operations which lead to certain constraints, 
# the smaller array is broadcast across the larger array so that they have compatible shapes. 

# import numpy as np
 
# A = np.array([5, 7, 3, 1])
# B = np.array([90, 50, 0, 30])
 
# # array are compatible because of same Dimension
# c = A * B
# print (c)



###########################################################################

# import numpy as np
# a = np.array([17, 11, 19]) # 1x3 Dimension array
# print(a)
# b = 3
# print(b)

# # Broadcasting happened because of
# # miss match in array Dimension.
# c = a + b
# print(c)



# ###########################################################################

# import numpy as np
# A = np.array([[11, 22, 33], [10, 20, 30]])
# print(A)

# b = 4
# print(b)

# C = A + b
# print(C)



###########################################################################
