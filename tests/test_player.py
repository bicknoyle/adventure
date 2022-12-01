import unittest

from adventure.player import Player

class TestPlayer(unittest.TestCase):
    def test_new(self):
        player = Player()

        self.assertIsInstance(player, Player)
