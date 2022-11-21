from typing import Dict
from adventure.constants import COMPASS_SHORT_MAP

class Room:
    def __init__(self, id: str, name: str, description: str, exits: Dict[str, str]) -> None:
        self.id = id
        self.name = name 
        self.description = description
        self.exits = exits
    
    def has_exit(self, direction: str) -> bool:
        return direction in self.exits

    def get_exit_id(self, direction: str) -> str:
        if self.has_exit(direction):
            return self.exits[direction]

    def __str__(self) -> str:
        display = "# " + self.name + "\n" + self.description.strip() + "\n" + "Exits: "

        if len(self.exits):
            display += ", ".join(map(lambda d: COMPASS_SHORT_MAP[d].capitalize(), self.exits.keys()))
        else:
            display += "(none)"

        return display
