import os
import unittest

from adventure.game import Game 

class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game(data_dir=os.path.join(os.getcwd(), 'data'))
        self.game.load()
        self.game.running = True
    
    def test_all(self) -> None:
        game = self.game

        game.parse_and_execute_command('look')
        game.parse_and_execute_command('go s')
        game.parse_and_execute_command('go e')
        game.parse_and_execute_command('go w')
        game.parse_and_execute_command('exit')

        self.assertFalse(game.running)