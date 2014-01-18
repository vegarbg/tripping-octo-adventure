class Board(object):
    state = None

    def __init__(self):
        self.state = Board.emptyState()

    @staticmethod
    def emptyState():
        return [
            [ " ", " ", " " ],
            [ " ", " ", " " ],
            [ " ", " ", " " ]
        ]

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
        state = Board.renderLine() + "\n"
        state += Board.renderCell( self.state[0][0] ) + Board.renderCell( self.state[0][1] ) + Board.renderCell( self.state[0][2] ) + Board.renderTerminator()
        state += Board.renderLine() + "\n"
        state += Board.renderCell( self.state[1][0] ) + Board.renderCell( self.state[1][1] ) + Board.renderCell( self.state[1][2] ) + Board.renderTerminator()
        state += Board.renderLine() + "\n"
        state += Board.renderCell( self.state[2][0] ) + Board.renderCell( self.state[2][1] ) + Board.renderCell( self.state[2][2] ) + Board.renderTerminator()
        state += Board.renderLine()
        return state

    @staticmethod
    def renderLine():
        return "+---+---+---+"

    @staticmethod
    def renderCell(symbol):
        return "| " + symbol + " "

    @staticmethod
    def renderTerminator():
        return "|\n"

    def fillSquare(self, x, y, symbol):
        self.state[y][x] = symbol
