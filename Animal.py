# Animal.py
# by Danny Dang
# created 2-20-2024

class Animal:
    has_brain = True
    is_alive = True
    age = 0
    name = None


    def move(self, speed, direction, distance):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def chirp(self):
        print("""
       _------.
      /  ,     \\_
    /   /  /{}\\ |o\\_
   /    \\  `--' /-' \\
  |      \\      \\    |         _________________
 |              |`-, |        /Give me you money\\
 /              /__/)/        \\_________________/
|              |
""")
    
Billy = Bird("Billy", 16)
print(f"This is {Billy.name}, he is a {Billy.age} years old")
print(f"Isn't he cute?! Listen to him talk")
Billy.chirp()