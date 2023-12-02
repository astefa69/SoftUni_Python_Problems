#Write a program to calculate whether one will have enough money to go on a trip 
#after selling distinct quantity of set of products
#Two if...else statements one after another

pVacation = float(input()) #price vacation
qPuzzels = int(input()) # quantity puzzels
qDolls = int(input()) #quantity dolls
qBears = int(input()) #quantity bears
qMinions = int(input()) #quantity minions
qTrucks = int(input()) #quantity trucks

pPuzzel = 2.60
pDoll = 3
pBear = 4.10
pMinion = 8.20
pTruck = 2

# Option + Shift + 7 is backslash
total_order_quantity = qPuzzels + qDolls + qBears + qMinions + qTrucks
total_order_revenue= qPuzzels * pPuzzelçqDolls * pDoll \
                    + qBears * pBear \
                    + qMinions * pMinion \
                    + qTrucks * pTruck
#If discount applies
if total_order_quantity >= 50:      # "If ordered toys are 50 or more"
    discount = 0.25 * total_order_revenue
else:
    discount = 0

total_order_revenue_after_discount = total_order_revenue - discount
rent = total_order_revenue_after_discount * 0.1
total_order_revenue_after_discount_less_rent = total_order_revenue_after_discount - rent
result = total_order_revenue_after_discount_less_rent - pVacation

#if result >= 0
if result >= 0:     # !!! ">=" -> "To calculate whether she will have enough money to go on a trip"
    print(f"Yes! {result:.2f} lv left.")
else:
    result = abs(result)
    print(f"Not enough money! {result:.2f} lv needed.")
