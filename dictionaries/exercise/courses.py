courses = {}
entry = input().split(' : ')

while entry[0] != "end":
    course, name = entry
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
    entry = input().split(' : ')

for course, students in courses.items():
    print(f"{course}: {len(courses[course])}")
    for student in students:
        print(f"-- {student}")
