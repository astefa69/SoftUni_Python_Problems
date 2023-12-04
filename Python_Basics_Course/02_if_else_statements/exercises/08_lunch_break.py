#During your lunch break, you want to watch an episode of your favourite show. 
#Your task is to write a program to find out if you have enough time 
#to watch the episode. During the break, you take time for lunch 
#and time for relaxation. The lunch time will be 1/8 of the break time 
#and the recreation time will be 1/4 of the break time. 
#Time to be rounded up to the nearest number!

from math import ceil

title_series = str(input())
duration_series = int(input())
duration_break = int(input())

# time_break = time_lunch + time_relax + x
duration_lunch = 1/8 * duration_break
duration_relax = 1/4 * duration_break

remaining_time = duration_break - duration_lunch - duration_relax

# difference = remaining_time - duration_series !
# absolute value !
difference = abs(remaining_time - duration_series)

#Time to be rounded up to the nearest number!
# absolute value !
difference = ceil(difference)

if remaining_time >= duration_series:
    print(f"You have enough time to watch {title_series} and left with {difference} minutes free time.")
else: #remaining time < duration_series
    print(f"You don't have enough time to watch {title_series}, you need {difference} more minutes.")