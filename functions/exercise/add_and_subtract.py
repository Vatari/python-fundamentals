
def sum_numbers(num1: int, num2: int, num3: int):
    lst = [num1, num2, num3]
    return sum(lst[:2])


def add_and_subtract(num1: int, num2: int, num3: int):
    res = sum_numbers(num1, num2, num3)
    return res - num3


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add_and_subtract(n1, n2, n3))
