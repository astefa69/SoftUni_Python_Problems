#Write a program that calculates whether the remaining money from the budget can
# buy tickets for the chosen category. And how much money they will be left or needed.

budget = float(input())
ticket_category = input()
group_count = int(input())

# Tickets have two categories with different prices:
if ticket_category == "VIP":
    ticket_price = 499.99
else:
    ticket_price = 249.99


#percentage of the budget should be allocated to transport
# remaining budget after deduction of transport costs
if group_count >= 50:
    budget *= (1 - 0.25)
elif group_count >= 25:
    budget *= (1 - 0.40)
elif group_count >= 10:
    budget *= (1 - 0.50)
elif group_count >= 5:
    budget *= (1 - 0.60)
elif group_count >= 1:
    budget *= (1 - 0.75)

total_price = ticket_price * group_count # ticket_price * group_count ! to get a price for the whole group
diff = abs(budget - total_price)

#print
#If the budget is sufficient:
if budget >= total_price:
    print(f"Yes! You have {diff:.2f} leva left.") #the remaining money of the group
#If the budget is NOT sufficient:
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
#Amounts must be formatted to two decimals.