import math
contender1 = int(input())
contender2 = int(input())
contender3 = int(input())

sum_time = contender1 + contender2 + contender3

min = sum_time // 60
sec = sum_time % 60

#min = math.floor(min)

if sec < 10:
    print(f"{min}:0{sec}")
else:   # min >=10 or minutes have two digits
    print(f"{min}:{sec}")


#Alternative solution, without if...else
# print(f"{min}:{sec:02d}") !!!

#import math
# contender1 = int(input())
# contender2 = int(input())
# contender3 = int(input())
#
# sum_time = contender1 + contender2 + contender3
#
# min = sum_time // 60
# sec = sum_time % 60
# print(f"{min}:{sec:02d}")  #different form of formatting !!!
                                # :02d formats digits less than 10
                                # by adding 0 (e.g. 01,02,03,...,09)


# if sum_time < 10:
#     min = 0
#     sec = sum_time
#     print(f"{min}:0{sec}")
#
# if sum_time < 60:
#     min = 0
#     sec = sum_time
#     print(f"{min}:{sec}")
#
# if sum_time >= 60:
#     min = sum_time // 60
#     sec = sum_time % 60
#     if sec < 10:
#         print(f"{min}:0{sec}")
#         else:
#         print(f"{min}:{sec}")