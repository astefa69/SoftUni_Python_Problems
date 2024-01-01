#Write a program that calculates the price, type and class of a rental car according to a given budget and season.
#The seasons are summer and winter - "Summer" and "Winter". Car types are convertible and jeep - "Cabrio" and "Jeep".
budget = float(input()) #real number in the range [10.00...10000.00]
season = input() #Season – string "Summer" or "Winter"
class_type = "" #"Economy class", "Compact class" or "Luxury class"
car_type= "" #Car type - "Cabrio" or "Jeep"
price = 0

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = 0.35 * budget
    else:# elif season == "Winter":
        car_type = "Jeep"
        price = 0.65 * budget
        pass
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = 0.45 * budget
    else:# elif season == "Winter":
        car_type = "Jeep"
        price = 0.80 * budget
        pass
elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    price = 0.9 * budget

#print
#Two lines should be printed on the console.
print(f"{class_type}") #Class type: "Economy class", "Compact class" or "Luxury class"
print(f"{car_type} - {price:.2f}") #car price
#Price must be formatted to the second decimal point
