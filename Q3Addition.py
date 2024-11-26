# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

import random

x=random.randint(1,101)
y=random.randint(1,101)
print(x,"+",y)

try:

    d = input("enter your answer")
    g = (x + y)


    if int(d) == int(g):
     print("correct good work")
    else:
     print("answer incorrect")
     

except ValueError:
    print("use a whole number next time")
     

