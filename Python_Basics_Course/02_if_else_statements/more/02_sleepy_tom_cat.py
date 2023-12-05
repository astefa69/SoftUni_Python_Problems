vacation_days = int(input())
business_days_play_time = 63 #mins per day
vacation_day_play_time = 127 #mins per day

target_play_time = 30_000 #Tom's playing time is 30 000 minutes per year

business_days = 365 - vacation_days
play_time_business_days_in_mins = business_days * business_days_play_time # annual in minutes
play_time_vacation_days_in_mins = vacation_days * vacation_day_play_time #annual in minutes
total_play_time_in_mins = play_time_business_days_in_mins + play_time_vacation_days_in_mins
difference_in_mins = abs(target_play_time - total_play_time_in_mins)
difference_in_hours = difference_in_mins // 60
difference_in_hours_remainder_in_mins = difference_in_mins % 60

#print:
#If Tom's playing time is above the limit for the current year:
if total_play_time_in_mins > target_play_time:
    print("Tom will run away")
    #On the second line print the difference from the limit in format:
    print(f"{difference_in_hours} hours and {difference_in_hours_remainder_in_mins} minutes more for play")
#If Tom's playing time is below the limit for the current year:
else: # target_play_time >= total_play_time_in_mins
    print("Tom sleeps well")
    #On the second line print the difference from the limit in format:
    print(f"{difference_in_hours} hours and {difference_in_hours_remainder_in_mins} minutes less for play")
