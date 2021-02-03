import random
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow


class YellowCircleParam:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.c = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class YellowCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('ui.ui', self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_click)
        self.circles = []
        self.max_d = 99

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        for i in self.circles:
            qp.setBrush(i.c)
            qp.drawEllipse(i.x, i.y, i.d, i.d)

    def button_click(self):
        self.circles = []
        for i in range(random.randint(2, 11)):
            self.circles.append(YellowCircleParam(random.randint(0, self.width() - self.max_d),
                                                  random.randint(0, self.height() - self.max_d),
                                                  random.randint(10, self.max_d)))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())
