hours = int(input())
mins = int(input())

mins_15 = mins + 15

# check if we need to add another hour if it is now after 23:45
if hours == 23 and mins >= 45:
    hours_15 = 0
    add_mins = mins_15 - 60
    print(f"{hours_15}:{add_mins:02d}")
elif mins_15 > 59:
    add_hours = mins_15 // 60 # divide by 60 to get how many hours to add
    add_mins = mins_15 - 60
    hours_15 = hours + add_hours
    print(f"{hours_15}:{add_mins:02d}")
else:
    print(f"{hours}:{mins_15:02d}")

#fails at, therefore added initial check for hours:
# if hours == 23 and mins >= 45:
#This was the wrong output:
#input	output
#23
#59	0:14
