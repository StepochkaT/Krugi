import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.flag = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        for _ in range(randint(1, 10)):
            R = randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(QPointF(randint(100, 800), randint(150, 800)), R, R)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())


