# The Geometric Mean is a special type of average where we multiply the numbers 
# together and then take a square root (for two numbers), cube root (for three numbers) etc.




# Method 1: Simple Calculations to get the Geometric Mean
# multivalues = 8*16*22*12*41
# n = 5
# GM = (multivalues)**(1/n)
# print("GM:", GM)





# Method 2: Using a List to Derive the Geometric Mean in Python
# multiply = 1
# values = [8, 16, 22, 12, 41]
# n = len(values)

# for i in values:
#     multiply = (multiply)*(i)

# GM = (multiply)**(1/n)
# print("GM:", GM)





# Method 3: Using Scipy
# pip install scipy
# from scipy.stats.mstats import gmean
# arr = gmean([8, 16, 22, 12, 41])
# print("GM:", arr)






