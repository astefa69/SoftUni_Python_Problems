folio = int(input())
paint = int(input())
solvent = int(input())
hours = int(input())

folio_total = folio * 1.50 + 2*1.50 #2 sq.m. more folio
paint_total = paint * 14.50 * 1.1 #1.1 is 10% more paint
solvent_total = solvent * 5.00
bags = 0.40

materials_total = folio_total + paint_total + solvent_total + bags
hours_total = hours * 0.3 * materials_total

total_cost = materials_total + hours_total

print(total_cost)
#print(f"total cost is {total_cost}")