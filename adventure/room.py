from adventure.utils import get_reverse_direction, COMPASS_SHORT_MAP

class Room:
    def __init__(self, name: str, description: str="") -> None:
        self.name = name
        self.description = description
        self.exits = {k: None for k in ['n', 's', 'e', 'w']}

    def has_exit(self, direction: str) -> bool:
        assert direction in self.exits
        return self.exits[direction] is not None

    def get_exit(self, direction: str) -> 'Room':
        if not self.has_exit(direction):
            return None
        else:
            return self.exits[direction]

    def set_exit(self, direction: str, room: 'Room', reverse: bool=True) -> None:
        assert direction in self.exits
        self.exits[direction] = room
        if reverse:
            room.exits[get_reverse_direction(direction)] = self
        else:
            room.exits[get_reverse_direction(direction)] = None

    def describe(self) -> str:
        descr = f"# {self.name}" + "\n" + self.description.strip() + "\n" + "Exits: "

        if len(self.exits):
            descr += ", ".join(map(lambda d: COMPASS_SHORT_MAP[d].capitalize(), [k for k, v in self.exits.items() if v is not None]))
        else:
            descr += "(none)"

        return descr