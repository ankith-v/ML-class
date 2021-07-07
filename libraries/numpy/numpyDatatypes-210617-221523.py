###########################################################################


# Example
# # Get the data type of an array object:
# import numpy as np
# arr = np.array([1, 2, 3, 4]) 
# print(arr.dtype)

# ###########################################################################

# # Example
# # Get the data type of an array containing strings:
# import numpy as np
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)



###########################################################################

# Example
# Create an array with data type string:
# import numpy as np
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)
# # For i, u, f, S and U we can define size as well.

# ###########################################################################

# # Example
# # Create an array with data type 4 bytes integer:
# import numpy as np
# arr = np.array([1, 2, 3, 4], dtype='i4')
# print(arr)
# print(arr.dtype)


###########################################################################

# Example
# A non integer string like 'a' can not be converted to integer (will raise an error):
# import numpy as np
# arr = np.array(['a', '2', '3'], dtype='i')




###########################################################################

# Example
# # Change data type from float to integer by using 'i' as parameter value:
# import numpy as np
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)


# ###########################################################################
# # Example
# # Change data type from float to integer by using int as parameter value:
# import numpy as np
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)

# ###########################################################################

# # Example
# # Change data type from integer to boolean:
# import numpy as np
# arr = np.array([1, 0, 3])
# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)

###########################################################################
# Example
# Make a copy, change the original array, and display both arrays:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)
# # The copy SHOULD NOT be affected by the changes made to the original array.


###########################################################################

# Example
# Make a view, change the original array, and display both arrays:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)
# # The view SHOULD be affected by the changes made to the original array.


###########################################################################
# Make Changes in the VIEW:
# Example
# Make a view, change the view, and display both arrays:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 31
# print(arr)
# print(x)
# # The original array SHOULD be affected by the changes made to the view.


###########################################################################


# Example
# Print the value of the base attribute to check if an array owns it's data or not:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)
# print(y.base)
# # The copy returns None.
# The view returns the original array.


###########################################################################

# Example
# Print the shape of a 2-D array:
# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)
# # The example above returns (2, 4), which means that the array has 2 dimensions, and each dimension has 4 elements.


# ###########################################################################

# # Example
# # Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
# import numpy as np
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)

###########################################################################


# Example
# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)


###########################################################################

# Example
# Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)

###########################################################################


# Example
# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# print(newarr)



###########################################################################

# Example
# # Check if the returned array is a copy or a view:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr.reshape(2, 4).base)
# # The example above returns the original array, so it is a view.

###########################################################################

# Example
# Convert 1D array with 8 elements to 3D array with 2x2 elements:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1)
# print(newarr)
# Note: We can not pass -1 to more than one dimension.




###########################################################################


# Example
# Convert the array into a 1D array:
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)


###########################################################################

# Example
# Iterate on the elements of the following 1-D array:
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)


###########################################################################

# Example
# Iterate on the elements of the following 2-D array:
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)



# ###########################################################################
# # If we iterate on a n-D array it will go through n-1th dimension one by one. To return the actual values, the scalars, 
# # we must iterate the arrays in each dimension.
# #   
# # Example
# # Iterate on each scalar element of the 2-D array:
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   for y in x:
#     print(y)


###########################################################################

# Example
# Iterate on the elements of the following 3-D array:
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   print(x)

###########################################################################

# # To return the actual values, the scalars, we must iterate the arrays in each dimension.
# # Example
# # Iterate down to the scalars:
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)


# ###########################################################################
# Example
# # Iterate through the following 3-D array:
# import numpy as np
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#   print(x)



# ###########################################################################

# # Example
# # Iterate through the array as a string:
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)

###########################################################################

# Example
# Iterate through every scalar element of the 2D array skipping 1 element:
# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#   print(x)


###########################################################################

# Example
# Enumerate on following 1D arrays elements:
# import numpy as np
# arr = np.array([1, 2, 3])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)


# ###########################################################################


# # Example
# # Enumerate on following 2D array's elements:
# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for idx, x in np.ndenumerate(arr):
#   print(idx, x)


###########################################################################


# Example
# Join two arrays
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)


###########################################################################


# Example
# Join two 2-D arrays along rows (axis=1):
# import numpy as np
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)
# 1 2   5 6
# 3 4   7 8
###########################################################################


# Example
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)


###########################################################################

# Example
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.hstack((arr1, arr2))
# print(arr)




###########################################################################


# Example
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.vstack((arr1, arr2))
# print(arr)


#dstack()

###########################################################################


# Example
# Split the array in 3 parts:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr)


###########################################################################


# #Example
# Split the array in 4 parts:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)

###########################################################################

# Example
# Access the splitted arrays:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# ###########################################################################

# # Example
# # Split the 2-D array into three 2-D arrays.
# import numpy as np
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)


###########################################################################



# Example
# Split the 2-D array into three 2-D arrays.
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr, 3)
# print(newarr)



###########################################################################



# Example
# Split the 2-D array into three 2-D arrays along rows.
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr, 3, axis=1)
# print(newarr)
# # An alternate solution is using hsplit() opposite of hstack()



###########################################################################

# # Example
# # Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.hsplit(arr, 3)
# print(newarr)


###########################################################################



# Example
# Find the indexes where the value is 4:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)


# ###########################################################################

# Example
# Find the indexes where the values are even:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)


###########################################################################

# Example
# Find the indexes where the values are odd:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)


# ###########################################################################
# # Example
# # Find the indexes where the value 7 should be inserted:
# import numpy as np
# arr = np.array([4, 6, 8, 9])
# x = np.searchsorted(arr, 7)
# print(x)


# # ###########################################################################
# Example
# Find the indexes where the value 7 should be inserted, starting from the right:
# import numpy as np
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7, side='right')
# print(x)


###########################################################################

# Example
# Find the indexes where the values 2, 4, and 6 should be inserted:
# import numpy as np
# arr = np.array([1, 3, 5, 7])
# x = np.searchsorted(arr, [2, 4, 6])
# print(x)


# ###########################################################################

# Example
# Sort the array:
# import numpy as np
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))


# ###########################################################################

# Example
# # Sort the array alphabetically:
# import numpy as np
# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))

# ###########################################################################


# Example
# # Sort a boolean array:
# import numpy as np
# arr = np.array([True, False, True])
# print(np.sort(arr))


###########################################################################
# Example
# Sort a 2-D array:
# import numpy as np
# arr = np.array([[3, 2, 4], [5, 0, 1]])	
# print(np.sort(arr))




###########################################################################


# Example
# Create an array from the elements on index 0 and 2:
# import numpy as np
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)

###########################################################################
# 

###########################################################################

# Example
# Create a filter array that will return only even elements from the original array:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#   # if the element is completely divisble by 2, set the value to True, otherwise False
#   if element % 2 == 0:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


###########################################################################


# Example
# Create a filter array that will return only values higher than 42:
# import numpy as np
# arr = np.array([41, 42, 43, 44])
# filter_arr = arr > 42
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)


###########################################################################

# Example
# Create a filter array that will return only values higher than 42:
# import numpy as np
# arr = np.array([41, 42, 43, 44])
# filter_arr = arr > 42
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)

###########################################################################

# Example
# Create a filter array that will return only even elements from the original array:
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# filter_arr = arr % 2 == 0
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)


###########################################################################