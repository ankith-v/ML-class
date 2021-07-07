###########################################################################

# numpy.lower() : This function returns the lowercase string from the given string. 
# It converts all uppercase characters to lowercase. If no uppercase characters exist, it returns the original string.

# Python program explaining
# # numpy.lower() function
 
# import numpy as np
 
# # converting to lowercase
# print(np.char.lower(['npS', 'FOR']))
 
# # converting to lowercase
# print(np.char.lower('npS'))


# ###########################################################################

# numpy.split() : This function returns a list of strings after breaking the given string by the specified separator.

# # Python program explaining
# # numpy.split() function
 
# import numpy as np
 
# # splitting a string
# print(np.char.split('nps for nps'))
 
# # splitting a string
# print(np.char.split('nps, for, nps', sep = ','))


###########################################################################

# numpy.join() : This function is a string method and returns a string in 
# which the elements of sequence have been joined by str separator.

# # Python program explaining
# # numpy.join() function
 
# import numpy as np
 
# splitting a string
# print(np.char.join('-', 'nps'))
 
# # splitting a string
# print(np.char.join(['-', ':', '+'], ['nps', 'for', 'one']))

# ###########################################################################


# numpy.count() : This function returns the number of occurrences of a substring in the given string.

# # Python program explaining
# # numpy.count() function
 
# import numpy as np
 
# a=np.array(['nps', 'for', 'nps'])
 
# # counting a substring
# print(np.char.count(a,'np'))
 
# # counting a substring
# print(np.char.count(a, 'fo'))



###########################################################################



# numpy.rfind() : This function returns the highest index of the substring if found in given string. If not found then it returns -1.

# # Python program explaining
# # numpy.rfind() function
 
# import numpy as np
 
# a=np.array(['nps', 'for', 'nps'])
 
# # counting a substring
# print(np.char.rfind(a,'np'))
 
# # counting a substring
# print(np.char.rfind(a, 'fo'))

###########################################################################



# numpy.isnumeric() : This function returns “True” if all characters in the string are numeric characters, Otherwise, It returns “False”.

# # Python program explaining
# # numpy.isnumeric() function
 
# import numpy as np
 
 
# # counting a substring
# print(np.char.isnumeric('nps'))
 
# # counting a substring
# print(np.char.isnumeric('12nps'))

###########################################################################

# String Comparison –
# numpy.equal(): This function checks for string1 == string2 elementwise.

# # Python program explaining
# # numpy.equal() function
 
# import numpy as np
 
# # comparing a string elementwise
# # using equal() method
# a=np.char.equal('nps','for')
 
# print(a)


# ###########################################################################

# numpy.not_equal(): This function checks whether two string is unequal or not.

# # Python program explaining
# # numpy.unequal() function
 
# import numpy as np
 
# # comparing a string elementwise
# # using unequal() method
# a=np.char.not_equal('nps','for')
 
# print(a)

# ###########################################################################

# numpy.greater(): This function checks whether string1 is greater than string2 or not.

# # Python program explaining
# # numpy.greater() function
 
# import numpy as np
 
# # comparing a string elementwise
# # using greater() method
# a=np.char.greater('nps','for')
 
# print(a)

# ###########################################################################