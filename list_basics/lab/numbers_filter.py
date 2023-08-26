number = int(input())

lst = []
filtered = []

for i in range(number):
    next_num = int(input())
    lst.append(next_num)
command = input()
if command == "even":
    for num in lst:
        if num % 2 == 0:
            filtered.append(num)
elif command == "odd":
    for num in lst:
        if num % 2 != 0:
            filtered.append(num)
elif command == "negative":
    for num in lst:
        if num < 0:
            filtered.append(num)
elif command == "positive":
    for num in lst:
        if num >= 0:
            filtered.append(num)
print(filtered)
