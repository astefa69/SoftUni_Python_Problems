#Maria wants to buy her son a present. She works in a flower shop. An order for flowers comes into the shop.
# Write a program that calculates the amount of the order and whether the profit is enough to buy the present.

#input
import math

q_magnolias = int(input()) #Number of magnolias - integer in the range [0 ... 50]
q_hyacinths = int(input()) #Number of hyacinths - integer in the range [0 ... 50]
q_roses = int(input()) #Number of roses - integer in the range [0 ... 50]
q_acti = int(input()) #Number of cacti - integer in the range [0 ... 50]
price_of_present = float(input()) #Price of the present - real number in the range [0.00 ... 500.00]

p_magnolias = 3.25 #Magnolias - 3.25 BGN
p_hyacinths = 4 #hyacinths - 4 BGN
p_roses = 3.50 #Roses - 3.50 BGN
p_acti = 8 #Cacti - 8 BGN

#calculations

revenue = q_magnolias * p_magnolias + q_hyacinths * p_hyacinths + q_roses * p_roses + q_acti * p_acti
revenue *= 0.95 #Of the total amount, Maria has to pay 5% taxes
diff = abs(price_of_present - revenue)

#print
#If the money IS enough:
if revenue >= price_of_present: # >= !
    print(f"She is left with {math.floor(diff)} leva.") #The amount must be rounded to a smaller integer (e.g. 1.90 -> 1).
#If the money is NOT enough:
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.") #The amount must be rounded to a larger integer (e.g. 1.90 -> 1).
