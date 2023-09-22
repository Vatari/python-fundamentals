import re

entry = input()
pattern = r"(?P<day>\d{2})(?P<sep>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
res = re.findall(pattern, entry)

for item in res:
    print(f"Day: {item[0]}, Month: {item[2]}, Year: {item[3]}")
