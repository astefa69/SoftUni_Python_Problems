season = input() #Season - string "Spring", "Summer", "Autumn" or "Winter"
km_per_month = float(input())  #Kilometers per month - float in the range [10.00...20000.00]

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary_per_km = 0.75 # lv/km.
    elif season == "Summer":
        salary_per_km = 0.90 # lv/km.
    else:  # season == "Winter"
        salary_per_km = 1.05 # lv/km.
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary_per_km = 0.95 # lv/km.
    elif season == "Summer":
        salary_per_km = 1.10 # lv/km.
    else:  # season == "Winter"
        salary_per_km = 1.25 # lv/km.
elif 10000 < km_per_month <= 20000:
    salary_per_km = 1.45 # lv/km.

#After the 10% is taken out for taxes the remaining amount is printed.
salary = km_per_month * salary_per_km * 4 * (1 - 0.1)  # 4 months in one season !!!

#print
# The driver's salary after taxes, formatted to two decimal points.
print(f"{salary:.2f}")