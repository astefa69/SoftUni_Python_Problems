#Write a program that reads a number r from the console and calculates and prints it
# the face and perimeter of a circle/circle of radius r, formatting the output as follows:
# "<calculated area>"
#"<calculated parameter>".
# Format the output to the second decimal.
import math

r = float(input())

#source:https://csharp-book.softuni.bg/Content/Chapter-2-1-simple-calculations/numerical-expressions/examples-numerical-expressions/circle-area-and-perimeter.html
#Area = π * r * r
#Perimeter = 2 * π * r

area = math.pi * r * r
perimeter = 2 * math.pi * r

print(f"{area:.2f}")
print(f"{perimeter:.2f}")
