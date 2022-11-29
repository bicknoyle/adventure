import unittest

from adventure.rooms import Room

class TestRoom(unittest.TestCase):
    def test_exits(self):
        lobby = Room(name='Lobby')
        self.assertFalse(lobby.exits.has('s'))

        elevator = Room(name='Elevator Room')
        lobby.exits.set('s', elevator)
        self.assertTrue(lobby.exits.has('s'))
        self.assertTrue(elevator.exits.has('n'))

        elevator.exits.remove('n')
        lobby.exits.set('s', elevator, reverse=False)
        self.assertFalse(elevator.exits.has('n'))

        with self.assertRaises(AssertionError):
            lobby.exits.has('x')

        self.assertEqual(lobby.exits.get('s'), elevator)

    def test_exits_get_hook(self):
        lobby = Room(name='Lobby')
        elevator = Room(name='Elevator Room')
        other = Room(name='Other Room')
        lobby.exits.set('s', elevator)

        def exit_override(self, direction: str) -> None:
            if direction == 's':
                return other

        lobby.exits.hooks.on('pre_get', exit_override)

        self.assertEqual(lobby.exits.get('s'), other)
