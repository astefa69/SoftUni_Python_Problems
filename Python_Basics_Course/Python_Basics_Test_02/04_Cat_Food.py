#100/100
price_per_kg = 12.45

q_group_one = 0
q_group_two = 0
q_group_three = 0

#price = 0
total_food = 0

q_cats = int(input())
for _ in range(q_cats):
    food = float(input())

    if 100 <= food < 200:
        q_group_one += 1
    elif food < 300:
        q_group_two += 1
    elif food < 400:
        q_group_three += 1

    total_food += food
price = total_food / 1000 * price_per_kg

#print
print(f"Group 1: {q_group_one} cats.") #number of cats in group 1: small cats
print(f"Group 2: {q_group_two} cats.") #number of cats in group 2: big cats
print(f"Group 3: {q_group_three} cats.") #number of cats in group 3: big cats
print(f"Price for food per day: {price:.2f} lv.") # price for the food
# Food price should be rounded to the second decimal.