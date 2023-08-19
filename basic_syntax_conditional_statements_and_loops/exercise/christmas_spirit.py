qty_decorations = int(input())
remaining_days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

spirit = 0
total_cost = 0

for curr_day in range(1, remaining_days + 1):
    if curr_day % 11 == 0:
        qty_decorations += 2
    if curr_day % 2 == 0:
        total_cost += ornament_set * qty_decorations
        spirit += 5
    if curr_day % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * qty_decorations
        spirit += 13
    if curr_day % 5 == 0:
        total_cost += tree_lights * qty_decorations
        spirit += 17
        if curr_day % 3 == 0:
            spirit += 30
    if curr_day % 10 == 0:
        spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights
if remaining_days % 10 == 0:
    spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")


