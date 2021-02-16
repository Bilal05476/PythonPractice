class PartyAnimal:
    x = 0
    def party(self):
        self.x += 1
        print("So far", self.x)
animal = PartyAnimal()

animal.party()
animal.party()
animal.party()
