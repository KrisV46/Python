class Zoo:
    __animals = 0  # private atribute
    def __init__(self,name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
    
    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1
    
    def get_info(self,species):
        result = " "
        if species == 'mammal':
            result +=  f"{species} in {self.name}: {', '.join (self.mammals)}\n"
        elif species == 'fish':
            result += f"{species} in {self.name}: {', '.join (self.fishes)}\n"
        elif species == 'bird':
            result += f"{species} in {self.name}: {', '.join (self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result 

zoo_name = input("Enter zoo name: ")
#number_animals = int(input("Enter the number of animals: "))
zoo = Zoo(zoo_name)  # suzdavame obekta zoo koito izpolzva obekta zoo
number_animals = int(input("Enter the number of animals: "))
for i in range(number_animals):
    animal = input("Enter an animal: ").split(" ") # izpolzvame tova v skobite na split e tam kydeto shhte splitvame i go predstavq kato list
    species = animal[0]
    name = animal[1]
    zoo.add_animals(species, name)

info = input("Which species do you want to see info about: ")
print(zoo.get_info(info))
