from PyQt4 import QtGui
import sys
import Window

class Game(object):

    def __init__(self):
        self.player = 1
        self.aiPieces = {}
        self.playerPieces = {}
        self.emptySpaces = {}

    def startGame(self):
        app = QtGui.QApplication(sys.argv)
        self.window = Window.Window()
        self.window.windowBoard.playSignal.connect(self.play)
        sys.exit(app.exec_())

    def play(self, sender):
        win = 0
        if self.player == 1:
            if(self.window.windowBoard[sender.m][sender.n] == 0):
                win = self.window.windowBoard.board.alterBoard(sender.m, sender.n, self.player)
                sender.setPlayer1()
                self.checkWin(win)
                self.playerPieces[sender] = {}
                for playerPiece in self.playerPieces:
                    self.playerPieces[playerPiece] = self.window.windowBoard.board.evaluate(playerPiece.m, playerPiece.n, 1)
                for aiPiece in self.aiPieces:
                    self.aiPieces[aiPiece] = self.window.windowBoard.board.evaluate(aiPiece.m, aiPiece.n, 2)
                # for piece in self.window.windowBoard.squares.values():
                #     self.emptySpaces[piece] = {}
                #     self.emptySpaces[piece] = self.window.windowBoard.board.evaluate(piece.m, piece.n, 2)
                self.changePlayer()
                win = self.AIplay()
        self.checkWin(win)
        self.changePlayer()


    def AIplay(self):
        def direita():
            i = 1
            while(self.window.windowBoard.board[playData[0].m][playData[0].n + i] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m)+","+str(playData[0].n+i)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m)+","+str(playData[0].n+i)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m, playData[0].n + i, self.player)
            return win
        def esquerda():
            i = 1
            while(self.window.windowBoard.board[playData[0].m][playData[0].n - i] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m)+","+str(playData[0].n-i)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m)+","+str(playData[0].n-i)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m, playData[0].n - i, self.player)
            return win
        def cima():
            i = 1
            while(self.window.windowBoard.board[playData[0].m - i][playData[0].n] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m-i)+","+str(playData[0].n)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m-i)+","+str(playData[0].n)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m - i, playData[0].n, self.player)
            return win
        def baixo():
            i = 1
            while(self.window.windowBoard.board[playData[0].m + i][playData[0].n] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m+i)+","+str(playData[0].n)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m+i)+","+str(playData[0].n)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m + i, playData[0].n, self.player)
            return win
        def diagonalCE():
            i = 1
            while(self.window.windowBoard.board[playData[0].m - i][playData[0].n - i] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m-i)+","+str(playData[0].n-i)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m-i)+","+str(playData[0].n-i)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m - i, playData[0].n - i, self.player)
            return win
        def diagonalBE():
            i = 1
            while(self.window.windowBoard.board[playData[0].m + i][playData[0].n - i] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m + i)+","+str(playData[0].n-i)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m + i)+","+str(playData[0].n-i)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m + i, playData[0].n - i, self.player)
            return win
        def diagonalCD():
            i = 1
            while(self.window.windowBoard.board[playData[0].m - i][playData[0].n + i] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m - i)+","+str(playData[0].n+i)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m - i)+","+str(playData[0].n+i)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m - i, playData[0].n + i, self.player)
            return win
        def diagonalBD():
            i = 1
            while(self.window.windowBoard.board[playData[0].m + i][playData[0].n + i] != 0):
                i += 1
            self.window.windowBoard.squares[str(playData[0].m + i)+","+str(playData[0].n+i)].setPlayer2()
            self.aiPieces[self.window.windowBoard.squares[str(playData[0].m + i)+","+str(playData[0].n+i)]] = {}
            win = self.window.windowBoard.board.alterBoard(playData[0].m + i, playData[0].n + i, self.player)
            return win

        playData = [None, None, 0]
        for piece in self.aiPieces:
            for strategy in self.aiPieces[piece].keys():
                if (self.aiPieces[piece][strategy] > playData[2]):
                    playData[0] = piece
                    playData[1] = strategy
                    playData[2] = self.aiPieces[piece][strategy]
        for piece in self.playerPieces:
            for strategy in self.playerPieces[piece].keys():
                if (self.playerPieces[piece][strategy] > playData[2]):
                    playData[0] = piece
                    playData[1] = strategy
                    playData[2] = self.playerPieces[piece][strategy]
        print(playData)
        if(playData[1] == "Direita"):
            win = direita()
        elif(playData[1] == "Esquerda"):
            win = esquerda()
        elif(playData[1] == "Cima"):
            win = cima()
        elif(playData[1] == "Baixo"):
            win = baixo()
        elif(playData[1] == "DiagonalCE"):
            win = diagonalCE()
        elif(playData[1] == "DiagonalBE"):
            win = diagonalBE()
        elif(playData[1] == "DiagonalCD"):
            win = diagonalCD()
        elif(playData[1] == "DiagonalBD"):
            win = diagonalBD()
        return win

    def changePlayer(self):
        if (self.player == 1):
            self.player = 2
        else:
            self.player = 1

    def checkWin(self, win):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)

        if win == 'w':

            msg.setText("Vencedor:  " + str(self.player) + "    ")
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()
        if win == 'd':
            msg.setText("Empate")
            msg.setWindowTitle("Fim de Jogo")
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(QtGui.qApp.quit)
            msg.exec_()

def main():
    Game().startGame()

if __name__ == "__main__":
    main()
