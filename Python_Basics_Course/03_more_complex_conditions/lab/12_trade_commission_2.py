# Alternative solution with "error_data = False" which works as a key
# takes the value "error_data = True" if the conditions entered with "if" are not satisfied.

city = str(input())
sales = float(input())

commission = 0
error_data = False # variable that stores the boolean value "False"
#                   # and checks if wrong data for city, and sales volume will be entered.
#                   # When an error is detected, error_data will take the value "True"


# advanced conditional statements:
# error_data = False if sales < 0 and city not in ['Sofia', 'Varna', 'Plovdiv'] else True

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:  # in case the entered Sales are wrong (the city may be valid)
        error_data = True
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13
    else:  # in case the entered Sales are wrong (the city may be valid)
        error_data = True

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:  # in case the entered Sales are wrong (the city may be valid)
        error_data = True
else:       #In case the entered City is wrong.
    error_data = True #If the city is not "Sofia", "Varna", "Plovdiv", "error_data" is activated and becomes True.
                         # Currently the "error_data" key is off until it hits the wrong date.
if not error_data:  # When it's not "error_data", print a sales commission.
    print(f"{commission:.2f}")
else:       #Otherwise if "error_data" = True, print error.
    print("error")