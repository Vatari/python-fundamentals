def reception(em1, em2, em3, count):
    total_employees = [em1, em2, em3]
    total_answered_per_hour = sum(total_employees)
    hour = 0
    while count > 0:
        hour += 1
        if hour % 4 != 0:
            count -= total_answered_per_hour
    print(f"Time needed: {hour}h.")


empl1 = int(input())
empl2 = int(input())
empl3 = int(input())
students = int(input())
reception(empl1, empl2, empl3, students)
