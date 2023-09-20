entry = input()
strength = 0
final_str = ''

for i in range(len(entry)):
    if strength > 0 and entry[i] != ">":
        strength -= 1
    elif entry[i] == ">":
        final_str += entry[i]
        strength += int(entry[i + 1])
    else:
        final_str += entry[i]

print(final_str)
