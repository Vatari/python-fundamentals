orders = int(input())
total_price = 0
for order in range(orders):
    price_capsule = float(input())
    days = int(input())
    amount_capsules_per_day = int(input())

    if price_capsule < 0.01 or price_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if amount_capsules_per_day < 1 or amount_capsules_per_day > 2000:
        continue
    price = price_capsule * days * amount_capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
