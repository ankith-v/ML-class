###################################################################################

# Python | Numpy np.eigvals() method
# With the help of np.eigvals() method, we can get the eigen values of a matrix by using np.eigvals() method.

# Syntax : np.eigvals(matrix)
# Return : Return the eigen values of a matrix.

# # import numpy
# from numpy import linalg as LA

# # using np.eigvals() method
# eigen = LA.eigvals([[1, 2], [3, 4]])
# print(eigen)

###############################################

# import numpy
# from numpy import linalg as LA

# # using np.eigvals() method
# eigen = LA.eigvals([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(eigen)


###################################################################################


# eigenvalues and right eigenvectors
# importing numpy library
# import numpy as np
  
# # create numpy 2d-array
# m = np.array([[1, 2],
#               [2, 3]])
  
# print("Printing the Original square array:\n", m)
  
# # finding eigenvalues and eigenvectors
# w, v = np.linalg.eig(m)
  
# # printing eigen values
# print("Printing the Eigen values of the given square array:\n", w)
  
# # printing eigen vectors
# print("Printing Right eigenvectors of the given square array:\n", v)


###################################################################################

  
# # create numpy 3d-array
# import numpy as np

# m = np.array([[1, 2, 3],
#               [2, 3, 4],
#               [4, 5, 6]])
  
# print("Printing the Original square array:\n",
#       m)
  
# # finding eigenvalues and eigenvectors
# w, v = np.linalg.eig(m)
  
# # printing eigen values
# print("Printing the Eigen values of the given square array:\n", w)
  
# # printing eigen vectors
# print("Printing Right eigenvectors of the given square array:\n", v)


###################################################################################
###################################################################################