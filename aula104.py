from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QGridLayout, QWidget
import sys
#modulos diferentes pra esse programa
from PyQt5.QtWidgets import QSizePolicy, QLineEdit
from PyQt5.QtGui import QIcon


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora de Jeffinho")
        self.setWindowIcon(QIcon('calculator_icon-icons.com_54044.ico'))
        self.setFixedSize(400,400)
        self.qw = QWidget()
        self.qgl = QGridLayout(self.qw)


        #coisas relacionadas ao display
        self.display = QLineEdit()
        self.display.setDisabled(True)
        self.display.setStyleSheet("* {background: White; color: #000; font-size: 30px;}")
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


        self.qgl.addWidget(self.display, 0, 0, 1, 5)

        #adicionando butões
        self.add_buton(QPushButton("7"), 1,0,1,1)
        self.add_buton(QPushButton("8"), 1,1,1,1)
        self.add_buton(QPushButton("9"), 1,2,1,1)
        self.add_buton(QPushButton("<--"), 1,3,1,1, lambda: self.display.setText(self.display.text()[:-1]), "background: #fc8803; color: #fff; font-weight: 700;")
        self.add_buton(QPushButton("C"), 1,4,1,1, lambda: self.display.setText(""),  "background: #fc0303; color: #fff; font-weight: 700;")


        self.add_buton(QPushButton("4"), 2,0,1,1)
        self.add_buton(QPushButton("5"), 2,1,1,1)
        self.add_buton(QPushButton("6"), 2,2,1,1)
        self.add_buton(QPushButton("+"), 2,3,1,1)
        self.add_buton(QPushButton("-"), 2,4,1,1)


        self.add_buton(QPushButton("1"), 3, 0, 1, 1)
        self.add_buton(QPushButton("2"), 3, 1, 1, 1)
        self.add_buton(QPushButton("3"), 3, 2, 1, 1)
        self.add_buton(QPushButton("*"), 3, 3, 1, 1)
        self.add_buton(QPushButton("/"), 3, 4, 1, 1)


        self.add_buton(QPushButton("S2"), 4, 0, 1, 1, lambda: self.display.setText("Você é lindi!"), "color: #f542f5; font-wight: 700; font-size: 20px;")
        self.add_buton(QPushButton("0"), 4, 1, 1, 1)
        self.add_buton(QPushButton("."), 4, 2, 1, 1)
        self.add_buton(QPushButton("^"), 4, 3, 1, 1)
        self.add_buton(QPushButton("="), 4, 4, 1, 1, self.eval_igual, style='background: #0362fc; color: #fff; font-weight: 700;')

        #setando o grid no app
        self.setCentralWidget(self.qw)


    def add_buton(self, button, linha, coluna, ocupa_linha, ocupa_coluna, funcao=None, style=None):
        self.qgl.addWidget(button, linha, coluna, ocupa_linha, ocupa_coluna)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        if style:
            button.setStyleSheet(style)
        if funcao == None:
            button.clicked.connect(lambda: self.display.setText(self.display.text() + button.text()))
        else:
            button.clicked.connect(funcao)


    def eval_igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText("Calculo Invalidi")



if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    qt.exec_()