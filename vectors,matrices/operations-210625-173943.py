###################################################################################

# numpy matrix operations | empty() function
# numpy.matlib.empty() is another function for doing matrix operations in numpy.
# It returns a new matrix of given shape and type, without initializing entries.

# Syntax : numpy.matlib.empty(shape, dtype=None, order=’C’)

# Parameters :
# shape : [int or tuple of int] Shape of the desired output empty matrix.
# dtype : [optional] Desired output data-type.
# order : Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.

# Return : A new matrix of given shape and type,

# importing numpy and matrix library
# import numpy
# import numpy.matlib
  
# # desired output matrix 
# out_mat = numpy.matlib.empty((2, 3)) 
# print ("Output matrix : ", out_mat) 


# # importing numpy and matrix library
# import numpy
# import numpy.matlib
  
# # desired output matrix 
# out_mat = numpy.matlib.empty((2, 3), dtype = int, order = 'C') 
# print ("Output matrix : ", out_mat) 



###################################################################################



# numpy matrix operations | zeros() function
# numpy.matlib.zeros() is another function for doing matrix operations in numpy. 
# It returns a matrix of given shape and type, filled with zeros.

# importing matrix library from numpy
# import numpy
# import numpy.matlib
  
# # desired 3 x 4 zero output matrix 
# out_mat = numpy.matlib.zeros((3, 4)) 
# print ("Output matrix : ", out_mat) 


# importing numpy and matrix library
# import numpy
# import numpy.matlib
  
# # desired 1 x 5 zero output matrix 
# out_mat = numpy.matlib.zeros(shape = 5, dtype = int) 
# print ("Output matrix : ", out_mat)



###################################################################################



# numpy matrix operations | ones() function
# numpy.matlib.ones() is another function for doing matrix operations in numpy. 
# It returns a matrix of given shape and type, filled with ones.

# importing matrix library from numpy
# import numpy
# import numpy.matlib
  
# # desired 3 x 4 output matrix 
# out_mat = numpy.matlib.ones((3, 4)) 
# print ("Output matrix : ", out_mat) 


# # importing numpy and matrix library
# import numpy 
# import numpy.matlib
  
# # desired 1 x 5 output matrix 
# out_mat = numpy.matlib.ones(shape = 5, dtype = int) 
# print ("Output matrix : ", out_mat) 



###################################################################################



# numpy matrix operations | eye() function
# numpy.matlib.eye() is another function for doing matrix operations in numpy. 
# It returns a matrix with ones on the diagonal and zeros elsewhere.
# Syntax : numpy.matlib.eye(n, M=None, k=0, dtype=’float’, order=’C’)

# Parameters :
# n : [int] Number of rows in the output matrix.
# M : [int, optional] Number of columns in the output matrix, defaults is n.
# k : [int, optional] Index of the diagonal. 0 refers to the main diagonal, 
# a positive value refers to an upper diagonal, and a negative value to a lower diagonal.Default is 0.
# dtype : [optional] Desired output data-type.
# order : Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.

# Return : A n x M matrix where all elements are equal to zero, except for the k-th diagonal, whose values are equal to one.

# importing matrix library from numpy
# import numpy
# import numpy.matlib
  
# # desired 3 x 3 output matrix 
# out_mat = numpy.matlib.eye(3, k = 0) 
# print ("Output matrix : ", out_mat) 


# # importing numpy and matrix library
# import numpy 
# import numpy.matlib
  
# # desired 4 x 5 output matrix 
# out_mat = numpy.matlib.eye(n = 4, M = 5, k = 1, dtype = int) 
# print ("Output matrix : ", out_mat) 



###################################################################################



# numpy matrix operations | identity() function
# numpy.matlib.identity() is another function for doing matrix operations in numpy. 
# It returns a square identity matrix of given input size.

# Syntax : numpy.matlib.identity(n, dtype=None)

# Parameters :
# n : [int] Number of rows and columns in the output matrix.
# dtype : [optional] Desired output data-type.

# Return : n x n matrix with its main diagonal set to one, and all other elements zero.

# importing matrix library from numpy
# import numpy 
# import numpy.matlib
  
# # desired 3 x 3 output square identity matrix 
# out_mat = numpy.matlib.identity(3) 
# print ("Output matrix : ", out_mat) 


# # importing numpy and matrix library
# import numpy 
# import numpy.matlib
  
# # desired 5 x 5 output square identity matrix 
# out_mat = numpy.matlib.identity(n = 5, dtype = int) 
# print ("Output matrix : ", out_mat) 



###################################################################################



# Numpy ndarray.dot() function | Python
# numpy.ndarray.dot() function return the dot product of two arrays.

# importing numpy  
# import numpy 
  
# arr1 = numpy.eye(3)
# arr = numpy.ones((3, 3)) * 3
# print(arr1)
# print(arr)
  
# dp = arr1.dot( arr )
# print(dp)

# dp2 = numpy.dot(arr1, arr )
# print(dp2)


# dp1 = arr1.dot(arr).dot(arr)
# print(dp1)


# res = arr1 @ arr
# print(res)


###################################################################################
###################################################################################