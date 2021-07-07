###########################################################################


# Python program explaining
# numpy.random.ranf() function
  
# # importing numpy
# import numpy as np
  
  
# # output random float value
# out_val = np.random.ranf()
# print ("Output random float value : ", out_val) 

# ###########################################################################

# Python program explaining
# numpy.random.ranf() function

# importing numpy
# import numpy as np


# # output array
# out_arr = np.random.ranf(size =(2, 1))
# print ("Output 2D Array filled with random floats : ", out_arr)


###########################################################################

# Python program explaining
# numpy.random.ranf() function

# # importing numpy
# import numpy as np

# # output array
# out_arr = np.random.ranf((3, 3, 2))
# print ("Output 3D Array filled with random floats : ", out_arr)


# ###########################################################################

# # Python program explaining
# # numpy.random.random() function

# # importing numpy
# import numpy as np


# # output array
# out_arr = np.random.random(size = 3)
# print ("Output 1D Array filled with random floats : ", out_arr)


###########################################################################

# # Python program explaining
# # numpy.random.random() function

# # importing numpy
# import numpy as np


# # output array
# out_arr = np.random.random(size =(2, 4))
# print ("Output 2D Array filled with random floats : ", out_arr)




###########################################################################

# ## Python program explaining
# # numpy.random.random() function

# # importing numpy
# import numpy as np

# # output array
# out_arr = np.random.random((2, 3, 2))
# print ("Output 3D Array filled with random floats : ", out_arr)


# ###########################################################################
# # Python program explaining
# # numpy.random.sample() function

# # importing numpy
# import numpy as np

# # output random value
# out_val = np.random.random_sample()
# print ("Output random float value : ", out_val)


# ###########################################################################

# # Python program explaining
# # numpy.random.random_sample() function

# # importing numpy
# import numpy as np


# # output array
# out_arr = np.random.random_sample(size =(1, 3))
# print ("Output 2D Array filled with random floats : ", out_arr)


###########################################################################
# # Python program explaining
# # numpy.random.sample() function

# # importing numpy
# import numpy as np

# # output random value
# out_val = np.random.sample()
# print ("Output random value : ", out_val)



###########################################################################

# # Python program explaining
# # numpy.random.sample() function

# # importing numpy
# import numpy as np


# # output array
# out_arr = np.random.sample(size =(3, 3))
# print ("Output 2D Array filled with random floats : ", out_arr)



###########################################################################

# Python program explaining
# # numpy.random.sample() function

# # importing numpy
# import numpy as np

# # output array
# out_arr = np.random.sample((2, 2, 3))
# print ("Output 3D Array filled with random floats : ", out_arr)



###########################################################################

# # Python program explaining
# # numpy.random.random_integers() function

# # importing numpy
# import numpy as np

# # output array
# out_arr = np.random.random_integers(low = 0, high = 5, size = 4)
# print ("Output 1D Array filled with random integers : ", out_arr)


###########################################################################
# # Python program explaining
# # numpy.random.random_integers() function

# # importing numpy
# import numpy as np


# # output array
# out_arr = np.random.random_integers(low = 3, size =(3, 3))
# print ("Output 2D Array filled with random integers : ", out_arr)


# ###########################################################################
# # Python program explaining
# # numpy.random.random_integers() function

# # importing numpy
# import numpy as np

# # output array
# out_arr = np.random.random_integers(1, 6, (2, 2, 3))
# print ("Output 3D Array filled with random integers : ", out_arr)


###########################################################################

# # Python program explaining
# # numpy.random.randint() function

# # importing numpy
# import numpy as np

# # output array
# out_arr = np.random.randint(low = 0, high = 3, size = 5)
# print ("Output 1D Array filled with random integers : ", out_arr)



###########################################################################

# Python program explaining
# # numpy.random.randint() function

# # importing numpy
# import numpy as np


# # output array
# out_arr = np.random.randint(low = 4, size =(2, 3))
# print ("Output 2D Array filled with random integers : ", out_arr)


###########################################################################

# # Python program explaining
# # numpy.random.randint() function

# # importing numpy
# import numpy as np

# # output array
# out_arr = np.random.randint(2, 10, (2, 3, 4))
# print ("Output 3D Array filled with random integers : ", out_arr)



###########################################################################

# # import choice
# import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt

# # Using choice() method
# gfg = np.random.choice(13, 5000)

# count, bins, ignored = plt.hist(gfg, 25, density = True)
# plt.show()


###########################################################################

# # import choice
# import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt

# # Using choice() method
# gfg = np.random.choice(5, 1000, p =[0.2, 0.1, 0.3, 0.4, 0])

# count, bins, ignored = plt.hist(gfg, 14, density = True)
# plt.show()





###########################################################################


# How to choose elements from the list with different probability using NumPy?
# Syntax: numpy.random.choice(a, size=None, replace=True, p=None)
# Output: Return the numpy array of random samples.
# Note: parameter p is probabilities associated with each entry in a(1d-array). 
# If not given the sample assumes a uniform distribution over all entries in list.
# import numpy library
# import numpy as np

# # create a list
# num_list = [10, 20, 30, 40, 50]

# # uniformly select any element
# # from the list
# number = np.random.choice(num_list)

# print(number)




# ###########################################################################

# # import numpy
# import numpy as np
# import matplotlib.pyplot as plt

# gfg = np.arange(10)
# print(gfg)
# # Using shuffle() method
# np.random.shuffle(gfg)

# print(gfg)

###########################################################################

# # import numpy
# import numpy as np
# import matplotlib.pyplot as plt

# gfg = np.arange(16).reshape((4, 4))
# print(gfg)
# # Using shuffle() method
# np.random.shuffle(gfg)

# print(gfg)

###########################################################################


