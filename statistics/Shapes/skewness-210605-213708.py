# It is a symmetrical graph with all measures of central tendency in the middle.

# scipy stats.skew()
# scipy.stats.skew(array, axis=0, bias=True) 

# skewness = 0 : normally distributed.
# skewness > 0 : more weight in the left tail of the distribution.
# skewness < 0 : more weight in the right tail of the distribution. 






# x = [8.0, 1, 2.5, 4, 28.0]
# n = len(x)
# mean = sum(x) / n
# var = sum((item - mean)**2 for item in x) / (n - 1)
# std = var ** 0.5
# skew = (sum((item - mean)**3 for item in x)
#          * n / ((n - 1) * (n - 2) * std**3))

# print("Skew:", skew)





# import pandas as pd

# dataVal = [(10,20,30,40,50,60,70),
#            (10,10,40,40,50,60,70),
#            (10,20,30,50,50,60,80)]

# dataFrame = pd.DataFrame(data=dataVal)

# skewValue = dataFrame.skew(axis=1)

# print("DataFrame:")
# print(dataFrame)

# print("Skew:")
# print(skewValue)