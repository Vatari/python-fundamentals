import re

entry = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
res = re.findall(pattern, entry)

for name in res:
    print(name, end=" ")
