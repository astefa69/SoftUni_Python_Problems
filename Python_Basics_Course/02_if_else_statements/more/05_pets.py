#input
import math

days = int(input()) #number of days - integer in range [1...5000]
food_reserved = int(input()) #food stored in kg - integer in the interval [0...100000]
food_dog_daily = float(input())#food per day for the dog in kg - real number in the interval [0.00...100.00]
food_cat_daily = float(input()) #food per day for the cat in kilograms- real number in the interval [0.00...100.00]
food_turtle_daily = float(input()) #food per day for the turtle in grams - real number in the interval [0.00...10000.00]

#calculations
food_needed = days * (food_dog_daily + food_cat_daily + food_turtle_daily)

diff = abs(food_reserved - food_needed)

#print
#If the stored food IS enough:
if food_reserved >= food_needed:
    print(f"{math.floor(diff)} kilos of food left.") #kilograms leftover
#The result should be rounded to the lower integer
#If the food left is NOT enough:
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.") #kilograms fall short
#Result should be rounded to the higher integer
