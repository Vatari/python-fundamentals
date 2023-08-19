
budget = float(input())
price_for_kg_flour = float(input())
price_for_pack_eggs = price_for_kg_flour * 0.75
price_for_quart_milk = (price_for_kg_flour * 1.25) / 4

money_needed_for_one_loaf = price_for_kg_flour + price_for_pack_eggs + price_for_quart_milk

loaves = 0
colored_eggs = 0

while budget >= money_needed_for_one_loaf:
    loaves += 1
    budget -= money_needed_for_one_loaf
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs "
      f"and {budget:.2f}BGN left.")
