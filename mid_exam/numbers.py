def top_five(numbers):
    numbers = [int(n) for n in numbers]
    avg = int(sum(numbers) // len(numbers))
    top_five_nums = [n for n in numbers if n > avg]
    reversed_list = sorted(top_five_nums, reverse=True)
    if len(reversed_list) >= 1:
        print(*reversed_list[:5])
    else:
        print("No")


digits = input().split()
top_five(digits)
