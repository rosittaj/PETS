class Pet(object):
    def __init__(self,species,name):
        try:
            self.species=species
            self.name=name
        except:
            print("the species is not one of the following :'dog','cat','horse',hamster'")
    def __str__(self):
        species="species of" + self.species +"."
        name="named" + self.name +"."
        return species,name
class Dog(Pet):
    def __init__(self,chases):
        name=self.name
        self.chases=chases

    def __str__(self):
        species = "species of" + self.species + "."
        chases = "chases" + self.chases + "."
        return species,chases
class Cat(Pet):
    def __init__(self,hates="Dogs"):
        species=self.species
        self.hates=hates

    def __str__(self):
        name = "species of" + self.species + "."
        hates = "hates" + self.hates + "."
        return hates, name
class Horse(Pet):
    def hi(self):
        print("hi")
class Hamster(Pet):
    def hi(self):
        print('hai')
def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)

pet_types = {'dog': Dog,'cat':Cat,'horse':Horse,'hamster':Hamster}
def main():
    animals = []
    base_prompt = "Add <pettype> -  dog, cat, horse,horse or another unknown pet type\nQuit\n\nEnter your Choice:"
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit" or command == "quit" or command == "QUIT":
            print("Exiting...")
            return
        elif command == "Add" or command == "add" or command == "ADD" and len(words) > 1:
            try:
                if whichone(animals, words[1]):
                    feedback += "You already have a pet with that name\n"
                else:
                    if len(words) > 2:
                        new_pet = whichtype(words[2])
                    else:
                        new_pet = Pet
                    animals.append(new_pet(words[1]))
            except:
                print("enter the details correctly. ")
        for pet in animals:
            feedback += "\n" + pet.__str__()
main()






