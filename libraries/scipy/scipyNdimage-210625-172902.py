##############################################################

# SciPy Ndimage
# The SciPy provides the ndimage (n-dimensional image) package, that contains the 
# number of general image processing and analysis functions. It is dedicated to image processing. 
# We can perform several tasks in image processing such as input/output image, 
# classification, Feature extraction, Registration, etc.

##############################################################

# Opening and Writing to Image Files
# The scipy.ndimage provides the misc package, which comes with some images. 


# from scipy import misc  
# f = misc.face()  
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt  
# plt.imshow(f)  
# plt.show()  

# print(f.shape)

##############################################################

# We can perform the some basic operations such as image rotation, image up-side down.

# from scipy import misc  
# import numpy as np
# face = misc.face()  
# flip_ud_face = np.flipud(face)  
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt  
# plt.imshow(flip_ud_face)  
# plt.show()  

##############################################################

# The SciPy provide the rotate() function, which rotates the image to the specified angle.

# from scipy import misc,ndimage  
# face = misc.face()  
# rotate_face = ndimage.rotate(face, 30) #rotating the image 30 degree  
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt  
# plt.imshow(rotate_face)  
# plt.show()  

##############################################################

# Filters
# Filtering is the process where we modify and enhance an image.
# Blurring
# Blurring is the technique that is used to reduce the noise in the image.

# from scipy import misc  
# from scipy import ndimage  
# face = misc.face()  
# blurred_image = ndimage.gaussian_filter(face, sigma=4)  
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt  
# plt.imshow(blurred_image)  
# plt.show()  

##############################################################

# Edge Detection
# Edge detection is an image processing term which is used for finding the boundaries of 
# objects within the image.

# import scipy.ndimage as nd  
# import numpy as np  
# im = np.zeros((256, 256))  
# # im[64:-64, 64:-64] = 1  or
# im[64:192, 64:192] = 1 
# im[90:-90,90:-90] = 2  
# im = nd.gaussian_filter(im, 5) 
# import matplotlib
# matplotlib.use('TkAgg')  
# import matplotlib.pyplot as plt 
# plt.imshow(im)  
# plt.show()  

##############################################################
# The output image appears like a square block of color. 
# Now, we will find the edges of those colored block. 
# The ndimage provides the sobel() function to perform this operation. 
# Whereas, NumPy provides the hypot() function which is used to combine the two resultant matrices to one. 

# import scipy.ndimage as nd  
# import numpy as np
# import matplotlib
# matplotlib.use('TkAgg') 
# import matplotlib.pyplot as plt  
# im = np.zeros((256, 256))  
# im[64:-64, 64:-64] = 1  
# im[90:-90,90:-90] = 2  
# im = nd.gaussian_filter(im, 8)  
# zx = nd.sobel(im, axis = 0, mode = 'constant')  
# zy = nd.sobel(im, axis = 1, mode = 'constant')  
# sobl = np.hypot(zx, zy)  
# plt.imshow(sobl)  
# plt.show()  

##############################################################
##############################################################