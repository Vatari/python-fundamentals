current_str = input()

while current_str != "End":
    if current_str != "SoftUni":
        new_str = ''
        for char in current_str:
            new_str += char * 2
        print(new_str)
    current_str = input()
