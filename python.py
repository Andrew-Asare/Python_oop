from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = True
    def climb(self):
        return "Up we go"

    def swollow(self):
        return "Don't chew"
python_object = Python()
# print(python_object.large)
print(python_object.venom)