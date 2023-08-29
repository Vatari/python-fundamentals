numbers = input().split(', ')
numbers = list(map(int, numbers))

for num in numbers:
    if num == 0:
        temp = num
        numbers.remove(num)
        numbers.append(temp)
print(numbers)