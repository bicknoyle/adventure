import unittest

from adventure.room import Room
from adventure.event import EventError

class TestRoom(unittest.TestCase):
    def test_construct(self):
        room = Room(name='Lobby')
        self.assertIsInstance(room, Room)

    def test_exits(self):
        lobby = Room(name='Lobby')
        self.assertFalse(lobby.has_exit('s'))

        elevator = Room(name='Elevator Room')
        lobby.set_exit('s', elevator)
        self.assertTrue(lobby.has_exit('s'))
        self.assertTrue(elevator.has_exit('n'))

        lobby.set_exit('s', elevator, reverse=False)
        self.assertFalse(elevator.has_exit('n'))

        with self.assertRaises(AssertionError):
            lobby.set_exit('x', elevator)

        self.assertEqual(lobby.get_exit('s'), elevator)

    def test_get_exit_event(self):
        lobby = Room(name='Lobby')
        elevator = Room(name='Elevator Room')
        lobby.set_exit('s', elevator)

        def this_explodes(direction: str) -> None:
            raise EventError()

        lobby.emitter.on('get_exit', this_explodes)

        self.assertIsNone(lobby.get_exit('s'))
