import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np



# x = np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2])
# y = np.array([215,325,185,332,406,522,412,614,544,421,445,408])
# plt.scatter(x, y, color = 'hotpink')
# plt.show()






# line of best fit

x = np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2])
y = np.array([215,325,185,332,406,522,412,614,544,421,445,408])
m, b = np.polyfit(x, y, 1)
plt.scatter(x, y, color = 'hotpink')
plt.plot(x, m*x + b)
plt.show()
