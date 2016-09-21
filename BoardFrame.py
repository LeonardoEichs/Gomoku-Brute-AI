from PyQt4 import QtGui, QtCore
import Square
import Board

class BoardFrame(QtGui.QFrame):
    playSignal = QtCore.pyqtSignal(Square.Square)
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self, parent):
        super(BoardFrame, self).__init__(parent)
        self.board = Board.Board()
        self.squares = {}
        self.initBoard()

    def __repr__(self):
        return self.board

    def __getitem__(self, key):
        return self.board[key]


    def initBoard(self):
        i = 0
        for n in range(self.BoardHeight):
            ii = 0
            for m in range(self.BoardWidth):
                square = Square.Square(self, n, m)
                self.squares[str(square.m)+","+str(square.n)] = square
                square.setGeometry(ii, i, 40, 40)
                if ((m == 7 and n == 7) or
                    (m == 4 and n == 4) or (m == 4 and n == 10) or
                    (m == 10 and n == 4) or (m == 10 and n == 10)):
                    square.setNormal2()
                else:
                    square.setNormal()
                self.connect(square, QtCore.SIGNAL('clicked()'), self.play)
                ii = ii + 40
            i = i + 40
        print(self.board)

    def play(self):
        self.playSignal.emit(self.sender())
