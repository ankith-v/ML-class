import numpy as np
import pandas as pd

farm = pd.DataFrame()
farm['Price'] = [632541, 42541, 356471, 7412512]
farm['Rooms'] = [2, 5, 3, 100]
farm['Square_feet'] = [1600, 2850, 1780, 90000]
print(farm)

h = farm[farm['Rooms'] < 20]
print("H", h)

farm['Outlier'] = np.where(farm['Rooms'] < 20, 0, 1)
print(farm)

