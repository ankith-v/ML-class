import numpy as np; np.random.seed(13)
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# x = [0,1,2,3,4,5,6,7,8,9,10,11,12]
# y = [6,2,3,5,2,5,0,0,2,3,7,4,1]

# plt.scatter(x, y)
# plt.show()






data = np.random.randint(0,12,size=72)
bins = np.arange(13)-0.5

hist, edges = np.histogram(data, bins=bins)

y = np.arange(1,hist.max()+1)
x = np.arange(12)
X,Y = np.meshgrid(x,y)

plt.scatter(X,Y, c=Y<=hist, cmap="Greys")

plt.show()






# # Create random data
# # rng = np.random.default_rng(123) # random number generator
# data = [6,2,3,5,2,5,0,0,2,3,7,4,1]
# # data = rng.integers(0, 13, size=40)
# values, counts = np.unique(data, return_counts=True)

# # Draw dot plot with appropriate figure size, marker size and y-axis limits
# fig, ax = plt.subplots(figsize=(6, 2.25))
# for value, count in zip(values, counts):
#     ax.plot([value]*count, list(range(count)), 'co', ms=10, linestyle='')
# for spine in ['top', 'right', 'left']:
#     ax.spines[spine].set_visible(False)
# ax.yaxis.set_visible(False)
# ax.set_ylim(-1, max(counts))
# ax.set_xticks(range(min(values), max(values)+1))
# ax.tick_params(axis='x', length=0, pad=8, labelsize=12)

# plt.show()





