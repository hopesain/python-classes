class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

    def is_adult(self):
        return self.age >= 18
    
# Creating an object of the Person class
p = Person("Hope", 23)

# Call methods
p.greet()
print(p.is_adult())
        