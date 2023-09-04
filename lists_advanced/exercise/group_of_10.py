numbers = [int(n) for n in input().split(', ')]
group_nums = 10
counter = 0
while counter < len(numbers):
    collected = []
    for number in numbers:
        if group_nums - 10 < number <= group_nums:
            collected.append(number)
            counter += 1
    print(f" Group of {group_nums}'s: {collected}")
    group_nums += 10
