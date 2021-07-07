#########################################################################

# Pie Chart is generally used to analyze the data 
# on how a numeric variable changes across different categories.

import pandas as pd
pstore = pd.read_csv("googleplaystore.csv")

#########################################################################

# First, we’ll do some data cleaning/mining to the Content rating column 
# and check what are the categories in there.

#importing all the libraries
# import numpy as np
# import pandas as pd

# #Analyzing the Content Rating column
# print(pstore['Content Rating'].value_counts())

#########################################################################

# Since the count of “Adults only 18+” and “Unrated” are significantly 
# less compared to the others, we’ll drop those categories from the Content Rating and update the dataset.

#importing all the libraries
# import numpy as np
# import pandas as pd

# #Remove the rows with values which are less represented 
# pstore = pstore[~pstore['Content Rating'].isin(["Adults only 18+","Unrated"])]

# #Resetting the index
# pstore.reset_index(inplace=True, drop=True)

# #Analyzing the Content Rating column again
# print(pstore['Content Rating'].value_counts())

#########################################################################

# Now, let’s plot Pie Chart for the categories present in the Content Rating column.

#importing all the libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# #Plotting a pie chart
# plt.figure(figsize=[9,7])
# pstore['Content Rating'].value_counts().plot.pie()
# plt.show()

#########################################################################

# From the above Pie diagram, we cannot correctly infer whether “Everyone 10+” and “Mature 17+”. 
# It is very difficult to assess the difference between those two categories 
# when their values are somewhat similar to each other.

# We can overcome this situation by plotting the above data in Bar chart.

#importing all the libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# #Plotting a bar chart
# plt.figure(figsize=[9,7])
# pstore['Content Rating'].value_counts().plot.barh()
# plt.show()

#########################################################################
#########################################################################


