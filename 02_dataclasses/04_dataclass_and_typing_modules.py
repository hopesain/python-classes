from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class Person:
    name: str
    age: int
    email: str
    house_coordinates: Tuple
    height: float = 150.0 #The defaults should always be at the end.

first_person = Person("Mirror Canesat", 23, "sainhope16@gmail.com", (1234423.33, -234233))
print(first_person)

@dataclass
class People:
    people: List[Person]

joe = Person('Joe', 25, 'joe@dataquest.io', (40.748441, -73.985664))
mary = Person('Mary', 43, 'mary@dataquest.io', (-73.985664, 40.748441))

people = People([joe, mary])
print(people)