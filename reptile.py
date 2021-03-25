from animal import Animal  # this is to ensure Animal class is inherited


class Reptile(Animal):  # We need to pass the animal class as an arg in our reptile class

    def __init__(self):
        super().__init__()  # super is used to make everything available from parent class
        self.cold_blooded = True
        self.tetrapod = None
        self.hear_chamber = [3, 4]

    def hunt(self):
        return "Working hard to catch the next meal"

    def use_venom(self):
        return "I use it if i have to"

    def seek_heat(self):
        return "Looking for sunshine"

    # lets see amazing benefits of OOP


reptile_object = Reptile()
# Time to see what
print(reptile_object.seek_heat())
