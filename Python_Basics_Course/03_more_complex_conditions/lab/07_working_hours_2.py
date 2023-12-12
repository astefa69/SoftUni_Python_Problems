#Write a program that reads the time of day (integer) and day of the week (string) - 
#entered by the user and checks whether the office of a company is open, 
#with office hours from 10-18, Monday to Saturday inclusive.
#Input: 
#11
#Monday
#Output: open


#Solution 1
hour = int(input())
day = str(input())

if day == "Sunday":
     print("closed")
elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
     
        
#Solution 2
#hour = int(input())
#day = str(input())
#
#
#if 10 <= hour <= 18:
#    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
#        print("open")
#    elif day == "Sunday":
#        print("closed")
#elif hour > 18:
#    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday" or "Sunday":
#        print("closed")
#elif 0 <= hour < 10:
#    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday" or "Sunday":
#        print("closed")
