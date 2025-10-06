class Dog:
    def __init__(self,name,color,breed):
        self.name = name
        self.color =color
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking woo woo")
    def run(self):
        print(f"{self.name} is {self.color} and is running as fast as {self.breed}")
        