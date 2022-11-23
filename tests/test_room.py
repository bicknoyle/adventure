import unittest

from adventure.room import Room

class TestRoom(unittest.TestCase):
    def test_construct(self):
        room = Room(name='Lobby')
        self.assertIsInstance(room, Room)

    def test_exits(self):
        lobby = Room(name='Lobby')
        self.assertFalse(lobby.has_exit('s'))

        elevator = Room(name='Elevator Room')
        lobby.set_exit('s', elevator)
        self.assertTrue(lobby.can_exit('s'))
        self.assertTrue(elevator.can_exit('n'))

        lobby.set_exit('s', elevator, reverse=False)
        self.assertFalse(elevator.can_exit('n'))

        with self.assertRaises(AssertionError):
            lobby.set_exit('x', elevator)

        self.assertEqual(lobby.get_exit('s'), elevator)

    def test_gates(self):
        room_a = Room(name='Room A')
        room_b = Room(name='Room B')

        def falsey_gate(room):
            pass

        room_a.set_exit('e', room_b)
        room_a.set_gate('e', falsey_gate)
        self.assertFalse(room_a.check_gate('e'))
        self.assertFalse(room_a.can_exit('e'))
        self.assertEqual(room_a.get_available_exits(), ())

        print(room_a.describe())

        def truthy_gate(room):
            return True

        room_a.set_gate('e', truthy_gate)
        self.assertTrue(room_a.check_gate('e'))
        self.assertTrue(room_a.can_exit('e'))
        self.assertEqual(room_a.get_available_exits(), ('e',))
