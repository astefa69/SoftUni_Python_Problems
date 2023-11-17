# Judge score: 75/100

starting_meters = 5_364
target_meters = 8_848
days = 1

while True:

    command = input()  #"END" or "action"

    action = command #•	"Yes" / "No" - текст - дали Атанас ще нощува преди изкачването на следващите метри или не
    if action == "Yes":
        days += 1

    if command == "END":
        break
    if days > 5: # !!! >=
        break
    if starting_meters >= target_meters:
        break


    climbed_meters = int(input()) #•	Изкачени метри - цяло число в интервала [1...4000]
    starting_meters += climbed_meters

if starting_meters >= target_meters:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(starting_meters)
