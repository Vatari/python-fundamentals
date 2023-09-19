entry = input().split()
total_sum = 0
for curr_str in entry:
    first_ch = curr_str[0]
    last_ch = curr_str[-1]
    curr_num = int(curr_str[1:len(curr_str) - 1])
    if first_ch.isupper():
        first_ch_position = ord(first_ch) - 64
        total_sum += curr_num / first_ch_position
    elif first_ch.islower():
        first_ch_position = ord(first_ch) - 96
        total_sum += curr_num * first_ch_position
    if last_ch.isupper():
        last_ch_position = ord(last_ch) - 64
        total_sum -= last_ch_position
    elif last_ch.islower():
        last_ch_position = ord(last_ch) - 96
        total_sum += last_ch_position

print(f"{total_sum:.2f}")
