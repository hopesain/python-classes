#By default this parameter is False, when set to True, frozen doesn't allow us to modify the attributes of an object after it's created.

from dataclasses import dataclass

@dataclass()
class Person:
    name: str
    age: int
    email: str

hope = Person("Hope", 23, "hope@email.com")

hope.age = 24

print(hope)

#Setting the frozen to True

@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str

sain = User("Sain", 25, "sain@email.com") #Attempts to modify this throws an error.

print(sain) 

sain.age = 23 # Attempting to change the age variable and check if it throws an error.

print(sain) #It returns a FrozenInstanceError.
