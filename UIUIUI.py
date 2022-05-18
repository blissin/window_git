import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit

from PyQt5 import uic

form_class = uic.loadUiType("UI\\mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout) # 1초 주기로 timeout 메소드 호출
        #Object.event.connect?
        
    def inquiry(self):
        self.lineEdit_current.setText(str("가즈아"))    

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        cur_date=QDate.currentDate()
        str_date=cur_date.toString(Qt.DefaultLocaleLongDate)
        self.statusBar().showMessage(str_date+" "+str_time)
        price = pyupbit.get_current_price("KRW-BTC")
        self.lineEdit_current.setText(str(price))

if __name__ == "__main__":
    app=QApplication(sys.argv) # QApplication 객체 생성
    window=MyWindow()
    window.show()
    app.exec_()                # 이벤트 루프 생성
    
    
    #https://wikidocs.net/21875