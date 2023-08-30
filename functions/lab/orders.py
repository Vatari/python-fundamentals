
def orders(product, qty: int):
    if product == "coffee":
        res = qty * 1.5
        return f"{res:.2f}"
    elif product == "water":
        res = qty * 1
        return f"{res:.2f}"
    elif product == "coke":
        res = qty * 1.4
        return f"{res:.2f}"
    elif product == "snacks":
        res = qty * 2
        return f"{res:.2f}"


product = input()
qty = int(input())

print(orders(product, qty))
