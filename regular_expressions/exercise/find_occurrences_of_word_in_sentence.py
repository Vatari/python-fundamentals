import re

entry = input()
word = input()
pattern = fr"\b{word}\b"

res = re.findall(pattern, entry, re.IGNORECASE)

print(len(res))
