def shopping_list(items):
    command = input().split()
    while True:
        list_type = command[0]
        item = command[1]
        if list_type == "Urgent":
            for i in items:
                if item not in items:
                    items.insert(0, item)
        elif list_type == "Unnecessary":
            for i in items:
                if item in items:
                    items.remove(item)
        elif list_type == "Correct":
            new_item = command[2]
            for i in range(len(items)):
                if items[i] == item:
                    items[i] = new_item
        elif list_type == "Rearrange":
            for i in items:
                if item in items:
                    items.remove(item)
                    items.append(item)
        elif list_type == "Go":
            return ", ".join(items)
        command = input().split()


text = input().split('!')
print(shopping_list(text))
