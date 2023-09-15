command = input().split()
products = {}
while command != "Buy":
    if len(command) > 1:
        product, price, qty = command
        if product not in products:
            products[product] = {"price": 0.0, "qty": 0}

        products[product]["price"] = float(price)
        products[product]["qty"] += int(qty)
        products[product]["total"] = products[product]["price"] * products[product]["qty"]
    else:
        break
    command = input().split()

for product in products.items():
    total = product[1]["total"]
    print(f"{product[0]} -> {total:.2f}")
