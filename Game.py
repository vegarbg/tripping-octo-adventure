from Board import Board

class Game(object):
    board = None

    def __init__(self):
        self.board = Board()

    def getDisplay(self):
        return self.board.renderState()

if __name__ == '__main__':
    game = Game()
    game.run()
