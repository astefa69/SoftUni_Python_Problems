fuel_type = input() #"Diesel", "Gasoline" or "Gas"
fuel_liters = int(input()) # litres of fuel in the tank

#print
# If the litres of fuel are greater than or equal to 25,  print on the console
if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if fuel_liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")  # string.lower() if not formatted correctly, score 14/100
    # ако са по-малко от 25, да се отпечата
    else: #elif fuel_liters < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
# In the event that fuel other than that specified is specified, print
elif fuel_type != "Diesel" or fuel_type != "Gasoline" or fuel_type != "Gas": #else:
    print("Invalid fuel!")
