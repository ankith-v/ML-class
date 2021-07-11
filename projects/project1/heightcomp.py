import pandas as pd
import statistics as stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('.\projects\project1\heights.csv')

# mean,median,mode
mean = df["height(cm)"].mean()
median = df["height(cm)"].median()
mode = df["height(cm)"].mode()
print("Mean , median , mode :", mean, ",", median, ",", mode)

# standard deviation
std_dev = stats.stdev(df["height(cm)"])
print("Standard deviation is :", std_dev)

# min and max
min_ht = min(df["height(cm)"])
print("Minimum height is :", min_ht, "cms")
max_ht = max(df["height(cm)"])
print("Maximum height is :", max_ht, "cms")

# percentiles
perc25 = np.percentile(df["height(cm)"],25)
perc50 = np.percentile(df["height(cm)"],50)
perc75 = np.percentile(df["height(cm)"],75)
print("The 25th , 50th , and 75th percentiles are :", perc25,",", perc50, ",", perc75, "respectively")

# histogram
matplotlib.use('TkAgg')
plt.hist(df["height(cm)"])
plt.hist(mean,color='red',label="mean")
plt.hist(median,color='darkgreen',label="median")
plt.hist(mode,color='black',label="mode")
plt.legend()
plt.xlabel("heights")
plt.ylabel("frequency")
plt.show()
