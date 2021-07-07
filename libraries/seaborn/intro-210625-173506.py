#########################################################################
# pip install seaborn 

# import seaborn as sns
# print(sns.get_dataset_names())

#########################################################################

# Now let us import any one of those datasets and visualize the data in the coming sections

# import seaborn as sns
# df = sns.load_dataset('car_crashes')
# print(df.head())

#########################################################################

# Styling and Themes in Seaborn
# First, let us see how we can style a simple Matplotlib plot using Seaborn’s set() function.

# from matplotlib import pyplot as plt
# import seaborn as sns
# df = sns.load_dataset('car_crashes')
# plt.scatter(df.speeding,df.alcohol)
# plt.show()


# Now let us see how we can style this plot using the set() function

# from matplotlib import pyplot as plt
# import seaborn as sns
# df = sns.load_dataset('car_crashes')
# plt.scatter(df.speeding,df.alcohol)
# sns.set()
# plt.show()

#########################################################################

# Seaborn Color Palette
# Seaborn has a reputation for making plots and graphs more attractive 
# using attractive colors and color combinations.

# import seaborn as sns
# sns.palplot(sns.color_palette("deep", 10))

# sns.palplot(sns.color_palette("PiYG", 10))

# sns.palplot(sns.color_palette("GnBu", 10))

#########################################################################
#########################################################################

# Plotting with the relplot function
# The Seaborn library provides us with relplot() function and this function provides access to 
# several different axes-level functions that show the relationship between two variables with 
# semantic mappings of subsets. The kind parameter selects the underlying axes-level function to use:
# 1. scatterplot() (with kind=”scatter”)
# 2. lineplot() (with kind=”line”)
# The default value for the parameter kind is ‘scatter’ which means that by default this 
# function would return a scatterplot. 

# import seaborn as sns
# from matplotlib import pyplot as plt
# tips = sns.load_dataset("tips")
# print(tips.head())

#########################################################################

# sns.relplot(data=tips, x="total_bill", y="tip")
# sns.relplot(data=tips, x="total_bill", y="tip", hue="day")
# sns.relplot(data=tips, x="total_bill", y="tip", hue="sex", col="day", col_wrap=2)
# sns.relplot(data=tips, x="size", y="tip",kind="line",ci=None)
# plt.show()

#########################################################################

# Histogram
# Histograms represent the data distribution by forming bins along with the range of the data 
# and then drawing bars to show the number of observations that fall in each bin.
# In Seaborn we use distplot() function to plot histograms.

# import seaborn as sns
# from matplotlib import pyplot as plt
# df = sns.load_dataset('iris')
# print(df.head())
# sns.distplot(df['petal_length'],kde = False)
# plt.show()

#########################################################################

# Bar Plot
# Seaborn supports many types of bar plots. Here, we will use both seaborn and matplotlib together 
# to demonstrate several plots.

# Vertical barplot
# The barplot plot below shows the survivors of the titanic crash based on category.

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_context('paper')
# # load dataset
# titanic = sns.load_dataset('titanic')
# # create plot
# sns.barplot(x = 'embark_town', y = 'age', data = titanic,
#             palette = 'PuRd',ci=None 
#             )
# plt.legend()
# plt.show()
# print(titanic.columns)


# import matplotlib.pyplot as plt
# import seaborn as sns
# # load dataset
# titanic = sns.load_dataset('titanic')
# # create plot
# sns.barplot(x = 'sex', y = 'survived', hue = 'class', data = titanic,
#             palette = 'PuRd',
#             order = ['male', 'female'],  
#             capsize = 0.05,             
#             saturation = 8,             
#             errcolor = 'gray', errwidth = 2,  
#             ci = 'sd'  
#             )
# plt.legend()
# plt.show()

# ci	- float or “sd” or None, optional -	Size of confidence intervals to draw around estimated values.  
#     If “sd”, skip bootstrapping and draw the standard deviation of the observations. 
#     If “None“, no bootstrapping will be performed, and error bars will not be drawn.
# saturation - float, optional - Proportion of the original saturation to draw colors at. 
# capsize - float, optional - Width of the “caps” on error bars.
# errcolor - matplotlib color - Color for the lines that represent the confidence interval.


# Horizontal barplot
# To draw a horizontal plot pass ‘h’ to the parameter, orient of the barplot function as shown below:

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_context('paper')
# titanic = sns.load_dataset('titanic')
# sns.barplot(x = 'age', y = 'embark_town', data = titanic,
#             palette = 'PuRd', orient = 'h')
# plt.show()

#########################################################################

# Count plot
# The count plot can be thought of as a histogram across a categorical variable.

# import matplotlib.pyplot as plt
# import seaborn as sns
  
# sns.set_context('paper')
 
# # load dataset
# titanic = sns.load_dataset('titanic')
# # create plot
# sns.countplot(x = 'class', hue = 'who', data = titanic, palette = 'magma')
# plt.title('Survivors')
# plt.show()

#########################################################################

