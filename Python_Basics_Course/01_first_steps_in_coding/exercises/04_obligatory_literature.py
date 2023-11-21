from math import floor
pages_current_book = int(input())
read_pages_per_hour = int(input())
count_days_to_read_whole_book = int(input())

count_hours_total = pages_current_book / read_pages_per_hour
needed_hours_per_day = count_hours_total / count_days_to_read_whole_book

print(floor(needed_hours_per_day))
# print(int(needed_hours_per_day)) # if asked to provide the whole number, no formatting, e.g. 7.2 -> 7, 7.9 -> 7
# print(round(needed_hours_per_day)) # rounds as usual to the closest whole number, e.g. if 6.8 -> 7, therefore use integer
# // is dividing to get a whole number or integer, but results in decimal number, e.g. 7.0, not 7
#needed_hours_per_day = count_hours_total // count_days_to_read_whole_book
#print(f'{hour:.0f}'