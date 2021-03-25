# Let's import reptile class

from reptile import Reptile

class Snake(Reptile):
    
    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.forked_toungue = True

    def use_tounge_to_smell(self):
        return "I use my tounge to smell the food"
    def shed_skin(self):
        return "growing out "
snake_object = Snake()
print(snake_object.limbs)
