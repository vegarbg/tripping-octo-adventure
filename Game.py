from Board import Board

class Game(object):
    board = None
    clicked = False

    def __init__(self):
        self.board = Board()

    def getDisplay(self):
        if self.clicked:
            return """
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip()
        else:
            return self.board.renderState()

    def clickSquare(self, x, y):
        self.clicked = True

if __name__ == '__main__':
    game = Game()
    game.run()
