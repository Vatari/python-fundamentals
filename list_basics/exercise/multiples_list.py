factor = int(input())
count = int(input())
multiplier = 1
lst = []

for i in range(count):
    lst.append(factor * multiplier)
    multiplier += 1
print(lst)
