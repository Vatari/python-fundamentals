entry = input()

for i in range(len(entry)):
    if entry[i] == ":":
        print(f"{entry[i]}{entry[i + 1]}")
