import unittest

from Game import Game

class TestGame(unittest.TestCase):
    def test_getDisplay_returns_a_string(self):
        game = Game()
        value = game.getDisplay()
        self.assertTrue( isinstance(value, str) )
