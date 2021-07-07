###########################################################################
# intro 
# import numpy
# arr = numpy.array([1, 2, 3, 4, 5])
# print(arr)

###########################################################################

# #alias
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

###########################################################################
# #check numpy version
# import numpy as np
# print(np.__version__)
###########################################################################

# # create with ndarray
# # Example
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))
# # type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.
# # ndarray type.
# # To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

###########################################################################

# # Example
# # Use a tuple to create a NumPy array:
# import numpy as np
# arr = np.array((1, 2, 3, 4, 5))
# print(arr)

###########################################################################
# # Create an array of ones
# import numpy as np
# arr = np.ones((3,4))
# print(arr)
###########################################################################

# # Create an array of zeros
# # numpy.zeros(shape, dtype = None, order = 'C')
# import numpy as np
# arr =np.zeros((2,3,4),dtype=np.int16)
# print(arr)

###########################################################################

# # Create an array with random values
# import numpy as np
# arr =np.random.random((2,2))
# print(arr)

###########################################################################

# # # Create an empty array
# empty, unlike zeros, does not set the array values to zero, and may therefore be marginally faster. 
# On the other hand, it requires the user to manually set all the values in the array, and should be used with caution.
# import numpy as np
# arr =np.empty((3, 4), dtype=int)
# print(arr)

###########################################################################

# # Create a full array
# import numpy as np
# arr =np.full((2,2),7)
# print(arr)

###########################################################################

# # Create an array of evenly-spaced values
# import numpy as np
# arr =np.arange(10,25,5)
# print(arr)
###########################################################################


# # Create an array of evenly-spaced values
# import numpy as np
# arr =np.linspace(0,2,9)
# print(arr)


###########################################################################
# create an identity array or matrix with np.eye(). 
# import numpy as np
 
# 2x2 matrix with 1's on main diagnol
# b = np.eye(2, dtype = float)
# print("Matrix b : \n", b)
 
# # matrix with R=4 C=5 and 1 on diagnol
# # below main diagnol
# a = np.eye(4, 5, k = -1)
# print("\nMatrix a : \n", a)


###########################################################################

#create identity matrix
# import numpy as np 
# # 2x2 matrix with 1's on main diagnol
# b = np.identity(2, dtype = float)
# print("Matrix b : \n", b)


###########################################################################

# # # Sample code for generation of first example
# import numpy as np
# # from matplotlib import pyplot as plt
# # pyplot imported for plotting graphs
  
# x = np.linspace(-4, 4, 9)
  
# # numpy.linspace creates an array of
# # 9 linearly placed elements between
# # -4 and 4, both inclusive 
# y = np.linspace(-5, 5, 11)
  
# # The meshgrid function returns
# # two 2-dimensional arrays 
# x_1, y_1 = np.meshgrid(x, y)
  
# print("x_1 = ")
# print(x_1)
# print("y_1 = ")
# print(y_1)



###########################################################################




# This is your data in the text file
# Value1  Value2  Value3
# 0.2536  0.1008  0.3857
# 0.4839  0.4536  0.3561
# 0.1292  0.6875  0.5929
# 0.1781  0.3049  0.8928
# 0.6253  0.3486  0.8791

# # Import your data
# import numpy as np
# x, y, z = np.loadtxt('data.txt', skiprows=1, unpack=True)
# print(x,y,z)    

# import numpy as np
# narray = np.genfromtxt('data.txt', skip_header=1)
# print(narray)   

###########################################################################

# use the savetxt() function 
# import numpy as np
# x = np.arange(0.0,5.0,1.0)
# np.savetxt('test.out', x, delimiter=',')

###########################################################################



# Print out memory address
# import numpy as np
# my_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_2d_array.data)

###########################################################################

# Print out the shape of `my_array`
# import numpy as np
# my_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_2d_array.shape)

###########################################################################

# Print out the data type of `my_array`
# import numpy as np
# my_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_2d_array.dtype)

###########################################################################

# Print out the stride of `my_array`
# import numpy as np
# my_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_2d_array.strides)

