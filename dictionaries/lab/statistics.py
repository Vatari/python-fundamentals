products = {}

items = input().split(": ")
while True:
    product = items[0]
    if product == "statistics":
        break
    qty = int(items[1])
    if product not in products:
        products[product] = qty
    else:
        products[product] += qty

    items = input().split(": ")

print("Products in stock:")
for item, value in products.items():
    print(f"- {item}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
