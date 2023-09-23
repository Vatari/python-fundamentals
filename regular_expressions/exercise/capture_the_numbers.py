import re

entry = input()
pattern = r"\d+"
res = []

while entry:
    digits = re.findall(pattern, entry)
    res.extend(digits)
    entry = input()

print(' '.join(res))