###########################################################################



# Print the number of `my_array`'s dimensions
# import numpy as np
# my_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_array.ndim)

# # Print the number of `my_array`'s elements
# print(my_array.size)

# # Print information about `my_array`'s memory layout
# print(my_array.flags)

# # Print the length of one array element in bytes
# print(my_array.itemsize)

# # Print the total consumed bytes by `my_array`'s elements
# print(my_array.nbytes)

###########################################################################

# Print the length of `my_array`
# import numpy as np
# my_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(len(my_array))

# # # Change the data type of `my_array`
# print(my_array.astype(float))


###########################################################################


# 0-D or scalar
# import numpy as np
# arr = np.array(42)
# print(arr)

###########################################################################



# Create a 1-D array containing the values 1,2,3,4,5:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)


###########################################################################


# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

###########################################################################


# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)

###########################################################################


# Example
# Check how many dimensions the arrays have:
# import numpy as np
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)



###########################################################################


# Example :Create an array with 5 dimensions and verify that it has 5 dimensions:
# import numpy as np
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)


###########################################################################


# # Example
# # Get the first element from the following array:
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[0])


# Example
# Get the second element from the following array.
# import numpy as np
# arr = np.array([1, 2, 3, 4]) 
# print(arr[1])


# # Example
# # Get third and fourth elements from the following array and add them.
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr[2] + arr[3])



###########################################################################

# Example
# Access the 2nd element on 1st dim:
# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st dim: ', arr[0, 1])
# # Example
# Access the 3rd element on 2nd dim:
# if you want to print 8: arr[1, 2])
# print('3rd element on 1st dim: ', arr[1, 2])


# # Example
# # Access the 4th element on 1nd dim:
# # if you want to print 4: arr[0, 3]

# print('2nd element on 1st dim: ', arr[0, 3])


# # Example
# # Access the 5th element on 2nd dim:
# print('5th element on 2nd dim: ', arr[1, 4])

###########################################################################



# Example 3d - explanation on the slide
# Access the third element of the second array of the first array:
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])
# # Example Explained arr[0, 1, 2] prints the value 6.

# # Example
# # Access the second element of the first array of the second array:
# print(arr[1, 0, 1])


###########################################################################



# Example
# Print the last element from the 2nd dim:
# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])


###########################################################################

# Example
# Slice elements from index 1 to index 5 from the following array:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])
# Note: The result includes the start index, but excludes the end index.
###########################################################################



# # Example
# # Slice elements from index 4 to the end of the array:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4:])


# ###########################################################################

# # Example
# # Slice elements from the beginning to index 4 (not included):
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[:4])


###########################################################################

# Example
# Slice from the index 3 from the end to index 1 from the end:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:-1])

# ###########################################################################
# # STEP
# # Use the step value to determine the step of the slicing:
# # Example
# # Return every other element from index 1 to index 5:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])

# ###########################################################################
# # Example
# # Return every other element from the entire array:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[::2])

###########################################################################

# # Example
# # From the second element, slice elements from index 1 to index 4 (not included):
# import numpy as np
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])
# # Note: Remember that second element has index 1.

# ###########################################################################

# # Example
# # From both elements, return index 2:
# import numpy as np
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2])


# ###########################################################################

# # Example
# # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
# import numpy as np
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:1, 1:4])

###########################################################################

# condition
# import numpy as np
# my_array = np.array([[1, 2, 3], [4, 5, 6]])
# my_3d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(my_array[my_array<2])

# # Specify a condition
# bigger_than_3 = (my_3d_array >= 3)
# print(my_3d_array[bigger_than_3])

# bigger_than_3 = (my_3d_array > 3) | (my_3d_array == 3)
# print(my_3d_array[bigger_than_3])


#fancy indexing
# # Select elements at (1,0), (0,1), (1,2) and (0,0)
# print(my_array[[1, 0, 1, 0],[0, 1, 2, 0]])
#  
# # Select a subset of the rows and columns
# print(my_array[[1, 0, 1, 0]][:,[0,1,2,0]])


###########################################################################



