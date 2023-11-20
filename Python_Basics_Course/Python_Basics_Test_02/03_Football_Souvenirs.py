#100/100
team = input() #team - text with options: "Argentina", "Brazil", "Croatia", "Denmark"
souvenier = input() #type of souvenirs - text with options: "flags", "caps", "posters", "stickers"
q_souvenier = int(input()) #number of souvenirs purchased - integer

not_valid_team = False
not_valid_souvenier = False

if team == "Argentina":
    if souvenier == "flags":
        price = 3.25
    elif souvenier == "caps":
        price = 7.20
    elif souvenier == "posters":
        price = 5.10
    elif souvenier == "stickers":
        price = 1.25
    else:
        price = 0
        not_valid_souvenier = True
        #print("Invalid stock!")
elif team == "Brazil":
    if souvenier == "flags":
        price = 4.20
    elif souvenier == "caps":
        price = 8.50
    elif souvenier == "posters":
        price = 5.35
    elif souvenier == "stickers":
        price = 1.20
    else:
        price = 0
        not_valid_souvenier = True
        # print("Invalid stock!")
elif team == "Croatia":
    if souvenier == "flags":
        price = 2.75
    elif souvenier == "caps":
        price = 6.90
    elif souvenier == "posters":
        price = 4.95
    elif souvenier == "stickers":
        price = 1.10
    else:
        price = 0
        not_valid_souvenier = True
        # print("Invalid stock!")
elif team == "Denmark":
    if souvenier == "flags":
        price = 3.10
    elif souvenier == "caps":
        price = 6.50
    elif souvenier == "posters":
        price = 4.80
    elif souvenier == "stickers":
        price = 0.90
    else:
        price = 0
        not_valid_souvenier = True
        # print("Invalid stock!")
else:
    price = 0
    not_valid_team = True
    #print("Invalid country!")

total = q_souvenier * price

#print
#If the country and item are set correctly:
if total > 0:
    print(f"Pepi bought {q_souvenier} {souvenier} of {team} for {total:.2f} lv.") #брой сувенири; вид сувенири; отбор; крайна сума
#If the country is not set correctly:
elif not_valid_team:
    print("Invalid country!")
#If the item is not set correctly:
elif not_valid_souvenier:
    print("Invalid stock!")
#The result is formatted to the second decimal.
