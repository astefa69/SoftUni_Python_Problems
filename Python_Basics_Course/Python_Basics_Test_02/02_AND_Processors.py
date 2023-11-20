import math

time_per_processor = 3
hours_per_day = 8
price = 110.10 #ЕOne piece costs 110.10 BGN.

q_processors_est = int(input()) #number of processors
                            # to be produced - integer
q_employees = int(input())
q_work_days = int(input())

#Number of processors produced to be rounded to the nearest integer.
hours_worked = q_employees * q_work_days * hours_per_day
q_processors = math.floor(hours_worked / time_per_processor)
#revenue = q_processors * price
#revenue_est = q_processors_est * price

diff = abs(q_processors - q_processors_est)
result = diff * price

#If more or as much as planned:
if q_processors >= q_processors_est:
    print(f"Profit: -> {result:.2f} BGN") #profits
else: #if less than planned:
    print(f"Losses: -> {result:.2f} BGN") #losses
#Amounts must be formatted to the second decimal 