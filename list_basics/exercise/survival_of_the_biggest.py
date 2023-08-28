numbers = input().split(" ")
n = int(input())
lst = []
final = []

for num in numbers:
    lst.append(int(num))

for i in range(n):
    temp = min(lst)
    lst.remove(temp)

print(", ".join(map(str, lst)))