# Point Plot
# Point plot is used to show point estimates and confidence intervals using scatter plot glyphs. 
# A point plot represents an estimate of central tendency for a numeric variable by the position 
# of scatter plot points and provides some indication of the uncertainty around that estimate using error bars.

# Point plots can be more useful than bar plots for focusing comparisons between different levels 
# of one or more categorical variables. 

# importing required packages 
# import seaborn as sns 
# import matplotlib.pyplot as plt 
   
# # loading dataset 
# data = sns.load_dataset("tips") 
# sns.pointplot(x="day", y="tip", data=data)
# sns.pointplot(x="time", y="total_bill", hue="smoker",
#                    data=data, palette="Accent")
# plt.show()

#########################################################################

# Joint Plot
# Joint Plot draws a plot of two variables with bivariate and univariate graphs. 
# It uses the Scatter Plot and Histogram. 
# Joint Plot can also display data using Kernel Density Estimate (KDE) and Hexagons. 
# We can also draw a Regression Line in Scatter Plot. 

# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_style("dark")
# tips=sns.load_dataset('tips')
# sns.jointplot(x='total_bill', y='tip',data=tips)

# # Add regression line to scatter plot and kernel density estimate to histogram
# # sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

# # Display kernel density estimate instead of scatter plot and histogram
# # sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')

# # Display hexagons instead of points in scatter plot
# # sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')

# plt.show()

#########################################################################

# Regplot
# Regplot is one of the functions in Seaborn that are used to visualize the linear relationship 
# as determined through regression. Also, you‘ll see a slightly shaded portion around the regression line 
# which indicates how much the pints are scattered around a certain area.

# Now we will plot a discrete x variable and add some jitter. 
# Here you can see that the areas where points are more densely populated have 
# less shaded portion around the regression line and shaded portion is more spread where 
# the points are more scattered.

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.regplot(x="total_bill", y="tip", data=tips)
# plt.show()

# sns.regplot(x="size", y="total_bill", data=tips, x_jitter=0.1)
# plt.show()


# We can set the parameter ci=None to get just the line without any highlighted portion.
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.regplot(x="total_bill", y="tip", data=tips,ci=None)
# plt.show()



# Lm Plot
# In Seaborn, we can also use lmplot instead of regplot to visualise a regression between 
# two variables as we saw in our last example. But what is the difference between the two plots?

# The regplot function performs a simple linear regression model fit and plot whereas the lmplot function 
# combines regplot and FacetGrid.

# The FacetGrid class helps in visualizing the distribution of one variable as well as the relationship 
# between multiple variables separately within subsets of your dataset using multiple panels.

# It is further important to note that lmplot() is more computationally intensive and is intended as a 
# convenient interface to fit regression models across conditional subsets of a dataset.

# Example of lmplot where it seems to work just like regplot.
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.lmplot(x="total_bill", y="tip", data=tips)
# plt.show()

# Here is how we can use the advance features of lmplot() and use it with multi-plot grid 
# for plotting conditional relationships.
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.lmplot(x="total_bill", y="tip", col="day", hue="day", data=tips, col_wrap=2, height=3)
# plt.show()

#########################################################################

# KDE plot
# KDE plot is a Kernel Density Estimate that is used for visualizing the Probability Density 
# of the continuous or non-parametric data variables i.e. we can plot for the univariate or 
# multiple variables altogether. 

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("dark")
iris = sns.load_dataset("iris")
# Plotting the KDE Plot 
# sns.kdeplot(iris.loc[(iris['species']=='setosa'), 
#             'sepal_length'], color='b', shade=True, label='setosa') 
# sns.kdeplot(iris.loc[(iris['species']=='virginica'), 
#             'sepal_length'], color='r', shade=True, label='virginica')
# plt.legend()
# plt.show()


# # Setting up the samples 
# iris_setosa = iris.query("species=='setosa'") 
# iris_virginica = iris.query("species=='virginica'") 
   
# # Plotting the KDE Plot 
# sns.kdeplot(iris_setosa['sepal_length'],  
#             iris_setosa['sepal_width'], 
#             color='r', shade=True, label='Iris_Setosa', 
#             cmap="Reds", shade_lowest=False) 
# # Plotting the KDE Plot 
# sns.kdeplot(iris_virginica['sepal_length'],  
#             iris_virginica['sepal_width'], 
#             color='b', shade=True, label='iris_virginica', 
#             cmap="Blues", shade_lowest=False)
# plt.legend()  
# plt.show() 

#########################################################################

# Box Plot
# The box plot, also called the box and whisker diagram is used for depicting groups of numerical data 
# through the quartiles. It is known as the box and whisker diagram because it is composed of a box and whiskers. Boxplot is also used for detecting the outlier in a data set.

# A box plot is composed of a summary of 5 different data points: 
# the minimum, first quartile, median, third quartile, and maximum.
# - Minimum
# - First Quartile or 25%
# - Median (Second Quartile) or 50%
# - Third Quartile or 75%
# - Maximum

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.boxplot(x="day", y="total_bill", data=tips)
# plt.show()

