def add_hearts(houses, index):
    houses[index] -= 2
    if houses[index] <= -2:
        print(f"Place {index} already had Valentine's day.")
    elif houses[index] <= 0:
        print(f"Place {index} has Valentine's day.")
    return houses


houses = [int(x) for x in input().split('@')]
position = 0
command = input().split()
while command[0] != "Love!":
    value = int(command[1])
    position += value
    if position >= len(houses):
        position = 0
    houses = add_hearts(houses, position)
    command = input().split()
print(f"Cupid's last position was {position}.")
failed = [int(house) for house in houses if int(house) > 0]
if failed:
    print(f"Cupid has failed {len(failed)} places.")
else:
    print("Mission was successful.")
