length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_aquarium_cm_cubbed = length * width * height #in cm.cubbed
#convert in decimeters= convert in liters
# 1 liter = 1 decimeter cubed
# 1000 = 10 cm * 10 cm * 10 cm
# to convert each side of the tank (length * width * height), I have to divide by 10, as 10 cm = 1 dm
# same is
#volume_aquarium_liters = volume_aquarium_cm_cubbed / 1000
volume_aquarium_liters = volume_aquarium_cm_cubbed * 0.001
volume_occupied_decimal = percent / 100 # convert to decimal number
required_liters = volume_aquarium_liters * (1 - volume_occupied_decimal)
print(required_liters)
