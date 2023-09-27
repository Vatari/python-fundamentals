plants = {}
n = int(input())


def rate_plant(plant_to_be_rated, rate, dict_):
    if not plant_to_be_rated in dict_:
        print("error")
    else:
        dict_[plant_to_be_rated]["rating"].append(int(rating))
    return dict_


def update_rarity(plant_to_be_updated, rarity_, dict_):
    if not plant_to_be_updated in dict_:
        print("error")
    else:
        dict_[plant_to_be_updated]["rarity"] = rarity
    return dict_


def reset_rating(plant_to_be_reset, dict_):
    if not plant_to_be_reset in dict_:
        print("error")
    else:
        dict_[plant_to_be_reset]["rating"].clear()
    return dict_


for i in range(n):
    plant, rarity = input().split("<->")
    if plant in plants:
        plants[plant]["rarity"] = int(rarity)

    plants[plant] = {"rarity": int(rarity), "rating": []}

while True:
    command = input().split(": ")

    if command[0] == "Exhibition":
        break
    elif command[0] == "Rate":
        plant, rating = command[1].split(' - ')
        rate_plant(plant, rating, plants)
    elif command[0] == "Update":
        plant, rarity = command[1].split(' - ')
        update_rarity(plant, rarity, plants)
    elif command[0] == "Reset":
        plant = command[1]
        reset_rating(plant, plants)

print("Plants for the exhibition:")
for plant, values in plants.items():
    if (len(values['rating'])) <= 0:
        rating = 0
    else:
        rating = sum(values['rating']) / len(values['rating'])

    print(f"- {plant}; Rarity: {values['rarity']}; Rating: {float(rating):.2f}")
