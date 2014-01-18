import unittest

from Board import Board

class TestBoard(unittest.TestCase):
    def test_board_state_is_empty_when_created(self):
        # Given: 
        # When: The board is created.
        board = Board()
        # Then: An empty board is generated.
        self.assertEquals( board.renderState(), self.emptyBoard() )

    def test_can_be_instantiated(self):
        board = Board()

    def test_render_state_returns_string(self):
        board = Board()
        state = board.renderState()
        self.assertTrue( isinstance(state, str) )

    def test_emptyBoard_returns_empty_board(self):
        self.assertEquals( Board.emptyBoard(), self.emptyBoard() )

    def test_changes_board_state_on_fillSquare(self):
        board = Board()
        board.fillSquare( 0, 0, "X" )
        self.assertEquals( board.renderState(), """
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip() )
        board.fillSquare( 1, 0, "X" )
        self.assertEquals( board.renderState(), """
+---+---+---+
| X | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip() )

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
