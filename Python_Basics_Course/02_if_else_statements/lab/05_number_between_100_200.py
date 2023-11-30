#Solutuin similar to https://python-book.softuni.org/chapter-03-simple-conditions.html
num = int(input())

# We make three validations, i.e. in which interval is the integer contained
# We make series of validations (two or more) for one variable
# We want only one validation to be correct

# < 100
# 100 <= number <= 200 # number in the interval 100 and 200 inclusive
# > 200

if num > 200:
    print("Greater than 200")
elif num >= 100:    # "=" is added, otherwise Judge returns wrong answe in pne of the checks.
                    # I suppose the check is for integer 100.
                    #100 should be included "Between 100 and 200", becausue it is not "Less than 100"
                    #"if the previous conditions were not true, then try this condition"
    print("Between 100 and 200")
else:   #All other cases which are not above, i.e. Less than 100
    print("Less than 100")


#Alternative solution from the lecture !!!
# number = int(input())
#
# if number < 100:
#     print("Less than 100")
# elif 100 <= number <= 200:
#     print ("Between 100 and 200")
# elif number > 200:
#     print ("Greater than 200")


#Alternative solution with else
# number = int(input())
#
# if number < 100:
#     print("Less than 100")
# elif 100 <= number <= 200:
#     print("Between 100 and 200")
# else:
#     print("Greater than 200")


#Alternative with ifs only
#Cons: we lose time to check each if.
# The construction if...elif, you pause when the check is True
#
# number = int(input())
#
# if number < 100:
#     print("Less than 100")
# if 100 <= number <= 200:
#     print("Between 100 and 200")
# if number > 200:
#     print("Greater than 200")