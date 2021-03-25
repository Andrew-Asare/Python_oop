# Let's create our first class
# syntax class is the key word then name of the class

# Creating an Animal class
class Animal():
    # name = "Dog" # class variable
    def __init__(self): # self refers the current class
        self.alive = True # Attributes / variables
        self.spine = True
        self.lungs = True

    def move(self):
        return "moving left right and centre "

    def eat(self):
        return "Keep eating to stay alive "

    def breath(self):
        return "Keep breathing if you want to live "

# creating an object of our Animal class

    # pass # pass is a key word used to by pass the code (so if there is nothing and you use pass it will wont throw an error)

cat = Animal() # creating an object of Animal class
# This will store all the data available in Animal clss into cat
# cat as child has inherited everything from Animal / parent class

# print(cat.eat()) # Absracted eat() method from our parent class
# lET'S MOVE ON TO INHERITANCE

