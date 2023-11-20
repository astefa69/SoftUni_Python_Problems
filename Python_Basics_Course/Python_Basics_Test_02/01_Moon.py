#100/100
import math
time_spent = 3
s = 384_400 * 2
v = float(input()) #average speed - real number
liters_per_100_km = float(input())

time = s / v
total_time = time + time_spent
liters = s * liters_per_100_km / 100


print(f"{math.ceil(total_time)}")
#•	litres of fuel needed for the journey
print(int(liters))

####
import math
time_spent = 3
s = 384_400 * 2
v = float(input()) #average running speed - real number
liters_per_100_km = float(input())

time = s / v
total_time = time + time_spent
liters = s * liters_per_100_km / 100

#print
#•	The number of hours for which George has travelled and returned
# (round the result to the largest whole number).
print(f"{math.ceil(total_time)}")
#•	The amount of litres of fuel needed for the journey.
print(int(liters))
