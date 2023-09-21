import re


def extract_info(text):
    name = re.search('(\@(\w+)\|)', text)
    age = re.search('(\#(\w+)\*)', text)
    return name.group(2), age.group(2)


n = int(input())
res = []

for text in range(n):
    text = input()
    res.append(extract_info(text))

for name, age in res:
    print(f"{name} is {age} years old.")
