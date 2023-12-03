# Logical exercise
# Conversions from seconds/meter to seconds for the whole distance !!
# math.floor !!
#if..else

#Calculate the time in seconds for Ivan to swim the distance
# and the difference to the World Record.
import math

time_record_secs = float(input())  # The record in seconds - a real number
distance_meters = float(input())  # Distance in meters - real number
time_ivan_secs_per_meter = float(input())   # Time in seconds to swim a distance of 1 m. - real number
#Water resistance slows it down every 15 m. by 12.5 seconds
# (Used when calculating how many times Ivan will slow down
# as a result of the resistance of the water.)

# The result should be rounded down to the nearest integer.
# Alternatively, integer division can be used without the need for another floor rounding:
# distance_meters // 15
# alternative two, int(distance_meters // 15)
time_slow_resistance_secs = math.floor(distance_meters / 15)
time_slow_resistance_secs = time_slow_resistance_secs * 12.5 # 12.5 secs slower every 15 meters

#Calculate the time in seconds that Ivan will
# swim the distance and the difference to the World Record.
time_ivan_secs = time_ivan_secs_per_meter * distance_meters
time_ivan_secs = time_ivan_secs + time_slow_resistance_secs
difference = time_ivan_secs - time_record_secs

# < , because the improved time must be less than the in the previous record, not equal.
if time_ivan_secs < time_record_secs:   # or difference < 0
    print(f"Yes, he succeeded! The new world record is {time_ivan_secs:.2f} seconds.")
else:   # time_ivan_secs >= time_record_secs
    print(f"No, he failed! He was {difference:.2f} seconds slower.")