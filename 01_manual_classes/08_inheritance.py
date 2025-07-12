class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Call the parent class constructor
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

s = Student("HopeSain", 23, "S12345")

s.greet()
s.study()
print(s.student_id)