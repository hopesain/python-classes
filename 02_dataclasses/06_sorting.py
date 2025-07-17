from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    name: str
    age: int
    email: str


joe = Person('Joe', 25, 'joe@dataquest.io')
mary = Person('Mary', 43, 'mary@dataquest.io')

print(joe > mary) #This approach sorts based on the first later, alphabetical order. M comes after J, so Joe cannot be greater than Mary.


@dataclass(order=True)
class User:
    sort_index: int = field(init=False, repr=False) #using field to create a sort index attribute.
    name: str
    age: int
    email: str

    def __post_init__(self):
        self.sort_index = self.age #Specifying the sorting criteria to use age.


john = User('John', 25, 'joe@dataquest.io')
doe = User('Doe', 43, 'mary@dataquest.io')

print(doe > john)