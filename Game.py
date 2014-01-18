class Game(object):
    emptyBoard = """
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
""".strip()

    def getDisplay(self):
        return self.emptyBoard

if __name__ == '__main__':
    game = Game()
    game.run()
