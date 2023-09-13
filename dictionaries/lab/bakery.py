items = input().split(" ")
bakery = {}

for i in range(0, len(items), 2):
    item = items[i]
    bakery[item] = int(items[i + 1])

print(bakery)
