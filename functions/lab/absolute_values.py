numbers = input().split(' ')


def absolute_values(strings):
    strings = map(float, strings)
    print([abs(num) for num in strings])


absolute_values(numbers)
