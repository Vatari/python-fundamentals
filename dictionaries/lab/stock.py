items = input().split()
products = input().split()
stock = {}

for i in range(0, len(items), 2):
    item = items[i]
    stock[item] = int(items[i + 1])

for product in products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
