#print("Enter a number from 1 to 9!")
number_one_to_nine = int(input())

if number_one_to_nine == 1:
    print("one")
elif number_one_to_nine == 2: #"if the previous conditions were not true, then try this condition"
    print("two")
elif number_one_to_nine == 3:
    print("three")
elif number_one_to_nine == 4:
    print("four")
elif number_one_to_nine == 5:
    print("five")
elif number_one_to_nine == 6:
    print("six")
elif number_one_to_nine == 7:
    print("seven")
elif number_one_to_nine == 8:
    print("eight")
elif number_one_to_nine == 9:
    print("nine")
else:   #The else keyword catches anything which isn't caught by the preceding conditions.
    print("number too big")

#https://github.com/SoftUni/Programming-Basics-Book-Python-EN/blob/master/chapter-03-simple-conditions.md