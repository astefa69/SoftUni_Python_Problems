#Additional bonus points are awarded as per the rules described below.
# Write a program that calculates the bonus points for the given number and outputs the total points including the bonus.
#If the number is up to 100 inclusive, the bonus points are 5.
#If the number is larger than 100, the bonus points are 20% of the number.
#If the number is larger than 1000, the bonus points are 10% of the number.
#Additional points are awarded as below (added separately from the described above):
##For even numbers -> + 1 p.
##For numbers, ending with 5 -> + 2 p.

points = int(input())
bonus = 0

if points > 1000:
    bonus = 0.1 * points
elif points > 100:  #"if the previous conditions were not true, then try this condition"
    bonus = 0.2 * points
elif points <= 100:
    bonus = 5

if points % 2 == 0:
    bonus = bonus + 1

if str(points).endswith('5'):
    bonus = bonus + 2

print(bonus)
sum = bonus + points
print(sum)