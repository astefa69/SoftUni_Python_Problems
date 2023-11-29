number_read = int(input())

# even: "even", e.g. 2, 4, 6, 8, 10,.... Even integers are even because when divided by 2, there is no reminder
#In mathematics, the remainder is the amount "left over" after performing some computation. In arithmetic, the remainder is the integer "left over" after dividing one integer by another to produce an integer quotient (integer division).
# 2:2 = 1 (remainder 0)
# 4:2 = 2 (remainder 0)
# 6:2 = 3 (remainder 0)
# odd: "odd"
if (number_read % 2) == 0: # == is operator for comparison, while = is operator for assigning value
    print("even")       #If True, executes print("even")
else:
    print("odd") # else, number_read % 2, != 0
                    #E.g. 5 % 2 = 1, != 0
                    # 5 : 2 = 2, remainder 1
                    #If False, executes print("odd")
                    #The else keyword catches anything which isn't caught by the preceding conditions.
#Checks
# 1024:2 = 521 (remainder 0) -> remainder = 0 -> even, and else is not executed
# 5:2 = 2 (remainder 1) -> remainder != 0 -> if is not executed, else is executed