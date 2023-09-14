result = {}

while True:
    item = input()
    if item == "stop":
        break
    qty = int(input())
    if item not in result:
        result[item] = 0
    result[item] += qty

for item, qty in result.items():
    print(f"{item} -> {qty}")
