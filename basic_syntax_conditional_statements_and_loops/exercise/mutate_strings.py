str1 = input()
str2 = input()
last_str = str1

for char_index in range(len(str1)):
    left_part = str2[:char_index + 1]
    right_part = str1[char_index + 1:]
    new_str = left_part + right_part
    if new_str == last_str:
        continue
    print(new_str)
    last_str = new_str
