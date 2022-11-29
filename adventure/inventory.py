from typing import Dict

from adventure.hooks import Hooks, hookable

class Inventory:
    def __init__(self) -> None:
        self._items: Dict[str, Item] = {}

    def add(self, item: 'Item') -> None:
        self._items[item.id] = item

    def has(self, item_id: str) -> bool:
        return item_id in self._items

    def get(self, item_id: str) -> 'Item':
        return self._items[item_id]

    def remove(self, item_id: str) -> 'Item':
        return self._items.pop(item_id)

class Item:
    def __init__(self, id: str) -> None:
        self.id = id
        self.hooks = Hooks()

    @hookable
    def use(self):
        pass

