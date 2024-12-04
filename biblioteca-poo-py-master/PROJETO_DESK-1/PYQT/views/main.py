import sys
from PyQt6 import uic
from PyQt6.Qtwidgets import QApplication, QMainWindow

ui_file = "main.ui"
class MainWindown(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUI(ui_file, self)
        self.botaoTeste.clicked.connect(self.clicked)

    def clicked(self):
        txt_user = self.inputnome
        txt_senha = self.inputsenha
        btn_cadastrar = self.    