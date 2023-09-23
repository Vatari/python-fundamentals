import re

entry = input()
furnitures = []
total_money = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
while entry != "Purchase":
    match = re.search(pattern, entry)
    if match:
        furniture, price, quantity = match.groups()
        furnitures.append(furniture)
        total_money += float(price) * int(quantity)
    entry = input()

print("Bought furniture:")
for furniture in furnitures:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
