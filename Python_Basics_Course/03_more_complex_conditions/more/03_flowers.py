q_hrizantemi = int(input())
q_roses = int(input())
q_lale = int(input())
season = input() #[Spring, Summer, Аutumn, Winter]
holiday = input() # [Y – yes / N - no]


p_hrizantemi = 0
p_roses = 0
p_lale = 0

#Flowershop offers 3 types of flowers: chrysanthemums, roses and tulips. Prices depend on the season.
if season == "Spring" or season == "Summer":
    p_hrizantemi = 2
    p_roses = 4.10
    p_lale = 2.50

elif season == "Autumn" or season == "Winter":
    p_hrizantemi = 3.75
    p_roses = 4.50
    p_lale = 4.15

# On festive days all flower prices increase by 15%.
if holiday == "Y":
    p_hrizantemi *= 1.15
    p_roses *= 1.15
    p_lale *= 1.15

total_price = q_hrizantemi * p_hrizantemi + q_roses * p_roses + q_lale * p_lale

# The following discounts are available:
# For purchases of more than 7 tulips in spring - 5% off the price of the entire bouquet.
if q_lale > 7 and season == "Spring":
    total_price *= 0.95

# For 10 or more roses purchased in winter - 10% off the entire bouquet.
if q_roses >= 10 and season == "Winter": # !!! >=
    total_price *= 0.90

# For purchases of more than 20 flowers in total in all seasons - 20% off the entire bouquet.
if q_hrizantemi + q_roses + q_lale > 20: #!!!
    total_price *= 0.80

#The price for arranging the bouquet is always 2lv.
total_price += 2 #!!!

#print
#Print one number on the console - the price of the flowers, formatted to the second decimal point.
print(f"{total_price:.2f}")