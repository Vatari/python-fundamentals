import re

pattern = r"(w{3}\.[a-zA-Z0-9-\.]+\.[a-z]+)"
entry = input()
valid_urls = []
while entry:
    matches = re.search(pattern, entry)
    if matches:
        valid_urls.append(matches.group(0))
    entry = input()

for url in valid_urls:
    print(url)
