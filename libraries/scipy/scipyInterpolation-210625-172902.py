##############################################################

# SciPy Interpolation
# Interpolation is a method for generating points between given points.

# Interpolation is defined as finding a value between two points on a line or a curve. 
# The first part of the word is "inter" as meaning "enter", which indicates us 
# to look inside the data. In the other words, 
# "The estimation of intermediate value between the precise data points is called as interpolation". 

# For example: for points 1 and 2, we may interpolate and find points 1.33 and 1.66.

# This method of filling values is called imputation.
# Apart from imputation, interpolation is often used where we need to smooth the discrete points in a dataset.

##############################################################

# Let's have a look how the interpolation work using the scipy.interpolation package.


# import numpy as np  
# x = np.linspace(0, 5, 10)   
# y = np.cos(x**2/3+4)  
# print(x,y)  



# We can plot those arrays as two dimension of the points in space
# import numpy as np  
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt  
# x = np.linspace(0, 5, 10)  
# y = np.cos(x**2/3+4)  
# plt.plot(x,y, 'o')  
# plt.show()  

##############################################################

# 1-D Interpolation
# scipy.interpolation provides interp1d class which is an useful method 
# to create a function based on fixed data points.

# SciPy provides us with a module called scipy.interpolate which has many functions to deal with interpolation:

# For given xs and ys interpolate values from 2.1, 2.2... to 2.9:
# from scipy.interpolate import interp1d
# import numpy as np
# xs = np.arange(10)
# ys = 2*xs + 1
# print(xs)
# print(ys)
# interp_func = interp1d(xs, ys)
# newarr = interp_func(np.arange(2.1, 3, 0.1))
# print(newarr)
# Note: that new xs should be in same range as of the old xs, 
#   meaning that we cant call interp_func() with values higher than 10, or less than 0.


# import numpy as np  
# from scipy.interpolate import interp1d 
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt 
# x = np.linspace(0, 5, 10)  
# y = np.cos(x**2/3+4)   
# fun1 = interp1d(x, y,kind = 'linear')  
# fun2 = interp1d(x, y, kind = 'cubic')  
# xnew = np.linspace(0, 4,30)  
# plt.plot(x, y, 'o', xnew, fun1(xnew), '-', xnew, fun2(xnew), '--')  
# plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')  
# plt.show()  

##############################################################

# Spline Interpolation
# In 1D interpolation the points are fitted for a single curve whereas in 
# Spline interpolation the points are fitted against a piecewise function defined with polynomials called splines.
# The UnivariateSpline() function takes xs and ys and produce a callable funciton that can be called with new xs.


# Find univariate spline interpolation for 2.1, 2.2... 2.9 for the following non linear points:
# from scipy.interpolate import UnivariateSpline
# import numpy as np
# xs = np.arange(10)
# ys = xs**2 + np.sin(xs) + 1
# interp_func = UnivariateSpline(xs, ys)
# newarr = interp_func(np.arange(2.1, 3, 0.1))
# print(newarr)

##############################################################

# Interpolation with Radial Basis Function
# Radial basis function is a function that is defined corresponding to a fixed reference point.
# The Rbf() function also takes xs and ys as arguments and produces a callable function that can be called with new xs.

# Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:
# from scipy.interpolate import Rbf
# import numpy as np
# xs = np.arange(10)
# ys = xs**2 + np.sin(xs) + 1
# interp_func = Rbf(xs, ys)
# newarr = interp_func(np.arange(2.1, 3, 0.1))
# print(newarr)

##############################################################
##############################################################