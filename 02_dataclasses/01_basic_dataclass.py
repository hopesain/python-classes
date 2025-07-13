from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

p1 = Person("hopeSain", 23, "hopesain@gmail.com")
p2 = Person("johnDoe", 26, "johndoe@gmail.com")

print(p1)
print(p1 == p2) 