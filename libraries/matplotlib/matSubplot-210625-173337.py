########################################################################

# Display Multiple Plots
# With the subplots() function you can draw multiple plots in one figure:

# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)        # no. row, no. col, plot no.
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)

# plt.show()

########################################################################

# The subplots() Function
# The subplots() function takes three arguments that describes the layout of the figure.
# The layout is organized in rows and columns, which are represented by the first and second argument.
# The third argument represents the index of the current plot.

########################################################################

# Draw 2 plots on top of each other:
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 1, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 1, 2)
# plt.plot(x,y)

# plt.show()

########################################################################

# Draw 6 plots:
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show()

########################################################################

# Title
# You can add a title to each plot with the title() function:

# 2 plots, with titles:
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.show()

########################################################################

# Super Title
# You can add a title to the entire figure with the suptitle() function:

# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.suptitle("MY SHOP")

# plt.show()

########################################################################
########################################################################

