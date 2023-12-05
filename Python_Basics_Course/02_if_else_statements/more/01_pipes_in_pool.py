#The pool with volume V has two pipes from which it is filled.
# Each pipe has a certain flow rate (litres of water passing through one pipe in one hour).
# The worker runs the pipes simultaneously and leaves for N hours.
# Write a program that outputs the state of the pool the moment the worker returns.

v = int(input()) #pool volume in liters
p1 = int(input()) #debit of the first pipe per hour
p2 = int(input()) #debit of the second pipe per hour
h = float(input()) #hours the worker is away

liters_filled = (p1 + p2) * h # liters
filled_capacity = liters_filled / v * 100
percent_p1 = (p1 * h) / liters_filled * 100
percent_p2 = (p2 * h) / liters_filled * 100

diff = abs(liters_filled - v)



#print
#Print one of two possible states on the console:
#How much the pool has filled and which pipe contributed what percentage.

if v >= liters_filled: #!!! >=
    print(f"The pool is {filled_capacity:.2f}% full. Pipe 1: {percent_p1:.2f}%. Pipe 2: {percent_p2:.2f}%.")
#If the pool overflowed - by how many litres it overflowed in the given time.
else: #liters_filled > v
    print(f"For {h:.2f} hours the pool overflows with {diff:.2f} liters.")