def calculate(food, hay, cover, pig_kg):
    day = 0
    while day <= 29:
        day += 1
        food -= 300
        if day % 2 == 0:
            hay -= food * 0.05
        if day % 3 == 0:
            cover -= pig_kg / 3

    if food <= 0 or hay <= 0 or cover <= 0:
        is_enough = False
    else:
        is_enough = True

    if is_enough:
        print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
    else:
        print("Merry must go to the pet store!")


qty_food = float(input()) * 1000
qty_hay = float(input()) * 1000
qty_cover = float(input()) * 1000
qty_kg = float(input()) * 1000
calculate(qty_food, qty_hay, qty_cover, qty_kg)
