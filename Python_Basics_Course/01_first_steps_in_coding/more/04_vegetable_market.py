#Sold are vegetables for N leva per kilo and fruits for M leva per kilo.
# Write a program that calculates the income from the harvest in euros
# (assuming that one euro is equal to 1.94BGN).

price_kg_vegetables = float(input())
price_kg_fruits = float(input())
quantity_vegetables = int(input())
quantity_fruits = int(input())

ex_rate_EUR_BGN = 1.94 #BGN/EUR

revenue_BGN = price_kg_vegetables * quantity_vegetables + price_kg_fruits * quantity_fruits
revenue_EUR = revenue_BGN / ex_rate_EUR_BGN

print(f"{revenue_EUR:.2f}")