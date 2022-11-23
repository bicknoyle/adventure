from adventure.game import Game
from adventure.room import Room

airlock = Room("Airlock", "This is the airlock room. There are a bunch of flashing lights and things.")

control = Room("Control Room", "This is the control room. There's a whole bunch of controls in here.")
airlock.set_exit('s', control)

lab = Room("Laboratory", "This is the laboratory. Science!")
storage = Room("Storage Room", "You have entered the storage room. The air in here smells musty.")
control.set_exit('e', lab)
control.set_exit('w', storage)

if __name__ == "__main__":
    game = Game()
    game.set_start_message("Welcome to adventure! This is the example game.")
    game.set_exit_message("Thanks for playing!")
    game.set_current_room(airlock)
    game.run()