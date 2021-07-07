###################################################################################

# The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array.
# You can find:
# rank, determinant, trace, etc. of an array.
# eigen values of matrices
# matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
# solve linear or tensor equations and much more!

# Importing numpy as np
import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
 
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
 
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
 
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))


###################################################################################
###################################################################################