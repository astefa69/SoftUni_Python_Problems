number_dancers = int(input()) 
points = float(input()) 
season = input() 
location = input()

# charity_amount = 0
# amount_per_dancer = 0

if location == "Bulgaria":
    amount_all_dancers = points * number_dancers
    if season == "summer":
        amount_all_dancers *= (1 - 0.05)
    else: # elif == "winter"
        amount_all_dancers *= (1 - 0.08)
else:  #elif location == "Abroad":
    amount_all_dancers = points * number_dancers + 0.5 * (points * number_dancers)
    if season == "summer":
        amount_all_dancers *= (1 - 0.10)
    else: # elif == "winter"
        amount_all_dancers *= (1 - 0.15)

charity_amount = amount_all_dancers * 0.75
left_money = amount_all_dancers - charity_amount
amount_per_dancer = left_money / number_dancers
#amount_per_dancer = amount_all_dancers * 0.35 / number_dancers


#print
print(f"Charity - {charity_amount:.2f}")
print(f"Money per dancer - {amount_per_dancer:.2f}")
