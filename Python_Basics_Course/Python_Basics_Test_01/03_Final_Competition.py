number_dancers = int(input()) #1.	Брой танцьори – цяло число в интервала [1 … 10]
points = float(input()) #2.	Брой точки – реално число в интервала [1.00 … 10000.00]
season = input() #3.	Сезон –  текст със следните възможности - "summer" или "winter"
location = input() #4.	Място – текст със следните възможности - "Bulgaria" или "Abroad"

# charity_amount = 0
# amount_per_dancer = 0

if location == "Bulgaria":
    amount_all_dancers = points * number_dancers
    if season == "summer":
        amount_all_dancers *= (1 - 0.05)
    else: # elif == "winter"
        amount_all_dancers *= (1 - 0.08)
else:  #elif location == "Abroad":
    amount_all_dancers = points * number_dancers + 0.5 * (points * number_dancers)
    if season == "summer":
        amount_all_dancers *= (1 - 0.10)
    else: # elif == "winter"
        amount_all_dancers *= (1 - 0.15)

charity_amount = amount_all_dancers * 0.75
left_money = amount_all_dancers - charity_amount
amount_per_dancer = left_money / number_dancers
#amount_per_dancer = amount_all_dancers * 0.35 / number_dancers

#•	Ако състезанието се е провело в България паричната награда се изчислява
# като се умножат точките по броя участниците.
#•	Ако се е провело в чужбина –
# се умножават броя участници по броя точки и към тях се добавя 50% от получената сума.
#От получената сума се изваждат разходите посочени в проценти спрямо сезона, през който се е провел:
#След завръщането си групата дарява 75% от сумата, след приспаднатите разходи, за благотворителност.
# Останалата сума се разпределя между членовете на групата.


#print
#•	Сумата, която са дали за благотворителност
print(f"Charity - {charity_amount:.2f}") #сума за благотворителност
#•	Сумата, която е получил всеки танцьор
print(f"Money per dancer - {amount_per_dancer:.2f}") #сума за танцьор
#Сумите да бъдат форматирани до втория знак след десетичната запетая.
