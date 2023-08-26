number = int(input())

positive_list = []
negatives_list = []
sum_negatives = 0
# sum = sum(negative_list)

for i in range(number):
    line = int(input())
    if line < 0:
        negatives_list.append(line)
    else:
        positive_list.append(line)
for number in negatives_list:
    sum_negatives += number

print(positive_list)
print(negatives_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum_negatives}")
