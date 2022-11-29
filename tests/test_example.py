import unittest
import io

from example.game import setup_game

class TestExample(unittest.TestCase):
    def setUp(self) -> None:
        self.game = setup_game()
        self.output = io.StringIO()
        self.game.set_output_handle(self.output)

    def test_play_example(self):
        game = self.game

        game.start()
        self.assertTrue(game.running)
        self.assertOutputContains(r'(?i)welcome to adventure')

        # commands that don't work
        # TODO: move these to their own test?
        game.next('go east')
        self.assertOutputContains(r'(?i)can\'t go east')
        game.next('foobar')
        self.assertOutputContains(r'(?i)can\'t foobar')
        game.next('get foobar')
        self.assertOutputContains(r'no foobar')
        game.next('examine foobar')
        self.assertOutputContains(r'no foobar')

        game.next('look')
        self.assertOutputContains(r'airlock')

        game.next('go north')
        game.next('look')
        self.assertOutputContains(r'(?i)you try to open', truncate=False)
        self.assertOutputContains(r'airlock')

        game.next('go south')
        self.assertOutputContains(r'control room')

        game.next('go west')
        self.assertOutputContains(r'storage')

        game.next('go east')
        game.next('go east')
        self.assertOutputContains(r'laboratory')

        self.assertTrue(game.current_room.inventory.has('keycard'))

        game.next('examine keycard')
        self.assertOutputContains(r'get keycard to examine')

        game.next('get keycard')
        self.assertOutputContains(r'picked up keycard')
        self.assertFalse(game.current_room.inventory.has('keycard'))
        self.assertTrue(game.player.inventory.has('keycard'))

        game.next('examine keycard')
        self.assertOutputContains(r'An access keycard')

        game.next('exit')
        self.assertOutputContains(r'(?i)thanks for playing')
        self.assertFalse(game.running)

    def assertOutputContains(self, regex, message: str=None, truncate: bool=True) -> None:
        self.assertRegex(self.output.getvalue(), regex, message)

        if truncate:
            self.output.seek(0)
            self.output.truncate()
