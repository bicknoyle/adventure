import unittest

from adventure.hooks import Hooks

class TestHooks(unittest.TestCase):
    def test_run(self):
        hooks = Hooks()

        self.assertIsNone(hooks.run('my_event'))

        def this_is_truthy():
            return True

        hooks.on('my_event', this_is_truthy)
        self.assertTrue(hooks.run('my_event'))

        def this_explodes():
            assert False

        hooks.on('my_event', this_explodes)
        with self.assertRaises(AssertionError):
            hooks.run('my_event')
