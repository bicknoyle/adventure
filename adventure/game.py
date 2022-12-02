import re
import sys
from adventure.player import Player
from adventure.rooms import Room
from adventure.exceptions import AdventureError, CommandNotFoundError, InventoryNotFoundError, ItemUseError

class Game:
    COMMANDS = {
        "^look$": "look",
        "^exit$": "exit",
        "^quit$": "exit",
        "^go (n|s|e|w|north|south|east|west)$": "go",
        "^get ([0-9A-Za-z_\- ]+)$": "get",
        "^examine ([0-9A-Za-z_\- ]+)$": "examine",
        "^use ([0-9A-Za-z_\- ]+)$": "use",
    }

    def __init__(self) -> None:
        self.running: bool = None
        self.current_room: Room = None
        self.start_message = ""
        self.exit_message = ""
        self.output_handle = sys.stdout
        self.player = Player()

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
            try:
                fn(*args)
            except AdventureError as e:
                self.output(str(e).format(*args))
            return

        self.output(str(CommandNotFoundError()).format(command))

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
        self.current_room = self.current_room.exits.get(normalized)
        self.look()

    def exit(self) -> None:
        self.output(self.exit_message)
        self.running = False

    def get(self, item_id: str) -> None:
        item = self.current_room.inventory.remove(item_id)
        self.player.inventory.add(item)
        self.output(f"You picked up {item.id}.")

    def examine(self, item_id: str) -> None:
        if self.current_room.inventory.has(item_id):
            self.output(self.current_room.inventory.get(item_id).describe())
        self.output(self.player.inventory.get(item_id).describe())

    def use(self, item_id: str) -> None:
        if not self.player.inventory.has(item_id):
            raise InventoryNotFoundError()
        elif result := self.current_room.use(item_id):
            # TODO: output if string?
            pass
        elif result := self.player.inventory.get(item_id).use():
            # TODO: output if string?
            pass
        else:
            raise ItemUseError()
