# easy
number = int(input())

if -100 <= number <= 100:
    if number != 0:
        print("Yes")
    else:
        print("No")
else: # 100 < number and number < -100
    print("No")

#Alternative solution
#from 03.PB-Python-Conditional-Statements-Advanced-Lab.docx

# number = int(input())
#
# if -100 <= number <= 100 and number!= 0:
#     print("Yes")
# else: # 100 < number and number < -100
#     print("No")