import pandas as pd

# df = pd.read_csv('winequality-white.csv', sep=';')
# print(df.head().to_string())
# print(df.tail(10))

# print(df.shape)

# print(df.info())

# print(df.describe().to_string())

# print(df.quality.unique())

# print(df.quality.value_counts())



import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('winequality-white.csv', sep=';')
# cor = df.corr()
# print(cor)
plt.figure(figsize=(10,8))
# sns.heatmap(cor, annot= True, linewidth=0.5, cmap='YlGnBu')
# plt.show()



# sns.boxplot(y='alcohol', data=df)
# plt.show()



x = df['alcohol']
plt.subplot(1,3,1)
sns.kdeplot(x)

x = df['chlorides']
plt.subplot(1,3,2)
sns.kdeplot(x)

x = df['pH']
plt.subplot(1,3,3)
sns.kdeplot(x)

plt.show()
