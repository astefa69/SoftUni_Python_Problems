flower_sort = str(input())
flower_q = int(input())
budget = int(input())

flower_p = 0
discount = 1 #starting price correction multiplicator

if flower_sort == "Roses":
    flower_p = 5
    if flower_q > 80:
        discount = 0.9
elif flower_sort == "Dahlias":
    flower_p = 3.80
    if flower_q > 90:
        discount = 0.85
elif flower_sort == "Tulips":
    flower_p = 2.80
    if flower_q > 80:
        discount = 0.85
elif flower_sort == "Narcissus":
    flower_p = 3
    if flower_q < 120:
        discount = 1.15  # price correction, increase
elif flower_sort == "Gladiolus":    #else
    flower_p = 2.50
    if flower_q < 80:
        discount = 1.20  # price correction, increase

total_price = flower_p * flower_q * discount

# if flower_q > 80:
#     total_price *= 0.9
# elif flower_q > 90:
#     total_price *= 0.85
# elif flower_q > 80:
#     total_price *= 0.85
# elif flower_q < 120:
#     total_price *= 1.15
# elif flower_q < 80:
#     total_price *= 1.20

difference = abs(budget - total_price)

if budget - total_price >= 0:
    print(f"Hey, you have a great garden with {flower_q} {flower_sort} and {difference:.2f} leva left.")
elif budget - total_price < 0:
    print(f"Not enough money, you need {difference:.2f} leva more.")


# Alternative solution
# difference is only in presenting the discount as a discount per flower
# in the if construction:

flower_sort = str(input())
flower_q = int(input())
budget = int(input())

flower_p = 0

if flower_sort == "Roses":
    flower_p = 5
    if flower_q > 80:
        flower_p *= 0.9 # *= denotes that the variable on the left is multiplied by the number on the right
elif flower_sort == "Dahlias":
    flower_p = 3.80
    if flower_q > 90:
        flower_p *= 0.85
elif flower_sort == "Tulips":
    flower_p = 2.80
    if flower_q > 80:
        flower_p *= 0.85
elif flower_sort == "Narcissus":
    flower_p = 3
    if flower_q < 120:
        flower_p *= 1.15  # price correction, increase
elif flower_sort == "Gladiolus":    #else
    flower_p = 2.50
    if flower_q < 80:
        flower_p *= 1.20  # price correction, increase

total_price = flower_p * flower_q

difference = abs(budget - total_price) # With abs() I guarantee a positive value for the difference of two variables. 
# Thus, there is no need to do the same calculation twice to get the two print outputs.
if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_q} {flower_sort} and {difference:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {difference:.2f} leva more.")