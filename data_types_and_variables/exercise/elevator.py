from math import ceil

num_of_people = int(input())
elevator_capacity = int(input())
courses = 0
if elevator_capacity != 0:
    courses = ceil(num_of_people / elevator_capacity)
print(courses)
