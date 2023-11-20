#100/100
q_locations = int(input())

for location in range(q_locations):
    exp_avg_output_daily = float(input()) #expected average daily gold yield - real number
    q_days_production = int(input()) #number of days to mine at the given location - integer

    total_output = 0

    #For each day one number is read:
    # Gold mined for the day - real number
    for day in range(q_days_production):
        current_output = float(input())
        total_output += current_output

    # average yield per day for the given location
    average_yield_daily = total_output / q_days_production

    # gold not enough to reach the expected average yield
    diff = abs(exp_avg_output_daily - average_yield_daily)

    #On completion of mining at a location, a line is printed as appropriate:
    #If the average daily gold production meets or exceeds the expected average daily gold production:
    if average_yield_daily >= exp_avg_output_daily:
        print(f"Good job! Average gold per day: {average_yield_daily:.2f}.") #average yield per day for the given location
    else: #If the average gold production per day is below the expected average gold production per day:
        print(f"You need {diff:.2f} gold.") #gold not enough to reach the expected average yield
    # Result to be formatted to the second character after the decimal sign.