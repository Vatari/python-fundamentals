def shoot(targets, curr_index, curr_value):
    targets[curr_index] -= curr_value
    if targets[curr_index] <= 0:
        targets.pop(curr_index)
    return targets


def add(targets, curr_index, curr_value):
    targets.insert(curr_index, curr_value)
    return targets


def strike(targets, curr_index, curr_value):
    targets = targets[0:curr_index - curr_value] + targets[curr_index + curr_value + 1::]
    return targets


targets = [int(n) for number in input().split()]
command = input().split()
while command[0] != 'End':
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets = shoot(targets, index, value)
    if action == "Add":
        if 0 <= index < len(targets):
            targets = add(targets, index, value)
        else:
            print("Invalid placement!")
    if action == "Strike":
        if 0 <= index - value < len(targets) and 0 <= index + value < len(targets):
            targets = strike(targets, index, value)
        else:
            print("Strike missed!")

    command = input().split()
print('|'.join(str(target) for target in targets))
