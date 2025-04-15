class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! ")
    
    def blow_bubbles(self):
        print(f"{self.name} blows bubbles! ")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! ")
    
    def build_nest(self):
        print(f"{self.name} is building a nest! ")

class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! ")
    
    def shed_skin(self):
        print(f"{self.name} is shedding its skin! ")

if __name__ == "__main__":
    print("\n=== Animal Polymorphism Demonstration ===")
    
    nemo = Fish("Nemo")
    tweety = Bird("Tweety")
    kaa = Snake("Kaa")
    
    animals = [nemo, tweety, kaa]
    
    for animal in animals:
        animal.move()
    
    print("\n=== Unique Methods ===")
    nemo.blow_bubbles()
    tweety.build_nest()
    kaa.shed_skin()