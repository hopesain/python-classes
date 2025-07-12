class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
# Creating an object of the Person class
p = Person("Alice", 30)

# Using the __str__ method
print(str(p))
print(repr(p))
print(p)