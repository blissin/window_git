import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO")
        self.setGeometry(300,300,300,300)

        btn1=QPushButton("click me",self)
        btn1.move(20,20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self,"mesage","clicked")

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mywindow=Mywindow()
    mywindow.show()
    app.exec_()