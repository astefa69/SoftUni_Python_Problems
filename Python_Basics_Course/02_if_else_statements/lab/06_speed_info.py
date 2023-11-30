#series of validations !!!
#only one should be correct

# real number or decimal -> float()
# integer or whole number -> int()
#text -> str()
speed = float(input())

if speed > 1000:
    print("extremely fast")
elif speed > 150:
    print("ultra fast")
elif speed > 50:
    print("fast")
elif speed > 10:
    print("average")
else:
    print("slow")

#Command + /
#Alternative solution with intervals as described
# speed = float(input())
#
# if speed <= 10:
#     print("slow")
# elif 10 < speed <= 50:
#     print("average")
# elif 50 < speed <= 150:
#     print("fast")
# elif 150 < speed <= 1000:
#     print("ultra fast")
# elif speed > 1000:
#     print("extremely fast")


#Alternative solution with if..elif...else
# speed = float(input())
#
# if speed <= 10:
#     print("slow")
# elif 10 < speed <= 50:
#     print("average")
# elif 50 < speed <= 150:
#     print("fast")
# elif 150 < speed <= 1000:
#     print("ultra fast")
# else:
#     print("extremely fast")