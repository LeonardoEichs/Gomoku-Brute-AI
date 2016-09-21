import sys
from PyQt4 import QtGui, QtCore
import BoardFrame

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)

        self.windowBoard = BoardFrame.BoardFrame(self)
        self.setCentralWidget(self.windowBoard)

        self.setWindowTitle('Gomoku')
        self.resize(600, 600)
        self.center()

        self.show()

    def center(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)
