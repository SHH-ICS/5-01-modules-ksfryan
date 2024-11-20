# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.

import math

a = float(input("enter your a leg :"))
b = float(input("enter your b leg :"))
c = math.sqrt(a**2 + b**2)

print("The lengh of your hypotenuse:")
print(c)
