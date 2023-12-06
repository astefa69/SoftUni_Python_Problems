import math

x = int(input()) # sq.m is the vineyard - integer
y = float(input()) # # y grapes per sq.m - float number in the range [0.00 ... 10.00]
z = int(input()) # z liters of wine needed - integer in the range [10 ... 600]
employees_count = int(input()) #брой работници – цяло число в интервала [1 … 20]

percent_to_produce_wine = 0.40 #40% of the harvest for wine production
grapes_to_produce_one_liter_wine = 2.5 #For 1 litre of wine you need 2.5 kg of grapes

produced_grapes = percent_to_produce_wine * x * y
produced_wine_in_liters = produced_grapes / grapes_to_produce_one_liter_wine
difference = abs(produced_wine_in_liters - z)

#print
#If the wine produced is less than required:
if produced_wine_in_liters < z:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
#The result should be rounded to the lower whole number

else: #If the wine produced is as much or more than needed:
    print(f"Good harvest this year! Total wine: {math.floor(produced_wine_in_liters)} liters.")
    #The result should be rounded to the lower whole number

    #If there is enough, the remainder is divided equally among the workers of the vineyard.
    # Both results should be rounded to the higher integer
    wine_in_liters_per_person = difference / employees_count
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_in_liters_per_person)} liters per person.") #вино за 1 работник
