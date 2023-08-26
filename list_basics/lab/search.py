number = int(input())
word = input()

lst = []
filtered = []

for i in range(number):
    text = input()
    lst.append(text)

for item in lst:
    if item.__contains__(word):
        filtered.append(item)


print(lst)
print(filtered)
