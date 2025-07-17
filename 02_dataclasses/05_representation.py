from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str

    def __repr__(self):
        return (f"My name is {self.name}, I am {self.age} years old.")
    
person = Person("Hope Sain", 23, "sainhope16@gmail.com")

print(person)