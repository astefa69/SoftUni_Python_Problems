city = str(input())
sales = float(input())

commission = 0    # will be overwritten in the calculations below
                # initially assume we are at the beginning of the month,
                # we haven't made any sales, therefore we don't have any commissions

if city == "Sofia":
    if sales > 10000:
        commission = sales * 0.12
        print(f"{commission:.2f}")
    elif sales > 1000:
        commission = sales * 0.08
        print(f"{commission:.2f}")
    elif sales > 500:
        commission = sales * 0.07
        print(f"{commission:.2f}")
    elif sales > 0:
        commission = sales * 0.05
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if sales > 10000:
        commission = sales * 0.13
        print(f"{commission:.2f}")
    elif sales > 1000:
        commission = sales * 0.10
        print(f"{commission:.2f}")
    elif sales > 500:
        commission = sales * 0.075
        print(f"{commission:.2f}")
    elif sales > 0:
        commission = sales * 0.045
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if sales > 10000:
        commission = sales * 0.145
        print(f"{commission:.2f}")
    elif sales > 1000:
        commission = sales * 0.12
        print(f"{commission:.2f}")
    elif sales > 500:
        commission = sales * 0.08
        print(f"{commission:.2f}")
    elif sales > 0:
        commission = sales * 0.055
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")



#
# #Alternative solution, solved in  class
# #2:20
# #https://softuni.bg/trainings/resources/video/88519/video-16-september-202 3-марио-захариев-programming-basics-with-python-september-2023/4291
#
# city = str(input())
# sales = float(input())
#
# commission = 0

# error_data = False # variable that stores the boolean value "False"
#                   # and checks if wrong data for city, and sales volume will be entered.
#                   # When an error is detected, error_data will take the value "True"
#
# if city == "Sofia":
#     pass
# elif city == "Varna":
#     pass
# elif city == "Plovdiv":
#     pass
# else:       # in case the entered city is wrong.
#     error_data = True #if the city is not "Sofia", "Varna", "Plovdiv", "error_data" is activated and becomes True.
#                         # currently the "error_data" key is off until it hits the wrong date.
# if not error_data:   # if it's not "error_data", everything has passed through correctly, and I want to do print the sales commission
#     print(f"{commission:.2f}")
# else:       #if "error_data" = True, print error
#     print("error")