parking = {}
n = int(input())

for i in range(n):
    entry = input().split()
    command = entry[0]
    if command == "register":
        user = entry[1]
        license = entry[2]
        if user not in parking:
            parking[user] = license
            print(f"{user} registered {license} successfully")
        else:
            print(f"ERROR: already registered with plate number {license}")
    elif command == "unregister":
        user = entry[1]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            del parking[user]

for users, license in parking.items():
    print(f"{users} => {license}")
