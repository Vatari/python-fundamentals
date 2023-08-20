coffees = 0
events = ["coding", "cat", "dog", "movie", "CODING", "CAT", "DOG", "MOVIE"]
while True:
    command = input()
    if command in events:
        if command.islower():
            coffees += 1
        elif command.isupper():
            coffees += 2
    if command == "END":
        break

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
