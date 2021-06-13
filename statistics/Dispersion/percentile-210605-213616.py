# Percentile: the value below which a percentage of data falls


# 16
# Example: You are the fourth tallest person in a group of 20
# 80% of people are shorter than you:


# That means you are at the 80th percentile.
# If your height is 1.85m then "1.85m" is the 80th percentile height in that group.






# Grouped Data
# When the data is grouped:

# Add up all percentages below the score,
# plus half the percentage at the score.





# 17
# Example: You Score a B!
# In the test 12% got D, 50% got C, 30% got B and 8% got A


# You got a B, so add up

# all the 12% that got D,
# all the 50% that got C,
# half of the 30% that got B,
# for a total percentile of 12% + 50% + 15% = 77%

# In other words you did "as well or better than 77% of the class"

# (Why take half of B? Because you shouldn't imagine you got the "Best B", or the "Worst B", 
# just an average B.)






# 18
# Deciles
# Deciles are similar to Percentiles (sounds like decimal and percentile together), 
# as they split the data into 10% groups:

# The 1st decile is the 10th percentile (the value that divides the data so 10% is below it)
# The 2nd decile is the 20th percentile (the value that divides the data so 20% is below it)
# etc!




# Example: Shopping
# A total of 10,000 people visited the shopping mall over 12 hours:

# Time (hours)	People
#     0       	0
#     2         350
#     4	        1100
#     6	        2400
#     8	        6500
#     10	    8850
#     12	    10,000
# a) Estimate the 30th percentile (when 30% of the visitors had arrived).
# b) Estimate what percentile of visitors had arrived after 11 hours.





# 19
# First draw a line graph of the data: plot the points and join them with a smooth curve:

# a) The 30th percentile occurs when the visits reach 3,000.
# 19a
# Draw a line horizontally across from 3,000 until you hit the curve, then draw a line vertically 
# downwards to read off the time on the horizontal axis:



# So the 30th percentile occurs after about 6.5 hours.

 

# b) To estimate the percentile of visits after 11 hours: draw a line vertically up from 11 
# until you hit the curve, then draw a line horizontally across to read off the population on the vertical axis:
# 19b


# So the visits at 11 hours were about 9,500, which is the 95th percentile.






# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# print(sorted(ages))

# What is the 75. percentile?




# import numpy
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# x = numpy.percentile(ages, 75)
# print(x)




