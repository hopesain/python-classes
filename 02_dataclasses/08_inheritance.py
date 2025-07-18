from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    age: int

@dataclass(order=True)
class Employee(Person):
    salary: str

first_employee = Employee("Hope", 23, "150,000")
second_employee = Employee("Sain", 24, "350,000")

print(first_employee)
print(second_employee)