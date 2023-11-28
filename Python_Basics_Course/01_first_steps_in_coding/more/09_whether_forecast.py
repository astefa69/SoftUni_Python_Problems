#Write a program that knows if it's hot or cold outside.
# A line is read from the console - text that tells you what the weather is.
# When "sunny" is typed, "It's warm outside!" should be printed.
# In all other cases "It's cold outside!" should be printed.

whether = input()

if whether == "sunny":
    print("It's warm outside!")
else: #current_whether == "cloudy" or current_whether == "snowy":
    print("It's cold outside!")