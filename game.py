import os

from adventure.game import Game

if __name__ == "__main__":
    game = Game(data_dir=os.path.join(os.getcwd(), "data"))
    game.run()