class Board(object):
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
        return Board.emptyBoard()
