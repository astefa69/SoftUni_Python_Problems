points = int(input())
#initiate new variable 'bonus' to accrue the bonus points
bonus = 0   

#if-elif construction
if points > 1000:
    bonus = 0.1 * points
    total_points = points * 1.1 # 0.1 * points + points = 1.1 * points
elif points > 100:
    bonus = 0.2 * points
    total_points = points * 1.2
else:
    bonus = 5
    total_points = points + bonus

#if statement to calculate the additional bonus
#check if a number is even you need to % divide it by 2
#"modulo 2" (odd/even) operation
if points % 2 == 0:
    bonus = bonus + 1
    total_points = total_points + 1

# check if a number ends in digit 5
#alternatively, modular division can also be used here: if number % 10 == 5:
if str(points).endswith('5'):
    bonus = bonus + 2
    total_points = total_points + 2

print(bonus)
print(total_points)




#Alternative solution (in class)
number = int(input())
bonus_points = 0
if number <= 100:
    bonus_points += 5 # bonus_points + 5 !!!
                        # -=
                        # *=
                        # /=
                        # //=
elif number > 1000:  # alternative:  elif  100 < bonus <= 1000:
    bonus_points += number * 0.1    # number * 10 / 100
else:   # 100 < bonus <= 1000
    bonus_points += number * 0.2  # number * 20 / 100

if number % 2 == 0:
    bonus_points += 1

if number % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(number + bonus_points)