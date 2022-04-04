import sys
from PyQt5.QtWidgets import *# QApplication, QWidget, QPushButton, QMainWindow, qApp, QAction, QDesktopWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import * #QCoreApplication, QDate, Qt
from PyQt5.QtGui import QIcon


#https://codetorial.net/pyqt5/basics/statusbar.html

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        self.initUI()

    
    def initUI(self):
        #위치, 사이즈
        self.setGeometry(300,300,400,400) # self.move() + self.resize()
        self.center() #center method
        #이름, 아이콘
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('다운로드.png'))
      
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q') #단축키로도 실행되게 설정
        exitAction.setStatusTip('Exit') #하단 메뉴바에 표시
        exitAction.triggered.connect(qApp.quit) #트리거        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        self.statusBar()

        #시간, 계속 표시하는 법 필요
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)+" "+self.time.toString(Qt.DefaultLocaleLongDate))
    

 
    def center(self):
        self.show()
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())