n = int(input()) #•	n - integer in interval [100…1000]

for a in range(1, 9 + 1): #•	a changes from 1 to 9
    for b in range(9, a - 1, -1): #•	b changes from 9 to а
        for c in range(0, 9 + 1): #•	c changes from 0 to 9
            for d in range(9, c - 1, -1): #•	d changes from 9 to c
                #If sum (a + b + c + d) is equal to product (a * b * c * d)
                # and simulataneously n ends in 5, number abcd shall be printed.
                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    #•	If valid combination is found:
                    print(f"{a}{b}{c}{d}")
                    exit()
                #If product (a * b * c * d) is divided to the sum (a + b + c + d) and is obtained 3 (whole number),
                # and at the same time n is divided by 3 without remainder, the number dcba should be printed
                elif (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    #•	If valid combination is found:
                    print(f"{d}{c}{b}{a}")
                    exit() #The program should print to the console only the first valid combination.
#•	If NO such combination is found:
print("Nothing found")
