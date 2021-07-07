###################################################################################

# inverse of a matrix using NumPy
# The inverse of a matrix is that matrix which when multiplied with the original matrix 
# will give as an identity matrix. The inverse of a matrix exists only if 
# the matrix is non-singular i.e., determinant should not be 0. 


# The inverse of any square matrix with the function numpy.linalg.inv(array). 
# Syntax: numpy.linalg.inv(a)
# Parameters:-
# a: Matrix to be inverted
# Returns: Inverse of the matrix a.


# Importing Library
# import numpy as np
  
# # Finding an inverse of given array
# arr = np.array([[1, 2], [5, 6]])
# inverse_array = np.linalg.inv(arr)
# print("Inverse array is ")
# print(inverse_array)
# print()

###################################################################################

# inverse of 3X3 matrix
# arr = np.array([[1, 2, 3], 
#                 [4, 9, 6], 
#                 [7, 8, 9]])
  
# inverse_array = np.linalg.inv(arr)
# print("Inverse array is ")
# print(inverse_array)
# print()

###################################################################################

# inverse of 4X4 matrix
# arr = np.array([[1, 2, 3, 4], 
#                 [10, 11, 14, 25],
#                 [20, 8, 7, 55], 
#                 [40, 41, 42, 43]])
  
# inverse_array = np.linalg.inv(arr)
# print("Inverse array is ")
# print(inverse_array)
# print()

###################################################################################

# inverse of 1X1 matrix
# arr = np.array([[1]])
# inverse_array = np.linalg.inv(arr)
# print("Inverse array is ")
# print(inverse_array)

###################################################################################
###################################################################################