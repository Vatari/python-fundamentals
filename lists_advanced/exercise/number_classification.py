def find_positive(numbers):
    nums = [str(n) for n in numbers if n >= 0]
    return nums


def find_negative(numbers):
    nums = [str(n) for n in numbers if n < 0]
    return nums


def find_even(numbers):
    nums = [str(n) for n in numbers if n % 2 == 0]
    return nums


def find_odd(numbers):
    nums = [str(n) for n in numbers if n % 2 != 0]
    return nums


numbers = [int(s) for s in input().split(', ')]

print(f"Positive: {', '.join(find_positive(numbers))}")
print(f"Negative: {', '.join(find_negative(numbers))}")
print(f"Even: {', '.join(find_even(numbers))}")
print(f"Odd: {', '.join(find_odd(numbers))}")
