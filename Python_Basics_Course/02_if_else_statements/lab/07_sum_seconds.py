# https://python-book.softuni.org/chapter-03-simple-conditions.html
#Problem: Sum Seconds
#Three athletes finish with some number of seconds (between 1 and 50). 
#Write a program that reads the times of the contestants and calculates their combined time in "minutes:seconds" format. Seconds are to be printed with a leading zero (2 -> "02", 7 -> "07", 35 -> "35").
#Judge: 100/100



athlete1_time = int(input())
athlete2_time = int(input())
athlete3_time = int(input())
seconds = athlete1_time + athlete2_time + athlete3_time
minutes = 0

if seconds > 59:
    minutes += 1
    seconds = seconds - 60
if seconds > 59:
    minutes += 1
    seconds = seconds - 60
if seconds < 10:
    print(f'{minutes}:O{seconds}')
else:
    print(f'{minutes}:{seconds}')


#Judge: 90/100 !
# athlete1_time = int(input())
# athlete2_time = int(input())
# athlete3_time = int(input())
#
# sum_time_seconds = athlete1_time + athlete2_time + athlete3_time
# if sum_time_seconds > 9:
#     min = 0
#     sec = sum_time_seconds
# if sum_time_seconds > 59:
#     min = 1
#     sec = sum_time_seconds - 60
# if sum_time_seconds > 119:
#     min = 2
#     sec = sum_time_seconds - 120
# if sec < 10:
#     print(f'{min}:0{sec}')
# else:
#     print(f'{min}:{sec}')

#Judge: 90/100 !
# sum_time_seconds = athlete1_time + athlete2_time + athlete3_time
# sum_time_mins = sum_time_seconds / 60
# if sum_time_seconds >=120:
#     min = sum_time_seconds / 60
#     sec = sum_time_seconds % 60
#     print(f"{min:.0f}:{sec:02d}")
# elif sum_time_seconds >= 60:
#     min = sum_time_seconds / 60
#     sec = sum_time_seconds % 60
#     print(f"{min:.0f}:{sec:02d}")
# elif sum_time_seconds >= 0:
#     min = 0
#     sec = sum_time_seconds14 % 60
#     print(f"{min:.0f}:{sec:02d}")
