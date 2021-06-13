import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import norm 

domain = np.linspace(-4,4,1000)
plt.plot(domain,norm.pdf(domain,0,1))
plt.title("Standard normal")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()