import unittest

from adventure.event import EventEmitter

class TestEventEmitter(unittest.TestCase):
    def test_emit(self):
        emitter = EventEmitter()

        def this_explodes():
            assert False

        emitter.on('my_event', this_explodes)

        with self.assertRaises(AssertionError):
            emitter.emit('my_event')
