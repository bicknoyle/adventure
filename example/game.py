import os, sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from adventure.game import Game
from adventure.room import Room
from adventure.hooks import HookError

def load_copy(copydeck) -> None:
    cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')) + os.path.sep
    for file in Path(cwd).rglob('*.txt'):
        with open(file, 'r') as fp:
            path = Path(str(file).replace(cwd, ''))
            key = '.'.join(path.with_suffix('').parts)
            copydeck[key] = fp.read()

def setup_game():
    game = Game()

    copydeck = {}
    load_copy(copydeck)

    game.set_start_message(copydeck.get('start_message'))
    game.set_exit_message(copydeck.get('exit_message'))

    airlock = Room("Airlock", copydeck.get('airlock.description'))

    control = Room("Control Room", copydeck.get('control.description'))
    airlock.set_exit('s', control)

    lab = Room("Laboratory", copydeck.get('lab.description'))
    storage = Room("Storage Room", copydeck.get('storage.description'))
    control.set_exit('e', lab)
    control.set_exit('w', storage)

    space = Room("Space", copydeck.get('space.description'))
    airlock.set_exit('n', space)
    def airlock_outer_door(self, direction: str) -> None:
        if direction == 'n':
            game.output(copydeck.get('airlock.exit_n'))
            raise HookError()

    airlock.hooks.on('pre_get_exit', airlock_outer_door)

    game.set_current_room(airlock)

    return game

if __name__ == "__main__":
    game = setup_game()
    game.run()