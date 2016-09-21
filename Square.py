from PyQt4 import QtGui, QtCore
import os

class Square(QtGui.QLabel):

    def __init__(self, parent, m, n):
        QtGui.QLabel.__init__(self, parent)
        self.name = 'Square[' + str(m) + '][' + str(n) + ']'
        self.m = m
        self.n = n

    def __repr__(self):
        return self.name

    ''' Sobrescrevendo função do QtGui.QLabel'''
    def mouseReleaseEvent(self, ev):
        self.emit(QtCore.SIGNAL('clicked()'))

    def getCoord(self):
        return self.m, self.n

    def setNormal(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/BoardSquareNormal.png"))

    def setNormal2(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/BoardSquareNormal2.png"))

    def setPlayer1(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/BoardSquareP1.png"))

    def setPlayer2(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/BoardSquareP2.png"))
