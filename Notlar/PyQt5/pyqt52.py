import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500,500)
        self.move(300,300)
        self.setWindowTitle("ilk Pencere")

        self.label = QLabel("Örnek Yazı",self)
        self.label.setGeometry(10,10,200,20)
        self.text = QLineEdit("Buraya yazı yazılacak",self)
        self.text.setGeometry(10,30,200,35)
        self.dugme = QPushButton("Dugme",self)
        self.dugme.setGeometry(10,100,200,30)
        self.dugme.clicked.connect(self.tiklandi)
        
    def tiklandi(self):
        self.label.setText(self.text.text())
app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())