def trains(args):
    while True:
        text = input().split()
        command = text[0]

        if command == "add":
            people = int(text[1])
            args[-1] += people
        elif command == "insert":
            index = int(text[1])
            people = int(text[2])
            args[index] += people
        elif command == "leave":
            index = int(text[1])
            people = int(text[2])
            args[index] -= people
        elif command == "End":
            break
    return args


num_of_wagons = int(input())
train = [0 for x in range(num_of_wagons)]
print(trains(train))

