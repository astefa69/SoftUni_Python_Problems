budget = float(input()) # floating-point number (fractional number)
mass = int(input()) # integer
price_cloth = float(input())

decor = 0.1 * budget

if mass > 150:
    discount = 0.1 * price_cloth
else:
    discount = 0

cost = decor + (price_cloth - discount) * mass
result = cost - budget

import os
if result > 0:
    print("Not enough money!",
          f"Wingard needs {result:.2f} leva more.",
          sep=os.linesep)
else:   # result <= budget
    result = abs(result)        # absolute number !
    print("Action!",
          f"Wingard starts filming with {result:.2f} leva left.", sep=os.linesep)