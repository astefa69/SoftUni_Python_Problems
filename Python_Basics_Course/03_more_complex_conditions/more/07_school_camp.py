season = input() # “Winter”, “Spring” or “Summer”;
type_of_group = input() #“boys”, “girls” or “mixed”;
students_count = int(input()) #integer in the range [1 … 10000];
nights_count = int(input()) # integer in the range [1 … 100].

nights_price = 0
sport = ""

if season == "Winter":
    if type_of_group == "boys":
        nights_price = 9.60
        sport = "Judo"
    elif type_of_group == "girls":
        nights_price = 9.60
        sport = "Gymnastics"
    else:
        nights_price = 10
        sport = "Ski"
elif season == "Spring":
    if type_of_group == "boys":
        nights_price = 7.20
        sport = "Tennis"
    elif type_of_group == "girls":
        nights_price = 7.20
        sport = "Athletics"
    else:
        nights_price = 9.50
        sport = "Cycling"
else: #elif season == "Summer"
    if type_of_group == "boys":
        nights_price = 15
        sport = "Football"
    elif type_of_group == "girls":
        nights_price = 15
        sport = "Volleyball"
    else:
        nights_price = 20
        sport = "Swimming"

price = nights_count * nights_price * students_count

#discounts
#The school receives a discount on the final price, depending on the number of students staying at the hotel:
# If the number of students is 50 or more, the school receives a 50% discount
if students_count >= 50:
    price = (1 - 0.5) * price
# Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
elif 20 <= students_count < 50:
    price = (1 - 0.15) * price
# If the number of students is 20 or more and at the same time less than 50, the school receives a 15% discount
elif 10 <= students_count < 20:
    price = (1 - 0.05) * price

#print
# The sports the students practiced and the cost of the accommodation the school paid,
# formatted to two decimal points, in the following format:
print(f"{sport} {price:.2f} lv.")
