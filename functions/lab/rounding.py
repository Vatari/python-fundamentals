numbers = input().split(' ')


def rounding(strings):
    strings = map(float, strings)
    print([round(num) for num in strings])


rounding(numbers)
