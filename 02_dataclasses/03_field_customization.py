from dataclasses import dataclass, field
from typing import List

@dataclass
class ShoppingCart:
    user: str
    items: List[str] = field(default_factory=list)
    total: float = 0.0
    _secret_token: str = field(default="abc123", repr=False)

    def add_item(self, item: str, price: float):
        self.items.append(item)
        self.total += price


cart = ShoppingCart("Hope")
cart.add_item("Python Book", 50)
cart.add_item("Keyboard", 30)

print(cart)
