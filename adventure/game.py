import os, sys
from adventure.room import Room

class Game:
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

        self.parse_and_execute_command(command)

    def parse_and_execute_command(self, command_orig: str) -> None:
        params = command_orig.strip().lower().split(maxsplit=2)
        command = params[0]
        argument = params[1] if len(params) == 2 else None

        if command == "exit" and not argument:
            self.exit()
        elif command == "look" and not argument:
            self.look()
        elif command == "go" and argument:
            self.go(argument)
        else:
            self.output(f"Can't {command_orig} here.")

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
        room = self.current_room.get_exit(normalized)
        if not room:
            self.output(f"Can't go {direction}.")
        else:
            self.current_room = room
            self.look()

    def exit(self) -> None:
        self.output(self.exit_message)
        self.running = False
