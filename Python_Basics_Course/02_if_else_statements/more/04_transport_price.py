# In this exercise, important is arrangement of the logic!

#From a vineyard of X square meters, 40% of the harvest 
#is set aside for wine production. Y kilograms of grapes 
#are produced from 1 square meter of vineyard. 
#For 1 litre of wine 2,5 kg of grapes are needed. 
#The desired quantity of wine to sell is Z litres.
#Write a program that calculates how much wine can be produced 
#and whether this quantity is sufficient. If it is enough, 
#the remainder is split equally among the workers in the vineyard.

distance = int(input())
period = input()

taxi_day_rate = 0.79
taxi_night_rate = 0.90
bus_rate = 0.09
train_rate = 0.06

taxi_start_fee = 0.70
bus_min_distance = 20
train_min_distance = 100

#taxi_price = (taxi_day_rate if period == "day" else taxi_night_rate) * distance + taxi_start_fee
if period == "day":
    taxi_price = (taxi_day_rate * distance) + taxi_start_fee
else:
    taxi_price = (taxi_night_rate * distance) + taxi_start_fee
bus_price = bus_rate * distance
train_price = train_rate * distance

if distance >= train_min_distance:
    cheapest_option = min(taxi_price, bus_price, train_price)
elif distance >= bus_min_distance:
    cheapest_option = min(taxi_price, bus_price)
else:
    cheapest_option = taxi_price

print(f"{cheapest_option:.2f}")
