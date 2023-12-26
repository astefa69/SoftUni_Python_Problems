days = int(input())
premise_type = str(input()) #"room for one person", "apartment" или "president apartment"
review = str(input())   #"positive"  или "negative"

adjustment_discount = 0
adjustment_review = 0
days -= 1 #the number of days you will stay at the hotel (example: 11 days = 10 nights)


if premise_type == "room for one person":
    price_daily = 18.00 #18.00 BGN per night
    if days >= 16: # more than 15 days
        adjustment_discount = 1 # 0%
    elif days >= 10:
        adjustment_discount = 1
    elif days < 10:
        adjustment_discount = 1
elif premise_type == "apartment":
    price_daily = 25.00 #25.00 BGN per night
    if days >= 16: # more than 15 days
        adjustment_discount = 0.50
    elif days >= 10:
        adjustment_discount = 0.65
    elif days < 10:
        adjustment_discount = 0.70 #30% of the final price
elif premise_type == "president apartment":
    price_daily = 35.00 #35.00 BGN per night
    if days >= 16: # more than 15 days
        adjustment_discount = 0.80
    elif days >= 10:
        adjustment_discount = 0.85
    elif days < 10:
        adjustment_discount = 0.90

if review == "positive":
    adjustment_review = 1.25
else:   # review == "negative"
    adjustment_review = 0.90

price = price_daily * days * adjustment_discount
price *= adjustment_review

print(f'{price:.2f}')