import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
from Selenium1 import InstaBotCore


class Uygulama(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("UI", "AnaMenu.ui"), self)
        self.Goster()

    def Goster(self):
        self.btTarayici.clicked.connect(self.git)
        self.btTakip.clicked.connect(self.Takip)
        self.btBirak.clicked.connect(self.TakipBirak)
        self.btLike.clicked.connect(self.Likela)
        self.btTakipciList.clicked.connect(self.Takipci)
        self.show()

    def Takipci(self):
        self.selinsBot.TakipciListeAl(self.txtTakip.text(), 100)

    def Likela(self):
        self.selinsBot.ilkFotoLike(self.txtTakip.text())

    def TakipBirak(self):
        self.selinsBot.TakipBirak(self.txtTakip.text())

    def Takip(self):
        self.selinsBot.TakipEt(self.txtTakip.text())

    def first_picture(self):
        self.selinsBot.likefoto()

    def git(self):
        self.selinsBot = InstaBotCore(self.txtUser.text(), self.txtPass.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Uygulama()
    sys.exit(app.exec_())
