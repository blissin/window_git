import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from SubWindow import SubWindow
from PyQt5 import uic

# Ui_class=uic.loadUiType("mw.ui")[0]

# class MainWindow(QMainWindow, Ui_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
        
#         # self=uic.loadUi("main_window.ui",self)
#         # self.initUI()
        
#     def initUI(self):
#         self.setWindowTitle('Main Window')
#         self.setGeometry(100, 100, 300, 200)
        
#         layout = QVBoxLayout()
#         layout.addStretch(1)
        
#         label = QLabel("미지정")
#         label.setAlignment(Qt.AlignCenter)
#         font = label.font()
#         font.setPointSize(30)
#         label.setFont(font)
#         self.label = label
        
#         btn = QPushButton("값 얻어오기")
#         btn.clicked.connect(self.onButtonClicked)
        
#         layout.addWidget(label)
#         layout.addWidget(btn)
#         layout.addStretch(1)
        
#         centralWidget = QWidget()
#         centralWidget.setLayout(layout)
        
#         self.setCentralWidget(centralWidget)
        
    # def onButtonClicked(self):
    #     win = SubWindow()
    #     r = win.showModal()
    #     if r:
    #         text = win.edit.text()
    #         self.label.setText(text)
    # def show(self):
    #     super().show()

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # win = MainWindow()
    # win.show()
    # sys.exit(app.exec_())
    
    age=0
    age+=1
    age=age+1
    ++age
    print(age)

    print(type({1,2,3,4,4}))
    print("a"*2)
    0
    type(0)