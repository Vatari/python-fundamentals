import re

entry = input()
pattern = r"\b_([A-Za-z0-9]+\b)"
res = re.findall(pattern, entry)

print(','.join(res))
