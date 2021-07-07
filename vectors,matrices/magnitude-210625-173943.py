###################################################################################

# There are mainly two ways of getting the magnitude of vector:

# By defining an explicit function which computes the magnitude of a given vector 
# based on the below mathematical formula:
# if V is vector such that, V = (a, b, c)
# then ||V|| = ?(a*a + b*b + c*c)


# importing required libraries
# import numpy
# import math

# # function defination to compute magnitude o f the vector
# def magnitude(vector):
# 	return math.sqrt(sum(pow(element, 2) for element in vector))

# # displaying the original vector
# v = numpy.array([0, 1, 2, 3, 4])
# print('Vector:', v)

# # computing and displaying the magnitude of the vector
# print('Magnitude of the Vector:', magnitude(v))


###################################################################################


# importing required libraries
# import numpy
# import math

# # function defination to compute magnitude o f the vector
# def magnitude(vector):
# 	return math.sqrt(sum(pow(element, 2) for element in vector))

# # computing and displaying the magnitude of the vector
# print('Magnitude of the Vector:', magnitude(numpy.array([1, 2, 3])))


###################################################################################


# By using the norm() method in linalg module of NumPy library. 
# Programs which use numpy.linalg.norm() to compute the magnitude of a vector:

  
# importing required libraries
# import numpy
  
# # displaying the original vector
# v = numpy.array([1, 2, 3])
# print('Vector:', v)
  
# # computing and displaying the magnitude of the vector using norm() method
# print('Magnitude of the Vector:', numpy.linalg.norm(v))

###################################################################################

# An additional argument ord can be used to compute the nth order of the norm() of a vector.


# importing required libraries
# import numpy

# # displaying the original vector
# v = numpy.array([0, 1, 2, 3, 4])
# print('Vector:', v)

# # computing and displaying the magnitude of the vector
# print('Magnitude of the Vector:', numpy.linalg.norm(v))

# # Computing the nth order of the magnitude of vector
# print('ord is 0: ', numpy.linalg.norm(v, ord = 0))
# print('ord is 1: ', numpy.linalg.norm(v, ord = 1))
# print('ord is 2: ', numpy.linalg.norm(v, ord = 2))
# print('ord is 3: ', numpy.linalg.norm(v, ord = 3))
# print('ord is 4: ', numpy.linalg.norm(v, ord = 4))

###################################################################################
