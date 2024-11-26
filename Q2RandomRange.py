# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.

import random
a = float(input("first number :"))
b = float(input("second number :"))

random_number = random.uniform(a,b)
print (random_number)

