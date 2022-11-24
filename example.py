from adventure.game import Game
from adventure.room import Room
from adventure.event import EventError

airlock = Room("Airlock", "This is the airlock room. There are a bunch of flashing lights and things. To your north the door leads into the void of space, to the south you hear a faint series of beeps and blips.")

control = Room("Control Room", "This is the control room. There's a whole bunch of controls in here beeping and making other computery noises.")
airlock.set_exit('s', control)

lab = Room("Laboratory", "This is the laboratory. Science!")
storage = Room("Storage Room", "You have entered the storage room. The air in here smells musty.")
control.set_exit('e', lab)
control.set_exit('w', storage)

space = Room("Space", "The cold dark of space. Here without a suit, you die.")
airlock.set_exit('n', space)
def airlock_outer_door(direction: str) -> None:
    if direction == 'n':
        print("You try to open the outer airlock door, but it won't open. Which is a good thing, because you're not wearing a suit!")
        raise EventError()

airlock.emitter.on('get_exit', airlock_outer_door)

if __name__ == "__main__":
    game = Game()
    game.set_start_message("Welcome to adventure! This is the example game.")
    game.set_exit_message("Thanks for playing!")
    game.set_current_room(airlock)
    game.run()