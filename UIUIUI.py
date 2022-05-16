import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("UI\\mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.btn_clicked) #Object.event.connect?
        
    def btn_clicked(self):
        print('clicked')


if __name__ == "__main__":
    app=QApplication(sys.argv) # QApplication 객체 생성
    window=MyWindow()
    window.show()
    app.exec_()                # 이벤트 루프 생성
    
    
    #https://wikidocs.net/21875