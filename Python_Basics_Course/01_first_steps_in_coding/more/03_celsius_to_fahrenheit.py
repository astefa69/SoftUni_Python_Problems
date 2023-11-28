#Write a program that reads degrees Celsius (°C) and
# convert them to degrees Fahrenheit (°F).
# Search the Internet for a suitable formula to perform the calculations.
# Format the output to the second decimal place.

#celsius -> fahrenheit
#To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
#Source: https://www.almanac.com/temperature-conversion-celsius-fahrenheit

celsius = float(input())

fahrenheit = celsius * 1.8 + 32

print(f"{fahrenheit:.2f}")