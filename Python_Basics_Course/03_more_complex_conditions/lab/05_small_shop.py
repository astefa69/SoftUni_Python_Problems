# Do a series of conditional statements, for each city check for the given product.
# In each check for a product, change the value of the variable price and print it.

products = str(input())
city = str(input())
quantity = float(input()) 

if city == "Sofia":
    p_coffee = 0.50
    p_water = 0.80
    p_beer = 1.20
    p_sweets = 1.45
    p_peanuts = 1.60
    if products == "coffee":
        print(p_coffee * quantity)
    elif products == "water":
        print(p_water * quantity)
    elif products == "beer":
        print(p_beer * quantity)
    elif products == "sweets":
        print(p_sweets * quantity)
    elif products == "peanuts":
        print(p_peanuts * quantity)
elif city == "Plovdiv":
    p_coffee = 0.40
    p_water = 0.70
    p_beer = 1.15
    p_sweets = 1.30
    p_peanuts = 1.50
    if products == "coffee":
        print(p_coffee * quantity)
    elif products == "water":
        print(p_water * quantity)
    elif products == "beer":
        print(p_beer * quantity)
    elif products == "sweets":
        print(p_sweets * quantity)
    elif products == "peanuts":
        print(p_peanuts * quantity)
elif city == "Varna":
    p_coffee = 0.45
    p_water = 0.70
    p_beer = 1.10
    p_sweets = 1.35
    p_peanuts = 1.55
    if products == "coffee":
        print(p_coffee * quantity)
    elif products == "water":
        print(p_water * quantity)
    elif products == "beer":
        print(p_beer * quantity)
    elif products == "sweets":
        print(p_sweets * quantity)
    elif products == "peanuts":
        print(p_peanuts * quantity)
############


# Solution 2
# price = 0   # new point

products = input()
city = input()
quantity = float(input())
price = 0   # initial price = 0. Each time the price will have a different value depending on the product.

if city == "Sofia":
    if products == "coffee":
        price = quantity * 0.50
    elif products == "water":
        price = quantity * 0.80
    elif products == "beer":
        price = quantity * 1.20
    elif products == "sweets":
        price = quantity * 1.45
    elif products == "peanuts":
        price = quantity * 1.60

if city == "Plovdiv":
    if products == "coffee":
        price = quantity * 0.40
    elif products == "water":
        price = quantity * 0.70
    elif products == "beer":
        price = quantity * 1.15
    elif products == "sweets":
        price = quantity * 1.30
    elif products == "peanuts":
        price = quantity * 1.50

if city == "Varna":
    if products == "coffee":
        price = quantity * 0.45
    elif products == "water":
        price = quantity * 0.70
    elif products == "beer":
        price = quantity * 1.10
    elif products == "sweets":
        price = quantity * 1.35
    elif products == "peanuts":
        price = quantity * 1.55

print(price)