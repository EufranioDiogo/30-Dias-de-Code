meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

tip = meal_cost * ( tip_percent / 100 )
tax = meal_cost * ( tax_percent / 100 )

total_cost = meal_cost + tip + tax
total_cost = round(total_cost)

print(total_cost)