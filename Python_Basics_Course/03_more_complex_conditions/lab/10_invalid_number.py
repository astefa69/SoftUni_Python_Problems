# number_integer = int(input())
#
# if number_integer == 0 or 100 <= number_integer <= 200:
#     print("")
# else:
#     print("invalid")


# Alternative solution in 03.PB-Python-Conditional-Statements-Advanced.pptx
number = int(input())
valid = 100 <= number <= 200 or number == 0
if not valid:
    print('invalid')
