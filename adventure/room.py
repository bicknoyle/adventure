from adventure.utils import make_compass_dict, get_reverse_direction, COMPASS_SHORT_MAP

class Room:
    def __init__(self, name: str, description: str="") -> None:
        self.name = name
        self.description = description
        self.exits = make_compass_dict()
        self.gates = make_compass_dict()

    def has_exit(self, direction: str) -> bool:
        assert direction in self.exits
        return self.exits[direction] is not None

    def can_exit(self, direction: str) -> bool:
        return self.has_exit(direction) and self.check_gate(direction)

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

    def set_gate(self, directon: str, callback) -> None:
        assert directon in self.gates
        self.gates[directon] = callback

    def check_gate(self, direction: str) -> None:
        assert direction in self.gates
        if self.gates[direction] is None:
            return True
        return self.gates[direction](self)

    def get_available_exits(self):
        return tuple(d for d in self.exits.keys() if self.has_exit(d) and self.check_gate(d))

    def describe(self) -> str:
        descr = f"# {self.name}" + "\n" + self.description.strip() + "\n" + "Exits: "

        available_exits = self.get_available_exits()
        if len(available_exits):
            descr += ", ".join(map(lambda d: COMPASS_SHORT_MAP[d].capitalize(), available_exits))
        else:
            descr += "(none)"

        return descr
