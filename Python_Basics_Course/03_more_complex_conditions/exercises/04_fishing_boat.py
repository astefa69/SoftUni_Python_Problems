budget = int(input())
season = input(str())
fishers_count = int(input())

rent = 0
discount = 1
add_discount = 1

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishers_count <= 6:
    discount = 0.9  #discount of 10%;
elif 7 <= fishers_count <= 11:  # !!! elif fishers_count <= 11. This is possible because the first check has already excluded the cases <= 6
    discount = 0.85 #отстъпка от 15%;
elif fishers_count >= 12: # else
    discount = 0.75 # отстъпка от 25%.

# additional discount for even number of fishermen and season other than autumn
if fishers_count % 2 == 0:
    if season != "Autumn": #if season == "Spring" or season == "Summer" or season == "Winter"
        add_discount = 0.95 #additional 5% discount if even number,
                            # unless it's fall - then no additional discount,
                            #which is applied after the discount under the previous criteria.

cost = rent * discount * add_discount

difference = abs(budget - cost)

if budget >= cost: #If the budget is sufficient
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < cost:	#If the budget is NOT sufficient
    print(f"Not enough money! You need {difference:.2f} leva.")



# Solution 2
# The difference is that this solution uses rent *= instead of variable 'discount'
#
# budget = int(input())
# season = input(str())
# fishers_count = int(input())
#
# rent = 0
# discount = 1
# add_discount = 1
#
# if season == "Spring":
#     rent = 3000
# elif season == "Summer" or season == "Autumn":
#     rent = 4200
# elif season == "Winter":
#     rent = 2600
#
# if fishers_count <= 6:
#     rent *= 0.9  #discount of 10%;
# elif fishers_count <= 11: 
#     rent *= 0.85 #discount of 15%;
# elif fishers_count >= 12: # else
#     rent *= 0.75 # discount of 25%.
#
# # additional 5% discount if even number
# if fishers_count % 2 == 0 and season != "Autumn": #if season == "Spring" or season == "Summer" or season == "Winter"
#         rent *= 0.95  #additional 5% discount if even number
#
# difference = abs(budget - rent)
#
# if budget >= rent:
#     print(f"Yes! You have {difference:.2f} leva left.")
# elif budget < rent:
#     print(f"Not enough money! You need {difference:.2f} leva.")