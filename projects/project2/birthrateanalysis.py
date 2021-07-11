import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('./projects/project2/births.csv')

# print(df.describe())
# print(df)

# outlier 1 - day null values(replace with 0) and >31 cannot exist in a month
df['day'].fillna(0, inplace=True) 
df['day'] = df['day'].astype(int)
df1 = df[df['day']<=31]

# print(df1)
# print(df1.describe())

# outlier 2 - births < mu-(2*sigma)
quartiles = np.percentile(df1['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])
df2 = df1[df1['births']>(mu-(2*sig))]
print("mu,sigma and the quartiles are : ",mu,sig,quartiles)
# print(df2.describe())

# plotting
sns.set()
birth = df2.pivot_table('births', index='year',columns='gender',aggfunc='sum')
birth.plot()
plt.ylabel("births per year")
plt.show()