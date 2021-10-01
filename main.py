species_list = {'dog': 'dog', 'cat': 'cat', 'horse': 'horse', 'hamster': 'hamster'}
animal = {'Dog': [], 'Cat': []}

class Pet():
    def __init__(self, species, name=''):
        if species not in species_list:
            print("\nspecies not in the species_list")
            species_list[species] = name
        else:
            self.species = species
            self.name = name

    def __str__(self):
        if self.name == '':
            print("\nSpecies of " + self.species + " unnames")
        else:
            print("\nSpecies of " + self.species + " named " + self.name)

class Dog(Pet):
    def __init__(self, name='', chases='Cats'):
        self.species = 'Dog'
        self.name = name
        self.chases = chases

    def __str__(self):
        if self.name == '':
            print("\nSpecies of " + self.species + " unnames" + " chasess " + self.chases)
        else:
            print("\nSpecies of " + self.species + " named " + self.name + " chasess " + self.chases)

class Cat(Pet):
    def __init__(self, name='', hates='Dog'):
        self.species = 'Cat'
        self.name = name
        self.hates = hates

    def __str__(self):
        if self.name == '':
            print("\nSpecies of " + self.species + " unnames" + " hates " + self.hates)
        else:
            print("\nSpecies of " + self.species + " named " + self.name + " hates " + self.hates)

def pet_object():
    species = input("enter the species name : ")
    new_pet = Pet(species)
    print(species_list)

def dog_object():
    name = input("enter the dog name: ")
    chases = input("enter the chases: ")
    dog = Dog(name, chases)
    animal['Dog']= [name, chases]
    print(animal)
    dog.__str__()

def cat_object():
    name = input("enter the cat name: ")
    hates = input("enter the hates: ")
    cat = Cat(name, hates)
    animal['Cat'] = [name, hates]
    cat.__str__()

def main():
    while True:
        print(" 1 Add Pet\n 2 Add Species Dog\n 3 Add Species Cat\n")
        choice = int(input("enter the choice: "))
        if choice == 1:
            pet_object()
        elif choice == 2:
            dog_object()

        elif choice == 3:
            cat_object()
        else:
            print("\nsorry invalid choice: ")


main()











