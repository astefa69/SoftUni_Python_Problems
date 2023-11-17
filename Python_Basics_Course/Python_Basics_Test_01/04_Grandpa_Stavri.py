number_days = int(input())

total_liters = 0
total_degrees = 0
#average_degrees = 0

for day in range(1, number_days + 1):
    q_rakia = float(input())
    degrees_rakia = float(input())

    total_liters += q_rakia
    degrees_rakia *= q_rakia
    total_degrees += degrees_rakia

average_degrees = total_degrees / total_liters

#print
print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print(f"Not good, you should baking!")
elif average_degrees <= 42:
    print("Super!")
else:
    print(f"Dilution with distilled water!")
