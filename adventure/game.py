import os
import yaml

from adventure.room import Room

class Game:
    def __init__(self, data_dir: str) -> None:
        self.running = None
        self.data_dir = data_dir
        self.config = {}
        self.rooms = {}
        self.current_room = None

    def load(self) -> None:
        with open(os.path.join(self.data_dir, "index.yml"), "r") as fp:
            self.config = yaml.safe_load(fp)

        with open(os.path.join(self.data_dir, "rooms.yml"), "r") as fp:
            self.rooms = yaml.safe_load(fp)
        
        self.set_room(id=self.config['start'])

    def set_room(self, id) -> None:
        rconfig = self.rooms[id]
        self.current_room = Room(id=id, name=rconfig['name'], description=rconfig['description'], exits=rconfig.get('exits', {}))
            
    def next(self) -> None:
        command_orig = input("> ")
        params = command_orig.strip().lower().split(maxsplit=2)
        command = params[0]
        argument = params[1] if len(params) == 2 else None

        if command == "exit" and not argument:
            self.running = False
        elif command == "look" and not argument:
            self.look()
        elif command == "go" and argument:
            self.go(argument)
        else:
            print(f"Can't {command_orig} here.")

        print("")

    def run(self) -> bool:
        if self.running is None:
            self.load()
            self.running = True

        print(self.config['start_message'])
        print("")
        
        while self.running:
            self.next()

        print(self.config['exit_message'])

    """
    COMMANDS
    """

    def look(self) -> None:
        print(self.current_room)

    def go(self, direction: str) -> None:
        normalized = direction[0:1]
        if normalized not in self.current_room.exits:
            print("Can't go {direction}.")
        else:
            id = self.current_room.exits[normalized]
            self.set_room(id)
            self.look()
