import re

entry = input()
pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
res = re.findall(pattern, entry)
print(", ".join(res))
