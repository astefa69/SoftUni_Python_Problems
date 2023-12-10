# Solution with logical check "or"
# Alternatively it can be solved with a list:
# elif amimal in ["crocodile", "tortoise", "snake"]:

animal = str(input())

if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")
