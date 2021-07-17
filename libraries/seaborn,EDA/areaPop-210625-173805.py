import pandas as pd

cities = pd.read_csv('california_cities.csv')
# print(cities.head().to_string())
print(cities.tail(10))


latitude, longitude = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.scatter(longitude, latitude, label=None, c=np.log10(population),
        cmap='viridis', s=area, alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3,8)


for area in [100, 200, 300]:
    plt.scatter([],[], alpha=0.3, s=area, label=str(area)+'km$^2$')
plt.legend(scatterpoints = 1, frameon= False, labelspacing=1, title='City area')
plt.title('Area and Population of California')
plt.show()