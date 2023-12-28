juniors_count = int(input())
seniors_count = int(input())
type_race = input()

if type_race == "trail":
    juniors_price = 5.50
    seniors_price = 7
elif type_race == "cross-country":
# If there are 50 or more participants in the "cross-country" race (junior and senior combined), the fee is reduced by 25%.
    if seniors_count + juniors_count >= 50:
        juniors_price = 8 * (1 - 0.25)
        seniors_price = 9.50 * (1 - 0.25)

    else:
        juniors_price = 8
        seniors_price = 9.50
elif type_race == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
elif type_race == "road":
    juniors_price = 20
    seniors_price = 21.50


amount_collected = juniors_count * juniors_price + seniors_count * seniors_price

#Organisers set aside 5% of the amount they collect for expenses.
amount_collected *= 0.95

#Print one number on the console:
# formatted to 2 decimal points.
print(f"{amount_collected:.2f}")
