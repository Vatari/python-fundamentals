searched_course = None
courses = {}
while True:
    command = input()

    if ":" not in command:
        searched_course = command
        break

    command_args = command.split(":")
    name = command_args[0]
    id_ = command_args[1]
    course = command_args[2]

    if course not in courses:
        courses[course] = {}
    courses[course][id_] = name

searched_course = searched_course.replace("_", " ")
current_course = courses[searched_course]

for k, v in current_course.items():
    print(f"{v} - {k}")
