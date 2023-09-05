curr_version = int("".join([v for v in input().split(".")]))

next_version = ".".join(str(curr_version + 1))

print(next_version)
