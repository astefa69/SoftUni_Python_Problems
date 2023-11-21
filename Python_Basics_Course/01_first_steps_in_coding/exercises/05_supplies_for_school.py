pens = int(input())
markers = int(input())
liquid = int(input())
discount_percent = int(input())

pens_total_price = pens * 5.80
markets_total_price = markers * 7.20
liquid_total_price = liquid * 1.20

#use backslash to \
Total_amount = (pens_total_price + \
                markets_total_price + \
                liquid_total_price) * \
               (1-discount_percent/100)
print(Total_amount)

#rounding in this example is not required!
#rounding
#print(f"{Total_amount:.2f}")
#print(round(Total_amount))