budget = float(input())
season = input() #One of two possible seasons - "summer" or "winter".

price = 0
destination = "" #"Bulgaria", "Balkans" и "Europe"
accommodation = "" #"Camp" и "Hotel"

#Any campsite or hotel, depending on the destination,
# has its own price that corresponds to a percentage of the budget
if budget > 1000:
    price = budget * 0.90
    destination = "Europe"
    accommodation = "Hotel"
elif budget > 100:
    destination = "Balkans"
    if season == "summer":
      price = budget * 0.40
      accommodation = "Camp"
    elif season == "winter":
        price = budget * 0.80
        accommodation = "Hotel"
elif budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
      price = budget * 0.30
      accommodation = "Camp"
    elif season == "winter":
        price = budget * 0.70
        accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")
