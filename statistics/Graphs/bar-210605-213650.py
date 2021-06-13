import matplotlib
import numpy as np
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# plt.rcdefaults()

# objects = ('Comedy', 'Action', 'Romance', 'Drama', 'Sci-fi', 'Thriller')
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,9]

# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Most liked movie')
# plt.title('Movie Genre')

# plt.show()





# Horizontal

objects = ('Comedy', 'Action', 'Romance', 'Drama', 'Sci-fi', 'Thriller')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,9]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Most liked movie')
plt.title('Movie Genre')

plt.show()