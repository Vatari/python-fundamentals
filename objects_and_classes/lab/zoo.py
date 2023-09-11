class Zoo:
    def __init__(self, name):
        self.__animals = 0
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals +=1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        animals = []
        if species == "mammal":
            species = "Mammals"
            animals = self.mammals
        elif species == "fish":
            species = "Fishes"
            animals = self.fishes
        elif species == "bird":
            animals = self.birds
            species = "Birds"

        return f"{species} in {self.name}: {', '.join(animals)}\nTotal animals: {self.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
for __ in range(n):
    text = input().split()
    specie = text[0]
    animal = text[1]
    zoo.add_animal(specie, animal)


types = input()
print(zoo.get_info(types))
