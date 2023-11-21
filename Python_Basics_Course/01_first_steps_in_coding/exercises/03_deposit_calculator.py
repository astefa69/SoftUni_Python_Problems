amount_deposited_today = float(input())
term_deposit = int(input())
annual_interest_rate = float(input()) / 100
total_deposit_amount = amount_deposited_today + term_deposit * ((amount_deposited_today * annual_interest_rate) / 12)

print(total_deposit_amount)