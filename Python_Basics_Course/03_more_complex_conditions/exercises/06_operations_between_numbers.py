# Solution 1
# Series of if, elif statements.
# When we have a division and a modulo division, the first thing we do is
# check if the divisor N2 is not equal to 0 and only then we divide.
#(Modulo operation returns the remainder of a division.)

N1 = int(input())
N2 = int(input())
operator = input() #one symbol among: "+", "-", "*", "/", "%".

result = 0  #defined here because it will be used throughout the code
remainder = 0   # verification for even_odd

if operator == "+":
    result = N1 + N2
    remainder = result % 2 # check whether the result is odd or even
    if remainder == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_odd}")  #the printing is added to each case

elif operator == "-":
    result = N1 - N2
    remainder = result % 2 # check whether the result is odd or even
    if remainder == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_odd}")

elif operator == "*":
    result = N1 * N2
    remainder = result % 2 # check whether the result is odd or even
    if remainder == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_odd}")

elif operator == "/":   #case "/" added,not given in the text
    if N2 != 0:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
    elif N2 == 0:
        print(f"Cannot divide {N1} by zero")
elif operator == "%":   #case "/" added,not given in the text
    if N2 != 0:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
    elif N2 == 0:
        print(f"Cannot divide {N1} by zero")
#
# if operator == "+":
#     print(f"{N1} {operator} {N2} = {result} - {even_odd}")
# elif operator == "/":
#     if N2 != 0:
#         print(f"{N1} / {N2} = {result:.2f}")
#     elif N2 == 0:
#         print(f"Cannot divide {N1} by zero")
# elif operator == "%":
#     if N2 != 0:
#         print(f"{N1} % {N2} = {remainder}")
#     elif N2 == 0:
#         print(f"Cannot divide {N1} by zero")
##############



# Solution 2 - in class
# Checks if the operation is +, -, * because the same message will be printed.
# Combines division and modulo division into one if statement.

N1 = int(input())
N2 = int(input())
operator = input() #един символ измежду: "+", "-", "*", "/", "%".

result = 0  #defined here because it will be used throughout the code

if operator == "+" or operator == "-" or operator == "*":
    even_odd = 0  # check for even_odd. Added here, not at the top, because it is only used in this code snippet.
    if operator == "+":
        result = N1 + N2
    elif operator == "-":
        result = N1 - N2
    elif operator == "*":   # else
        result = N1 * N2

    if result % 2 == 0: # check whether the result is odd or even
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_odd}")

elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:   # N2 != 0:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":   #else
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:  # N2 != 0:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")