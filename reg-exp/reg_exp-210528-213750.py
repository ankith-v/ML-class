# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern
# Example:
# ^a...s$      # any five letter string starting with a and ending with s.

# Python has a module named re to work with RegEx.




# Example:
# import re

# pattern = '^a...s$'         #^ and $ are metacharacters
# test_string = 'abssp'
# result = re.match(pattern, test_string)

# if result:
#     print("Search successful.")
# else:
#     print("Search unsuccessful.")




# metacharacters - [] . ^ $ * + ? {} () \ |




# Example:
# import re

# pattern = '[abc]'        
# test_string = 'yhafbtg'
# pattern = '[^1-4]'        
# test_string = '73472985'
# result = re.match(pattern, test_string)

# if result:
#     print("Search successful.")
# else:
#     print("Search unsuccessful.")





# [a-e] is the same as [abcde]
# [1-4] is the same as [1234]
# [0-39] is the same as [01239].(0 to 3 and then 9)


# [^abc] means any character except a or b or c.
# [^0-9] means any non-digit character.


# Test-  https://regex101.com/




# Example: Period
# import re

# pattern = '...'        
# test_string = 'hrd'
# result = re.match(pattern, test_string)

# if result:
#     print("Search successful.")
# else:
#     print("Search unsuccessful.")




# Example: Caret - caret symbol ^ is used to check if a string starts with a certain character.
# import re

# pattern = '^a'        
# test_string = 'bant'
# result = re.match(pattern, test_string)

# if result:
#     print("Search successful.")
# else:
#     print("Search unsuccessful.")




# Example: Dollar - The dollar symbol $ is used to check if a string ends with a certain character.
# import re

# pattern = 'a$'      
# test_string = 'formula'
# # test_list = 'formula is c=a+b'
# result = re.search(pattern, test_string)
# # result1 = re.findall('is', test_list)

# if result:
#     print("Search successful.")
# else:
#     print("Search unsuccessful.")





# Function	Description
# findall	    Returns a list containing all matches
# search	    Returns a Match object if there is a match anywhere in the string
# split	        Returns a list where the string has been split at each match
# sub	        Replaces one or many matches with a string






# Example: Star - The star symbol * matches zero or more occurrences of the pattern left to it.
# import re

# pattern = 'ma*n'        
# test_string = 'sdma'
# # test_string = 'qwemaaanikl'
# result = re.findall(pattern, test_string)
# result1 = re.search(pattern, test_string)
# print("Result:",result)
# print("Result1:",result1.group())





# Example: Plus - The plus symbol + matches one or more occurrences of the pattern left to it. 
# import re

# pattern = 'ma+n'        
# # test_string = 'man'
# test_string = 'womaaaaaaaaaan'
# # test_string = 'maaanff'
# result = re.findall(pattern, test_string)
# result1 = re.search(pattern, test_string)
# print("Result:",result)
# print("Result1:",result1.group())





# Example: Question Mark - The question mark symbol ? matches zero or one occurrence of the pattern left to it. 
# import re

# pattern = 'ma?n'        
# # test_string = 'man'
# # test_string = 'maan'
# test_string = 'woman'
# result = re.findall(pattern, test_string)
# result1 = re.search(pattern, test_string)
# print("Result:",result)
# print("Result1:",result1.group())
    




# Example: Braces -  {n,m}. This means at least n, and at most m repetitions of the pattern left to it.
# import re

# pattern = 'a{2,3}'       
# test_string = 'abc daaaaaaaaaaaaat'
# # result1 = re.match(pattern, test_string)
# result2 = re.search(pattern, test_string)
# result3 = re.findall(pattern, test_string)
# # print("Result1:",result1)
# print("Result2:",result2.group())
# print("Result3:",result3)





# RegEx [0-9]{2, 4} 
# import re

# pattern = '[0-9]{2,4}'       
# test_string = 'ab12345878354263cd'

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# Alternation - Vertical bar | is used for alternation (or operator)
# import re

# pattern = 'a|b'       
# test_string = 'abcsfbfggadb'      #adabgh

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# Group - Parentheses () is used to group sub-patterns. 
# import re

# pattern = '(a|b|c)xz'       
# test_string = 'abcdxz'      #abxz  abcxz   abcdxz

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# Backslash
# \A - Matches if the specified characters are at the start of a string.
# import re

# pattern = '\Ain'       
# test_string = 'inthe  sun in'      

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \b - Matches if the specified characters are at the beginning or end of a word.
# import re

# # pattern = '\\bfoo'       
# # test_string = 'I like football playing football'      

# pattern = 'foo\\b'       
# test_string = 'I like afoo playingfoo football' 

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \B - Opposite of \b
# import re

# # pattern = '\\Bfoo'       
# # test_string = 'fooPlayinfoogballfoo'      #Playingfootball

# pattern = 'foo\\B'       
# test_string = 'fooPlayinfoo gballfoo'      #Playingfootball

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \d - Matches any decimal digit. Equivalent to [0-9]
# import re

# pattern = '\d'       
# test_string = 'ab453c'     #Python

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \D - Matches any non-decimal digit. Equivalent to [^0-9]
# import re

# pattern = '\D'       
# test_string = '12a5bc4'     #Python

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \s - Matches where a string contains any whitespace character.
# import re

# pattern = '\s'       
# test_string = '12 a b c4 okk'     

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \S - Matches where a string contains any non-whitespace character
# import re

# pattern = '\S'       
# test_string = '12 a bc 4j'     

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \w - Matches any alphanumeric character (digits and alphabets). 
# Equivalent to [a-zA-Z0-9_]. 
# By the way, underscore _ is also considered an alphanumeric character
# import re

# pattern = '\w'       
# test_string = '12 ab8_c/*ghf-4'     

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \W - Matches any non-alphanumeric character (digits and alphabets). 
# Equivalent to [^a-zA-Z0-9_]. 
# By the way, underscore _ is also considered an alphanumeric character
# import re

# pattern = '\W'       
# test_string = '12 a_bc*-4'     

# result = re.findall(pattern, test_string)
# print("Result: ",result)




# \Z - Matches if the specified characters are at the end of a string
# import re

# pattern = 'Python\Z'       
# test_string = 'Program Python ProgramPython'     

# result = re.findall(pattern, test_string)
# print("Result: ",result)




#split()
# import re

# pattern = '\d+'       
# test_string = 'Apple2 Banana8Banana8'     

# result = re.split(pattern, test_string)
# print("Result: ",result)




# sub() replace
# import re

# pattern = '\s+'       
# test_string = 'abc 12 def 34 gh 56'     
# replace ='*'

# result = re.sub(pattern, replace, test_string)
# print("Result: ",result)




# subn() replace count
# import re

# pattern = '\s+'       
# test_string = 'ah bc 12 def 34 gh 56'     
# replace ='8'

# result = re.subn(pattern, replace, test_string)
# print("Result: ",result)





# match.group()
# import re

# pattern = '(\d{2} \d{1})'       
# test_string = '78961 34567 3456'     

# match = re.search(pattern, test_string)
# # print("Match: ",match)

# if match:
#     print(match.group())
# else:
#     print("Pattern not found")





# The start() function returns the index of the start of the matched substring. 
# print(match.start())


# Similarly, end() returns the end index of the matched substring
# print(match.end())


# The span() function returns a tuple containing start and end index of the matched part.
# print(match.span())


# The re attribute of a matched object returns a regular expression object. 
# print(match.re)


# Similarly, string attribute returns the passed string.
# print(match.string)

