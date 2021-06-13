import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
  
data = [16, 19, 23, 25, 27, 44, 45, 47, 55, 56]
  
# separating the stem parts
stems = [1, 1, 2, 2, 2, 4, 4, 4, 5, 5]
  
plt.ylabel('Data')   # for label at y-axis
  
plt.xlabel('stems')   # for label at x-axis
  
plt.xlim(0, 10)   # limit of the values at x axis
  
plt.stem(stems, data)   # required plot

plt.show()