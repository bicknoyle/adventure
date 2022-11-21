import unittest

from adventure.room import Room 

class TestRoom(unittest.TestCase):
    def test_new(self):
        room = Room(id='lobby', name='Lobby', description='This is a lobby', exits={})
        self.assertIsInstance(room, Room)
    
    def test_exits(self):
        exits = {'n': 'elevator'}
        room = Room(id='lobby', name='Lobby', description='This is a lobby', exits=exits)
        
        self.assertFalse(room.has_exit('s'))
        self.assertTrue(room.has_exit('n'))

        self.assertIsNone(room.get_exit_id('s'))
        self.assertEqual(room.get_exit_id('n'), 'elevator')
