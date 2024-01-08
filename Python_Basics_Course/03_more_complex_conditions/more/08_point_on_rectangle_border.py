#Input data is read from the console and consists of 6 lines entered by the user:
# the decimal numbers x1, y1, x2, y2, x and y (ensuring that x1 < x2 and y1 < y2).
# Print "Border" (the point lies on either side) or "Inside/Outside" (otherwise).

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

# if x1 < x < x2 and y1 < y < y2:
#     print("Inside / Outside")
# elif x > x1 and y1 < y < y2:
#     print("Inside / Outside")

#Hint: use one or more conditional if statements with logical operations.
# A point {x, y} lies on either side of a rectangle {x1, y1} - {x2, y2},
# if one of the following conditions is satisfied:
# x coincides with x1 or x2 and at the same time y is between y1 and y2
if x == x1 or x == x2:
    if y1 <= y <= y2 :
        print("Border")
# y coincides with y1 or y2 and at the same time x is between x1 and x2
elif y == y1 or y == y2:
    if x1 <= x <= x2 :
        print("Border")
else:
    print("Inside / Outside")


##Aleternative solution
## We read the coordinates of the rectangle and the point
#x1 = float(input())
#y1 = float(input())
#x2 = float(input())
#y2 = float(input())
#x = float(input())
#y = float(input())
#
## Check whether the point is on the sides of the rectangle or inside it
#is_on_horizontal_side = (x == x1 or x == x2) and y1 <= y <= y2
#is_on_vertical_side = (y == y1 or y == y2) and x1 <= x <= x2
#
#if is_on_horizontal_side or is_on_vertical_side:
#    print("Border")
#else:
#    print("Inside / Outside")
