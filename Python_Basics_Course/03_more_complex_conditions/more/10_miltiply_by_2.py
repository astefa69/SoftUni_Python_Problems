#Write a program to multiply positive numbers by 2.
# A sequence of real numbers is read from the console, each on a new line,
# until a negative one is entered. After each multiplied number on a new line
# print "Result: {the result of the multiplication}".
# The result of the multiplication to be formatted to the second digit after the decimal point.
# When a negative number is obtained, print "Negative number!" on the console and
# the program to terminate execution.

number = float(input())
while number >= 0:
    number *= 2
    print(f"Result: {number:.2f}")

    number = float(input())
else:
    print("Negative number!")