# The bottom black horizontal line of the box plot is the minimum value
# The first black horizontal line of the rectangle shape of the box plot is the first quartile
#  or 25%
# The second black horizontal line of the rectangle shape of the box plot is Second quartile or 50% or median.
# The third black horizontal line of rectangle shape of the same box plot is third quartile or 75%
# The top black horizontal line of the rectangle shape of the box plot is the maximum value.
# The small diamond shape of the box plot is outlier data.

#########################################################################

# Violin Plot
# Violin plots also like boxplots summarize numeric data over a set of categories. 
# They are essentially a box plot with a kernel density estimate (KDE) overlaid 
# along with the range of the box and reflected to make it look nice. 
# Unlike a box plot, in which all of the plot components correspond to actual data points, 
# the violin plot features a kernel density estimation of the underlying distribution. 

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.violinplot(x=tips["total_bill"])
# plt.show()

# sns.violinplot(x="day", y="total_bill", hue="smoker",
#                     data=tips, palette="muted")
# plt.show()

# # Now we can also represent the above plot like this by setting the parameter split as True:
# sns.violinplot(x="day", y="total_bill", hue="smoker",
#                     data=tips, palette="muted", split=True)
# plt.show()

#########################################################################

# Heatmap
# A heatmap is a two-dimensional graphical representation of data where the individual values 
# that are contained in a matrix are represented as colours. In Seaborn, we can make annotated 
# heatmaps which can be tweaked using Matplotlib as per requirement.

# Now if we get the data of the dataset ‘flights’ and transform it by monthly as shown below, 
# it can give us a lot of information about the data. But this information is in tabular form 
# and can be better displayed by using heatmap
# import seaborn as sns
# flights=sns.load_dataset("flights")
# flights = flights.pivot("month", "year", "passengers")
# print(flights)

# import seaborn as sns
# import matplotlib.pyplot as plt
# flights=sns.load_dataset("flights")
# flights = flights.pivot("month", "year", "passengers")
# sns.heatmap(flights,linewidths=.5,cmap="YlGnBu")
# plt.show()

# Now we can also put the respective values in the boxes using the annot parameter of this function
# import seaborn as sns
# import matplotlib.pyplot as plt
# car_crashes = sns.load_dataset("car_crashes")
# corr=car_crashes.corr()
# print(corr)
# sns.heatmap(corr,annot=True,linewidths=.5,cmap="YlGnBu")
# plt.show()

#########################################################################

# Cluster map
# Cluster map method plots a matrix dataset as a hierarchically-clustered heatmap. 
# It uses hierarchical clusters to order data by similarity. 
# This reorganizes the data for the rows and columns and displays similar content next to one another 
# for even more depth of understanding the data.

# import seaborn as sns
# import matplotlib.pyplot as plt
# flights=sns.load_dataset("flights")
# flights = flights.pivot("month", "year", "passengers")
# sns.clustermap(flights,linewidths=.5,cmap="coolwarm")
# plt.show()


# As you can see in this map all the columns and rows that have similar data together 
# and now neither the years nor the months are in order as we saw in the heatmap. 
# We can modify it a bit and only cluster rows or columns
# import seaborn as sns
# import matplotlib.pyplot as plt
# flights=sns.load_dataset("flights")
# flights = flights.pivot("month", "year", "passengers")
# sns.clustermap(flights,linewidths=.5,cmap="coolwarm",col_cluster=False)
# plt.show()

#########################################################################

# Facetgrid
# Facet grid forms a matrix of panels defined by row and column by dividing the variables. 
# Due to panels, a single plot looks like multiple plots. It is very helpful to analyze all combinations 
# in two discrete variables.

# The advantage of using Facet is, we can input another variable into the plot. 
# The above plot is divided into two plots based on a third variable called ‘diet’ using the ‘col’ parameter. 
# We can also one more parameter “row” which can help to add one more variable to our plot. 
# Now the plot below shows that relation between tips and total bill and also show their relation 
# with two more variables,i.e gender and time.

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# g = sns.FacetGrid(tips, col="time")
# g.map(sns.scatterplot, "total_bill", "tip")
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# g = sns.FacetGrid(tips, col="time", row="sex")
# g.map(sns.scatterplot, "total_bill", "tip")
# plt.show()

#########################################################################

# Pair Plot
# Pair plot creates a grid of Axes such that each numeric variable in data will be shared 
# across the y-axes across a single row and the x-axes across a single column. 
# The diagonal plots are treated differently: a univariate distribution plot is drawn to show 
# the marginal distribution of the data in each column.

# Pair Plots are a really simple way to visualize relationships between each variable. 
# It produces a matrix of relationships between each variable in your data for an instant examination 
# of our data.

# import seaborn as sns
# from matplotlib import pyplot as plt
# df = sns.load_dataset('iris')
# sns.set_style("ticks")
# sns.pairplot(df,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
# plt.show()

#########################################################################
#########################################################################
#########################################################################
#########################################################################

