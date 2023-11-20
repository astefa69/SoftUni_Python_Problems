#100/100
price_toy = 5
price_pullover = 15

q_below_seventeen = 0
q_above_sixteen = 0
total_amount_toys = 0
total_amount_pullovers = 0

command = input()
while command != "Christmas":
    years = int(command)

    if years > 16:
        q_above_sixteen += 1
    else:
        q_below_seventeen += 1

    total_amount_pullovers = q_above_sixteen * price_pullover
    total_amount_toys = q_below_seventeen * price_toy

    command = input()

#print
print(f"Number of adults: {q_above_sixteen}") #number of people over 16 years
print(f"Number of kids: {q_below_seventeen}") #Number of people under 16 (incl.)
print(f"Money for toys: {total_amount_toys}") #the amount for all toys
print(f"Money for sweaters: {total_amount_pullovers}") #amount for all sweaters