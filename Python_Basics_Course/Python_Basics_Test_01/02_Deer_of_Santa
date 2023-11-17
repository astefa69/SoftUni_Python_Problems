import math
number_days = int(input()) 
available_food = int(input())
food_deer_one = float(input())
food_deer_two = float(input())
food_deer_three = float(input())

food_consumed = number_days * (food_deer_one + food_deer_two + food_deer_three)
available_food -= food_consumed


#Print
#If delivered food is enough:
if available_food >= 0:
    available_food = abs(available_food)
    available_food = math.floor(available_food)
    print(f"{available_food} kilos of food left.") # килограми, които остават
#	Result to be rounded to the lower SMALLEST integer
else: #if delivered food is NOT enough:
    available_food = abs(available_food)
    available_food = math.ceil(available_food)
    print(f"{available_food} more kilos of food are needed.")
#	Result to be rounded to the HIGHER integer
