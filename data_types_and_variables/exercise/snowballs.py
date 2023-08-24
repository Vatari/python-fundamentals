from math import pow

snowballs = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for snowball in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    curr_snowball_value = pow(snowball_weight / snowball_time, snowball_quality)
    if curr_snowball_value > max_value:
        max_value = curr_snowball_value
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
