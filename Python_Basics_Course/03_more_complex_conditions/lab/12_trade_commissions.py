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