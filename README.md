# Python OOP
# Why OOP

## Four pillars of OOP with use cases

## Python OOP examples

### Creating the parent class
- First we create a parent class, in this case Animal
```python
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
```
### Next we create a child class 
- The child class is used so that it can inherit attributes from its parent
- In this case the first child class is Reptile
```python
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
# print(reptile_object.seek_heat())
```

- The next child class is Snake
```python
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
print(snake_object.venom)
# print(snake_object.limbs)

```
- and finally Python will be the last child class
```python
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False
    def climb(self):
        return "Up we go"

    def swollow(self):
        return "Don't chew"
python_object = Python()
# print(python_object.large)
print(python_object.venom)
```
### Polymorphism 
Here is an example of polymorphism with the snake adder
- it takes the attribute venom and changes it
```python
from snake import Snake


class Adder(Snake):

    def __init__(self):
        super().__init__()
        self.venom = False  # You can override values of the parent class, this is polymorphism

    def smell(self):  # You can also override the method of the parent class, this is polymorphism
        return "I smell like an adder"


if __name__ == "__main__":
    james = Adder()
    print(james.venom)
    print(james.smell())
```
