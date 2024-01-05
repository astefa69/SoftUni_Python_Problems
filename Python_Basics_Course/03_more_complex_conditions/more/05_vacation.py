#Write a program to calculate the price for a given budget and season,
# the location and accommodation for a holiday.

budget = float(input()) #float number in the interval [10.00...10000.00]
season = input() #string "Summer" or "Winter"

# location #Alaska" и "Morocco"
# accomodation #"Hotel", "Hut" or "Camp".
# price

if budget <= 1000:
    accomodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65 * budget
    else: #season == "Winter"
        location = "Morocco"
        price = 0.45 * budget
if 1000 < budget <= 3000:
    accomodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.80 * budget
    else: #season == "Winter"
        location = "Morocco"
        price = 0.60 * budget

if budget > 3000:
    accomodation = "Hotel"
    price = 0.9 * budget
    if season == "Summer":
        location = "Alaska"
    else: #season == "Winter"
        location = "Morocco"


#print
print(f"{location} - {accomodation} - {price:.2f}")
