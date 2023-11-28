#Write a program that reads from the console the side and height of a triangle and
# calculates its face. Use the formula for the face of a triangle: area = a * h / 2.
# Format the output to the second decimal.

a = float(input())
h = float(input())

area = a * h / 2

print(f"{area:.2f}")