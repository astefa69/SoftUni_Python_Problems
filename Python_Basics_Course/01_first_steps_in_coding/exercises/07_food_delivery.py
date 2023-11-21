count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
meal_price = chicken_menu_price * count_chicken_menu +\
             fish_menu_price * count_fish_menu +\
             count_vegetarian_menu * vegetarian_menu_price
desert_price = meal_price * 0.20
delivery_price = 2.50
total_meal_price = meal_price + desert_price + delivery_price

print(total_meal_price)
# printed answer is 173.37999999999997 not 173.38. Still 100/100 in Judge !