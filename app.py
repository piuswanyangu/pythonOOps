from pple import Person
from dog import Dog
# print("Hello World")
# age = 21
# fname = "Mike satori"
# print(f"my names are {fname} and am {age}")

# how to access class properties
person1 = Person("Jeff Kuria",23,2000,"male")
print(person1.fname)
print(person1.age)
print(person1.year)
print(person1.gender)

# how to call a method from a class
person1.eat()

# Dog section
dog1 = Dog("Boss","Brown","German shephered")
print(dog1.name)
print(dog1.color)
print(dog1.breed)

dog1.run()