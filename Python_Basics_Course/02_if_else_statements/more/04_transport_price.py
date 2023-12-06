# In this exercise, important is arrangement of the logic!

#A student has to travel n kilometres. He has a choice of three modes of transport:
#- Taxi. Start fare: 0.70 BGN. Daily fare: 0.90 BGN / km. Night fare: 0.90 / km.
#- Bus. Day/night fare: BGN 0.09 per km. / km. Can be used for distances of minimum 20 km.
#- Train. Day/night fare: BGN 0.06 per km. / km. Can be used for distances of minimum 100 km.
#Write a program that enters the number of kilometers n and the period of the day 
#(day or night) and calculates the price of the cheapest transport.
#Output: print on the console the lowest price for the specified read distance,
# formatted to the second digit after the decimal separator.

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
