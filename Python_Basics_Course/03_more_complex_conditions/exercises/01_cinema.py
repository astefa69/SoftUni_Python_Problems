tickets_type = str(input())
q_rows = int(input())
q_columns = int(input())

price = 0 #initiate/define variable

if tickets_type == "Premiere":
    price = 12.00

elif tickets_type == "Normal":
    price = 7.50

elif tickets_type == "Discount":    # else
    price = 5.00

revenue = q_rows * q_columns * price
print(f"{revenue:.2f} leva")


# Alternative solution
#03.PB-Python-Conditional-Statements-Advanced-Exercise.docx

tickets_type = input()
q_rows = int(input())
q_columns = int(input())

price = 0

cinema_capacity = q_rows * q_columns

if tickets_type == "Premiere":
    revenue = cinema_capacity * 12.00
elif tickets_type == "Normal":
    revenue = cinema_capacity * 7.50
elif tickets_type == "Discount":
    revenue = cinema_capacity * 5.00

print(f"{revenue:.2f} leva")