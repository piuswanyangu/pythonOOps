class Person:
    def __init__(self,fname,age,year,gender):
        self.fname = fname
        self.age = age
        self.year = year
        self.gender = gender

    def eat(self):
        print(f"{self.fname} is eating")

    def walk(self):
        print("The person is walking")


