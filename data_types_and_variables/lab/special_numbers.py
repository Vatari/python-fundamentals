def is_special(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum == 5 or digit_sum == 7 or digit_sum == 11


num = int(input())
for number in range(1, num + 1):
    print(f"{number} -> {is_special(number)}")
