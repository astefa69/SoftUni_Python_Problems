#Write a program that reads the type and size of a geometric figure and calculates its area.
#Round the result to 3 decimals.

figure_type = str(input()) #square, rectangle, circle, triangle

if figure_type == "square":
    side_a = float(input())
    area = side_a * side_a
    print(f"{area:.3f}")
if figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b # A = w * l, length * width
    print(f"{area:.3f}")
if figure_type == "circle":
    radius_fig = float(input())
    import math
    area = math.pi * radius_fig ** 2    # A = pi * r^2
    print(f"{area:.3f}")
if figure_type == "triangle":
    side_a = float(input()) #length of the base
    altitude = float(input())  #  height or altitude of the triangle
    area = (side_a * altitude) / 2  # (base * altitude) / 2
    print(f"{area:.3f}")



# elif figure_type == "rectangle":
#     side_a = float(input)
#     side_b = float(input)
#     print(side_a)
#     print(side_b)
# elif figure_type == "circle":
#     radius = float(input)
#     print(radius)
# elif figure_type == "triangle":
#     side_a = float(input)
#     side_b = float(input)
#     print(side_a)
#     print(side_b)

