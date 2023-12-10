age = float(input())
sex = str(input())

if sex == "m":
    if age >= 16:
        print('Mr.')
    else:
        print('Master')
# sex == "f": # not "else" becasue it allows you to enter (and prints)
# all other cases, even not specified, e.g. allows you to
# enter and print 15, Gosho, results in Miss, which should not be the case !
elif sex == "f":
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')

#Alernative solution
#Condition statements on age, then condition statements on gender.
# age = float(input())
# sex = str(input())
#
# if age >= 16:
#     if sex =='m':
#         print('Mr.')
#     else: #sex == 'f':
#         print('Ms.')
# else: # age < 16
#     if sex =='m':
#         print('Master')
#     else: #sex == 'f':
#         print('Miss')