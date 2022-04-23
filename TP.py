import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QComboBox
from PyQt5 import uic

class MyApp(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("TP.ui",self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())