while True:
    entry = input()
    if entry == "end":
        break
    print(f"{entry} = {entry[::-1]}")
