num_of_lines = int(input())
capacity = 255
water_counter = 0

for line in range(num_of_lines):
    curr_flow = int(input())
    if capacity - curr_flow < 0:
        print("Insufficient capacity!")
    else:
        water_counter += curr_flow
        capacity -= curr_flow
print(water_counter)
