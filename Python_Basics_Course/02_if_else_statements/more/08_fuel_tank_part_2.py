#Write a program that calculates how much it will cost a driver to fill up the tank
# of his car, knowing - what type of fuel he is filling up,
# what is the cost per litre of fuel
# and whether he has a discount card.

#input
fuel_type = input() #Fuel type - string with options "Gas", "Gasoline" or "Diesel"
fuel_quantity = float(input()) #Fuel quantity - real number in the range [1.00 ... 50.00]
discount_card = input() #Club card - string with options "Yes" or "No"

#gasoline = 2.22 #gasoline - 2.22 BGN per liter,
# diesel = 2.33 #Diesel - 2.33 leva per liter
#gas = 0.93 #Gas - 0.93 BGN per litre
#price = 0

if discount_card == "No":
    if fuel_type == "Gas":
        price = 0.93
    elif fuel_type == "Gasoline":
        price = 2.22
    else: #elif fuel_type == "Diesel":
        price = 2.33
else:
    # If the driver has a discount card, they benefit from the following discounts per litre of fuel:
    # 18 cents per litre of petrol, 12 cents per litre of diesel and 8 cents per litre of gas.
    # gasoline_disc = 0.18
    # diesel_disc = 0.12
    # gas_disc = 0.08
    if fuel_type == "Gas":
        price = 0.93 - 0.08
    elif fuel_type == "Gasoline":
        price = 2.22 - 0.18
    else: #elif fuel_type == "Diesel":
        price = 2.33 - 0.12

#If the driver has filled up between 20 and 25 litres inclusive, he gets an 8 percent discount
# of the final price, if more than 25 litres of fuel, he receives a 10 percent discount on the final price.
if 20 <= fuel_quantity <= 25:
    discount = 0.92 #final_price = fuel_type * fuel_quantity * 0.92
elif fuel_quantity > 25:
    discount = 0.90 #final_price = fuel_type * fuel_quantity * 0.90
else:
    discount = 1

final_price = price * fuel_quantity * discount


#print
print(f"{final_price:.2f} lv.")
# Fuel price to be formatted to the second digit after the decimal.