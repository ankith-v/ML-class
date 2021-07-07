#########################################################################

# We will be using sns.distplot() in the code to plot distribution graphs.

import pandas as pd
import numpy as np
pstore = pd.read_csv("googleplaystore.csv")
# print(pstore.head(10))

#########################################################################

# let’s see how distribution plot looks like if we plot for ‘Rating’ column from the above dataset

# # importing all the libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Create a distribution plot for rating
# sns.distplot(pstore.Rating)
# plt.show()

#########################################################################

# we can change the number of bins and make the graph more understandable.
# We just have to add the number of bins in the code,
#Change the number of bins
# sns.distplot(pstore.Rating, bins=20, kde = False)
# plt.show()
# To remove the curve, we just have to write ‘kde = False’ in the code.

#########################################################################

# We can also provide the title and color of the bins similar to matplotlib to the distribution plots.
#importing all the libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# #Create a distribution plot for rating
# sns.distplot(pstore.Rating, bins=20, color="g")
# plt.title("Distribution of app ratings", fontsize=20, color = 'red')
# plt.show()

#########################################################################

# Styling the Seaborn graphs
# One of the biggest advantages of using Seaborn is, it offers a wide range of 
# default styling options to our graphs.
# These are the default styles offered by Seaborn.
# 'Solarize_Light2',
#  '_classic_test_patch',
#  'bmh',
#  'classic',
#  'dark_background',
#  'fast',
#  'fivethirtyeight',
#  'ggplot',
#  'grayscale',
#  'seaborn',
#  'seaborn-bright',
#  'seaborn-colorblind',
#  'seaborn-dark',
#  'seaborn-dark-palette',
#  'seaborn-darkgrid',
#  'seaborn-deep',
#  'seaborn-muted',
#  'seaborn-notebook',
#  'seaborn-paper',
#  'seaborn-pastel',
#  'seaborn-poster',
#  'seaborn-talk',
#  'seaborn-ticks',
#  'seaborn-white',
#  'seaborn-whitegrid',
#  'tableau-colorblind10'

#########################################################################

# We just have to write one line of code to incorporate these styles into our graph.

#importing all the libraries
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# #Adding dark background to the graph
# plt.style.use("dark_background")

# #Create a distribution plot for rating
# sns.distplot(pstore.Rating, bins=20, color="g")
# plt.title("Distribution of app ratings", fontsize=20, color = 'red')
# plt.show()

#########################################################################
#########################################################################
