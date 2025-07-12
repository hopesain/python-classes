from datetime import date

class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18
    
    @classmethod
    def from_year_of_birth(cls, name, birth_year):
        age = date.today().year - birth_year
        return cls(name, age)



# Using the static method and it returns a boolean.
print(Person.is_adult(20))

# Using the class method to create an instance from year of birth.
p = Person.from_year_of_birth("hopeSain", 2001)
print(p.name, p.age)

# Regular method (uses self)
p2 = Person("Alice", 30)
print(p2.name, p2.species)
