WIN = 'w'
DRAW = 'd'
CONTINUE = 'c'

class Board():
    BoardWidth = 15
    BoardHeight = 15

    def __init__(self):
        self.board = [[0 for i in range(self.BoardWidth)] for ii in range(self.BoardHeight)]
        self.pieces = 0

    def __repr__(self):
        board = ''
        for i in range(self.BoardHeight):
            board = board + str(self.board[i]) + '\n'
        return board

    def __getitem__(self, key):
        return self.board[key]

    def alterBoard(self, m, n, player):
        self[m][n] = player
        win = self.checkWin(m, n, player)
        print(self)
        return win

    def checkWin(self, m, n, player):

        count = 1
        self.pieces = self.pieces + 1
        if (self.pieces == 15 * 15):
            return DRAW

        # Vencendo pela diagonal baixo direita
        for i in range(1, 5):
            if (m - i >= 0 and n - i >= 0 and self.board[m - i][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela diagonal cima direita
        for i in range(1, 5):
            if (m + i <= 14 and n - i >= 0 and self.board[m + i][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo pela diagonal baixo esquerda
        for i in range(1, 5):
            if (m - i >= 0 and n + i <= 14 and self.board[m - i][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela diagonal cima esquerda
        for i in range(1, 5):
            if (m + i <= 14 and n + i <= 14 and self.board[m + i][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo pela esquerda
        for i in range(1, 5):
            if (n + i <= 14 and self.board[m][n + i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo pela direita
        for i in range(1, 5):
            if (n - i >= 0 and self.board[m][n - i] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        # Vencendo por Cima
        for i in range(1, 5):
            if (m + i <= 14 and self.board[m + i][n] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN

        # Vencendo por Baixo
        for i in range(1, 5):
            if (m - i >= 0 and self.board[m - i][n] == player):
                count = count + 1
            else:
                break
        if (count == 5):
            return WIN
        else:
            count = 1

        return CONTINUE

    def evaluate(self, m, n, player):

        points = {}
        count = 0

        # Vencendo pela diagonal baixo direita
        for i in range(1, 5):
            if (m - i >= 0 and n - i >= 0 and self.board[m - i][n - i] == player):
                count = count + 10
            elif (m - i >= 0 and n - i >= 0 and self.board[m - i][n - i] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["DiagonalCE"] = count
        count = 0

        # Vencendo pela diagonal cima direita
        for i in range(1, 5):
            if (m + i <= 14 and n - i >= 0 and self.board[m + i][n - i] == player):
                count = count + 10
            elif (m + i <= 14 and n - i >= 0 and self.board[m + i][n - i] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["DiagonalBE"] = count
        count = 0

        # Vencendo pela diagonal baixo esquerda
        for i in range(1, 5):
            if (m - i >= 0 and n + i <= 14 and self.board[m - i][n + i] == player):
                count = count + 10
            elif (m - i >= 0 and n + i <= 14 and self.board[m - i][n + i] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["DiagonalCD"] = count
        count = 0

        # Vencendo pela diagonal cima esquerda
        for i in range(1, 5):
            if (m + i <= 14 and n + i <= 14 and self.board[m + i][n + i] == player):
                count = count + 10
            elif (m + i <= 14 and n + i <= 14 and self.board[m + i][n + i] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["DiagonalBD"] = count
        count = 0

        # Vencendo pela esquerda
        for i in range(1, 5):
            if (n + i <= 14 and self.board[m][n + i] == player):
                count = count + 10
            elif (n + i <= 14 and self.board[m][n + i] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["Direita"] = count
        count = 0

        # Vencendo pela direita
        for i in range(1, 5):
            if (n - i >= 0 and self.board[m][n - i] == player):
                count = count + 10
            elif (n - i >= 0 and self.board[m][n - i] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["Esquerda"] = count
        count = 0

        # Vencendo por Cima
        for i in range(1, 5):
            if (m + i <= 14 and self.board[m + i][n] == player):
                count = count + 10
            elif (m + i <= 14 and self.board[m + i][n] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["Baixo"] = count
        count = 0

        # Vencendo por Baixo
        for i in range(1, 5):
            if (m - i >= 0 and self.board[m - i][n] == player):
                count = count + 10
            elif (m - i >= 0 and self.board[m - i][n] == 0):
                count = count + 5
            else:
                count = 0
                break
        points["Cima"] = count
        count = 0

        return points
