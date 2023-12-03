# Processor - 35% of the price of the purchased video cards/PC !
# 35% * (Video card 250 BGN / PC * Number of video cards), not 35% * Video card 250 BGN / PC


budget = float(input())
q_graphic_card = int(input())
q_processor = int(input())
q_RAM = int(input())

p_graphic_card = 250
total_graphic_card = p_graphic_card * q_graphic_card

p_processor = 0.35 * total_graphic_card
total_processor = p_processor * q_processor

p_RAM = 0.10 * total_graphic_card
total_RAM = p_RAM * q_RAM

total_amount = total_graphic_card + total_processor + total_RAM

if q_graphic_card > q_processor:
    discount = 0.15
else:   #q_graphic_card <= q_processor
    discount = 0

total_amount = (1 - discount) * total_amount
difference = abs(total_amount - budget)

if total_amount <= budget:
    print(f"You have {difference:.2f} leva left!")
else:   # total_amount > budget
    print(f"Not enough money! You need {difference:.2f} leva more!")
