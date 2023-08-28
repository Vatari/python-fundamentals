sum_list = input().split(', ')
num_of_beggars = int(input())
final_list = []
counter = 0
temp_sum = 0
sum_list_as_digits = []

# sum_list_as_digits = [int(i) for i in sum_list] # --> List comprehension

for i in range(len(sum_list)):
    sum_list_as_digits.append(int(sum_list[i]))
while counter < num_of_beggars:
    for el in range(counter, len(sum_list_as_digits), num_of_beggars):
        temp_sum += sum_list_as_digits[el]
    final_list.append(temp_sum)
    temp_sum = 0
    counter += 1

print(final_list)

