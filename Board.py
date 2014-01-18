class Board(object):
    state = None

    def __init__(self):
        self.state = Board.emptyBoard()

    @staticmethod
    def emptyBoard():
        return """
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip()

    def renderState(self):
        return self.state

    def fillSquare(self, x, y, symbol):
        self.state = """
+---+---+---+
| X |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip()
