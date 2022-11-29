from typing import Dict

from adventure.exceptions import ExitNotFoundError
from adventure.hooks import hookable, Hooks
from adventure.utils import make_compass_dict, get_reverse_direction, COMPASS_SHORT_MAP

class Exits:
    DIRECTIONS = {'n', 's', 'e', 'w'}

    def __init__(self, owner) -> None:
        self._rooms: Dict[str, Room] = {}
        self._owner: Room = owner
        self.hooks = Hooks()

    def set(self, direction: str, room: 'Room', reverse=True) -> None:
        assert direction in self.DIRECTIONS
        self._rooms[direction] = room

        if reverse:
            room.exits.set(get_reverse_direction(direction), self._owner, reverse=False)

    def has(self, direction: str) -> bool:
        assert direction in self.DIRECTIONS

        return direction in self._rooms

    @hookable
    def get(self, direction: str) -> 'Room':
        if not self.has(direction):
            raise ExitNotFoundError()

        return self._rooms[direction]

    def remove(self, direction: str) -> 'Room':
        return self._rooms.pop(direction)

    def available_directions(self):
        return tuple(d for d in self._rooms.keys())

class Room:
    def __init__(self, name: str, description: str="") -> None:
        self.name = name
        self.description = description
        self.exits = Exits(self)
        self.hooks = Hooks()

    def describe(self) -> str:
        descr = f"# {self.name}" + "\n" + self.description.strip() + "\n" + "Exits: "

        available_exits = self.exits.available_directions()
        if len(available_exits):
            descr += ", ".join(map(lambda d: COMPASS_SHORT_MAP[d].capitalize(), available_exits))
        else:
            descr += "(none)"

        return descr
