class Person():
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age
        self.email = email

# Creating an object of the Person class with attributes
p = Person("John Doe", 25, "john.doe@example.com")

# Accessing and printing the attributes
print(f"Name: {p.name}, Age: {p.age}, Email: {p.email}")