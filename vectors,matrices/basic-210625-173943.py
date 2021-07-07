#################################################################################

# Operation on Matrix :
# 1. add() :- This function is used to perform element wise matrix addition.

# 2. subtract() :- This function is used to perform element wise matrix subtraction.

# 3. divide() :- This function is used to perform element wise matrix division.

# 4. multiply() :- This function is used to perform element wise matrix multiplication.

# 5. dot() :- This function is used to compute the matrix multiplication, rather than element wise multiplication.

# 6. sqrt() :- This function is used to compute the square root of each element of matrix.

# 7. sum(x,axis) :- This function is used to add all the elements in matrix. Optional “axis” argument computes the column sum if axis is 0 and row sum if axis is 1.

# 8. “T” :- This argument is used to transpose the specified matrix.


# importing numpy for matrix operations
import numpy
  
# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])
  
# using add() to add matrices
print ("The element wise addition of matrix is : ")
print (numpy.add(x,y))
  
# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (numpy.subtract(x,y))
  
# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (numpy.divide(x,y))

# using multiply() to multiply matrices element wise
print ("The element wise multiplication of matrix is : ")
print (numpy.multiply(x,y))
  
# using dot() to multiply matrices
print ("The product of matrices is : ")
print (numpy.dot(x,y))

# using sqrt() to print the square root of matrix
print ("The element wise square root is : ")
print (numpy.sqrt(x))
  
# using sum() to print summation of all elements of matrix
print ("The summation of all matrix element is : ")
print (numpy.sum(y))
  
# using sum(axis=0) to print summation of all columns of matrix
print ("The column wise summation of all matrix  is : ")
print (numpy.sum(y,axis=0))
  
# using sum(axis=1) to print summation of all columns of matrix
print ("The row wise summation of all matrix  is : ")
print (numpy.sum(y,axis=1))
  
# using "T" to transpose the matrix
print ("The transpose of given matrix is : ")
print (x.T)



# Numpy matrix.transpose()
# With the help of Numpy matrix.transpose() method, we can find the transpose of the 
# matrix by using the matrix.transpose() method.

# Syntax : matrix.transpose()
# Return : Return transposed matrix

          
# applying matrix.transpose() method
# trans = x.transpose()
# print(trans)