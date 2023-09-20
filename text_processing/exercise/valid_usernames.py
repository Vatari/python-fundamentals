import re


def is_allowed(username):
    if len(username) < 3 or len(username) > 16:
        return False
    pattern = re.compile(r'[^a-zA-Z0-9-\-_.]')
    string = pattern.search(username)
    return not bool(string)


usernames = input().split(', ')
valid_usernames = []

for name in usernames:
    if is_allowed(name):
        valid_usernames.append(name)

print('\n'.join(valid_usernames))
