def to_do_list():
    notes = [''] * 11
    while True:
        text = input().split('-')
        if text[0] == "End":
            break
        priority = int(text[0])

        note = text[1]
        notes[priority] = note

    notes = [x for x in notes if x != '']
    return notes


print(to_do_list())
