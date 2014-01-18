import unittest

from Board import Board

class TestBoard(unittest.TestCase):
    def test_square_is_filled_on_click(self):
        # Given: The board is empty
        # When: The player clicks a square
        # Then: The square is filled with the current player's symbol
        pass

    def test_can_be_instantiated(self):
        board = Board()

    def test_render_state_returns_string(self):
        board = Board()
        state = board.renderState()
        self.assertTrue( isinstance(state, str) )

    def test_board_state_is_empty_when_created(self):
        # Given: 
        # When: The board is created.
        board = Board()
        # Then: An empty board is generated.
        self.assertEquals( board.renderState(), self.emptyBoard() )

    def emptyBoard(self):
        return """
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip()
