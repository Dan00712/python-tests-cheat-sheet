from typing import Self, List
from dataclasses import dataclass

@dataclass
class ShoppingItem:
    """Represents a Shopping Cart Item"""
    name: str
    price:int 

class ShoppingCart:
    def __init__(self):
        self._items:List[ShoppingItem] = []

    @property
    def items(self) -> List[ShoppingItem]:
        return self.items
    
    def append(self, item:ShoppingItem):
        self._items.append(item)
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, i:int)->ShoppingItem:
        return self._items[i]
    
