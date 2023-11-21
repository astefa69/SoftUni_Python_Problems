subscription_fee_annual = int(input())
sneakers_price = (1 - 0.4) * subscription_fee_annual
sport_suit_price = (1 - 0.2) * sneakers_price
basketball_price = (1/4) * sport_suit_price
accessories_price = (1/5) * basketball_price

annual_fee_total = (subscription_fee_annual \
                    + sneakers_price \
                    + sport_suit_price \
                    + basketball_price \
                    + accessories_price)

print(annual_fee_total)