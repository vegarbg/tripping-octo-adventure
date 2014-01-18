import unittest

from Game import Game
from Board import Board

class TestGame(unittest.TestCase):
    def test_square_is_filled_on_click(self):
        # Given: The board is empty
        game = Game()
        # When: The player clicks a square
        game.clickSquare( 0, 0 )
        # Then: The square is filled with the current player's symbol
        self.assertEquals( game.getDisplay(), """
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip() )

    def test_a_board_is_displayed_when_the_game_is_started(self):
        # Given: 
        # When: The game is started.
        game = Game()
        # Then: An empty board is generated.
        self.assertEquals( game.getDisplay(), Board.emptyBoard() )

    def test_getDisplay_returns_a_string(self):
        game = Game()
        value = game.getDisplay()
        self.assertTrue( isinstance(value, str) )
