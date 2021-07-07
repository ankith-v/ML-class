# Password generator using for loop
import random as random
character = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"

length = int(input("Enter Password length:"))
password = ""


for i in range(length):
    # password = password+random.choice(character)
    password += random.choice(character)
print(password)









# Password generator using join
import random


character = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"

length = int(input("Enter Password length:"))
password = ""


password2 = password.join(random.sample(character, length))
print(password2)








# Password generator with string
import random
import string


character = string.ascii_uppercase + string.ascii_lowercase + string.digits 


length = int(input("Enter Password length:"))
password = ""


for i in range(length):
    password += random.choice(character)
print(password)


