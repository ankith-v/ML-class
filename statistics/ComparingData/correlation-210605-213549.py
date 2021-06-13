import pandas as pd

df = pd.read_csv("C:\\Users\\rohan\\Desktop\\lab\\Statistics\\Comparing data\\nba.csv")

# first 10  rows
# print("First ten rows:", df[:10])

# find correlation
# # using pearson method
# correlation = df.corr(method='pearson')
# print(correlation)


# # # using kendall method
# correlation = df.corr(method='spearman')
# print(correlation)










ice = pd.DataFrame()
ice['temp'] = [14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2]


correlation = ice.corr(method='pearson')
print(correlation)







