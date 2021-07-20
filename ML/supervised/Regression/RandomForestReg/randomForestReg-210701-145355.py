
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('C:\\Users\\rohan\\Desktop\\lab\\ML\\Supervised\\randomForestReg\\IceCreamData.csv')
# print(dataset.head())

X = dataset['Temperature'].values
y = dataset['Revenue'].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train.reshape(-1,1), y_train)


y_pred = regressor.predict(X_test.reshape(-1,1))
# print(y_pred)


df = pd.DataFrame({'Real values': y_test, 'Predicted values': y_pred})
# print(df)



from sklearn.metrics import r2_score, mean_squared_error
print('R2 score:', r2_score(y_test, y_pred))

print('Mean squared error:', mean_squared_error(y_test, y_pred, squared=False))




X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
# plt.scatter(X_test, y_test, color = 'red')
# plt.scatter(X_test, y_pred, color = 'green')
# plt.title("Random Forest Regression")
# plt.xlabel('Temperature')
# plt.ylabel("Revenue")
# plt.show()


plt.plot(X_grid, regressor.predict(X_grid),color = 'black')
plt.title("Random Forest Regression")
plt.xlabel('Temperature')
plt.ylabel("Revenue")
plt.show()