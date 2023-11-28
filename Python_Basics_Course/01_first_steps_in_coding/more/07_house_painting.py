# Write a program that calculates how many liters of paint are needed to paint a house.
#Where green paint is used for the walls and red paint for the roof. 
# The consumption of green paint is 1 litre for 3.4 m2 and of red paint 1 litre for 4.3 m2.

x = float(input()) #height of the house
y = float(input()) #length of the side wall
h = float(input()) #height of the triangular wall of the roof

green_paint = 3.4 # 1 liter for 3.4 sq.m.
red_paint = 4.3 # 1 liter for 4.3 sq.m.

#first floor
floor_squares =  2 * (x * x) - (2 * 1.2) # area of two squares without the door
floor_rectangles = 2 * (y * x) - 2 * (1.5 * 1.5) # area of two rectangles excluding the area of two windows

floor_area = floor_squares + floor_rectangles
green_paint_l = floor_area / green_paint

#roof
roof_triangles  = 2 * ((h * x) / 2)
roof_rectangles = 2 * (y * x)

roof_area = roof_triangles + roof_rectangles

red_paint_l = roof_area / red_paint

#Formatted to the second decimal
print(f"{green_paint_l:.2f}")
print(f"{red_paint_l:.2f}")
