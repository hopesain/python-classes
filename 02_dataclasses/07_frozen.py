#By default this parameter is False, when set to True, frozen doesn't allow us to modify the attributes of an object after it's created.

from dataclasses import dataclass

@dataclass()
class Person:
    name: str
    age: int
    email: str

hope = Person("Hope", 23, "hope@email.com")

hope.age = 24

print(hope)

#Setting the frozen to True

@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str

sain = User("Sain", 25, "sain@email.com") #Attempts to modify this throws an error.

print(sain) 

"""
sain.age = 23 # Attempting to change the age variable and check if it throws an error.

print(sain) #It returns a FrozenInstanceError.
"""

# The genius you, is currently asking what if I want to freeze a single attribute.
# Let's say we have a student class with two attributes, student_id (immutable), name (mutable).

@dataclass(frozen=True)
class StudentID:
    student_id: str 

@dataclass()
class Student:
    id: StudentID
    name: str

student = Student(StudentID("abc123"), "Hope Sain")

student.id = StudentID("xyz789")

print(student)

# Lol, I thought I may change this but hell na, it is not working as intended. When I find time, will get back to this. 
# Let me name the commit, will get back to this later.