import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        uic.loadUi("arayuz.ui", self)
        self.bt1.clicked.connect(self.tiklandi)
        self.show()

    def tiklandi(self):
        self.lab1.setText(self.text1.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec_())