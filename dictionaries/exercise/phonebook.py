phonebook = {}

while True:
    entry = input()
    if '-' not in entry:
        break
    name, phone = entry.split('-')
    phonebook[name] = phone


n = int(entry)
for i in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
