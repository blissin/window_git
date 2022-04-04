import sys
from PyQt5.QtWidgets import * # QApplication, QMainWindow
from PyQt5.QtCore import * #QDate, Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        #box layout
        # okButton = QPushButton('OK',self)
        # cancelButton = QPushButton('Cancel',self)   

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)
        # hbox.addStretch(1)

        # vbox = QVBoxLayout()
        # vbox.addStretch(3)
        # vbox.addLayout(hbox)
        # vbox.addStretch(1)

        # self.setLayout(vbox)
        '''
        #grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(30, 30) #absolute layout
        btn.resize(btn.sizeHint()) #적당한 크기로?
        btn.clicked.connect(QCoreApplication.instance().quit)
        # Quit 버튼
        self.setWindowTitle('QWidget')
        self.setGeometry(300, 300, 400, 200)
        self.show()        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())