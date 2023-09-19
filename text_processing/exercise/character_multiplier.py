first_str, second_str = input().split()
total_sum = 0
if len(first_str) > len(second_str):
    for i in range(len(second_str)):
        total_sum += ord(first_str[i]) * ord(second_str[i])
    for i in range(len(second_str), len(first_str)):
        total_sum += ord(first_str[i])
elif len(second_str) > len(first_str):
    for i in range(len(first_str)):
        total_sum += ord(first_str[i]) * ord(second_str[i])
    for i in range(len(first_str), len(second_str)):
        total_sum += ord(second_str[i])
else:
    for i in range(len(first_str)):
        total_sum += ord(first_str[i]) * ord(second_str[i])

print(total_sum)
