def get_sum(num):
    odd_sum = []
    even_sum = []
    for n in num:
        if int(n) % 2 != 0:
            odd_sum.append(int(n))
        else:
            even_sum.append(int(n))
    return f"Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}"


number = input()
print(get_sum(number))
