class Person:
    # Class attribute
    species = "Human"

    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute

# Create two objects
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# Instance attributes (unique)
print(p1.name)    # Alice
print(p2.name)    # Bob

# Class attribute (shared)
print(p1.species)  # Human
print(p2.species)  # Human


# Change class attribute for all
Person.species = "Homo sapiens"

print(p1.species)  # Homo sapiens
print(p2.species)  # Homo sapiens