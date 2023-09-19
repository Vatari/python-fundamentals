entry = input().split('\\')
last_str = entry[-1].split('.')
filename = last_str[0]
ext = last_str[1]
print(f"File name: {filename}\nFile extension: {ext}")
