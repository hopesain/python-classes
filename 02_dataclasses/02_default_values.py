from dataclasses import dataclass

@dataclass
class Book:
    title: str 
    author: str
    price: float = 100.0
    available: bool = False

first_book = Book("Unsung songs", "Hope Sain", 50.5, True)
second_book = Book("Looking for rain god", "Uncle Ben")
third_book = Book("Trying hard", "Anthu Adabwa", available=True)

print(first_book)
print(second_book)
print(third_book)