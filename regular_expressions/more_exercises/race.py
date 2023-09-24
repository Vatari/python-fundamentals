import re
from collections import Counter

participants = input().split(', ')
entry = input()
pattern_name = r"[A-Za-z]"
pattern_digits = r"\d+"
names = {}

while entry != "end of race":
    name = re.findall(pattern_name, entry)
    score = re.findall(pattern_digits, entry)

    new_name = ''.join(name)
    new_score = "".join(score)
    new_score = [int(s) for s in new_score]
    if new_name in participants:
        if new_name not in names:
            names[new_name] = 0
        names[new_name] += sum(new_score)
    entry = input()
count = Counter(names)
sorted_racers = count.most_common(3)

print(f"1st place: {sorted_racers[0][0]}")
print(f"2nd place: {sorted_racers[1][0]}")
print(f"3rd place: {sorted_racers[2][0]}")
