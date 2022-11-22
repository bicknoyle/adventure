import os
from adventure.room import Room

class Game:
    def __init__(self) -> None:
        self.running = None
        self.current_room = None

        # TODO - make this configurable?
        airlock = Room("Airlock", "This is the airlock room. There are a bunch of flashing lights and things.")
        self.current_room = airlock

        control = Room("Control Room", "This is the control room. There's a whole bunch of controls in here.")
        airlock.set_exit('s', control)

        lab = Room("Laboratory", "This is the laboratory. Science!")
        storage = Room("Storage Room", "You have entered the storage room. The air in here smells musty.")
        control.set_exit('e', lab)
        control.set_exit('w', storage)

    def next(self) -> None:
        command_orig = input("> ")
        if command_orig == "":
            return

        self.parse_and_execute_command(command_orig)

        print("")

    def parse_and_execute_command(self, command_orig: str) -> None:
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

    def run(self) -> bool:
        if self.running is None:
            self.running = True

        print("start_message")
        print("")

        while self.running:
            self.next()

        print("exit_message")

    """
    COMMANDS
    """

    def look(self) -> None:
        print(self.current_room.describe())

    def go(self, direction: str) -> None:
        normalized = direction[0:1]
        if not self.current_room.has_exit(normalized):
            print(f"Can't go {direction}.")
        else:
            room = self.current_room.get_exit(normalized)
            self.current_room = room
            self.look()
