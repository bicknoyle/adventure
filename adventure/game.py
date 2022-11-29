import re
import sys
from adventure.rooms import Room
from adventure.exceptions import ExitNotFoundError

class Game:
    COMMANDS = {
        "^look$": "look",
        "^exit$": "exit",
        "^go (n|s|e|w|north|south|east|west)$": "go"
    }

    def __init__(self) -> None:
        self.running: bool = None
        self.current_room: Room = None
        self.start_message = ""
        self.exit_message = ""
        self.output_handle = sys.stdout

    def set_current_room(self, room: 'Room') -> None:
        self.current_room = room

    def set_start_message(self, message: str) -> None:
        self.start_message = message

    def set_exit_message(self, message: str) -> None:
        self.exit_message = message

    def set_output_handle(self, handle) -> None:
        self.output_handle = handle

    def next(self, command: str=None) -> None:
        # TODO: refactor
        if command is None:
            command = input("> ")
        if command == "":
            return

        self.run_command(command)

    def run_command(self, command: str) -> None:
        for pattern, method in self.COMMANDS.items():
            p = re.compile(pattern)
            m = p.match(command)
            if not m:
                continue
            args = m.groups()
            fn = getattr(self, method)
            fn(*args)
            return

        self.output(f"Can't {command} here.")

    def start(self) -> None:
        if self.running is None:
            self.running = True
        else:
            raise Exception("Already started!")

        self.output(self.start_message)

    def run(self) -> bool:
        self.start()

        while self.running:
            self.next()

    def output(self, message: str):
        print(message, file=self.output_handle)

    """
    COMMANDS
    """

    def look(self) -> None:
        self.output(self.current_room.describe())

    def go(self, direction: str) -> None:
        normalized = direction[0:1]
        room = None
        try:
            room = self.current_room.exits.get(normalized)
        except ExitNotFoundError as e:
            self.output(f"Can't go {direction}.")
        else:
            self.current_room = room
            self.look()

    def exit(self) -> None:
        self.output(self.exit_message)
        self.running = False
