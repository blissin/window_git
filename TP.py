import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyApp(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("TP.ui",self)
        self.show()
    
    def open(self):
        f_name=QFileDialog.getOpenFileName(self, 'Open file','./', 'All File(*);;압축파일(*.zip)')
        self.label_filename.setText(f_name[0])
    
    def close(self):
        sys.exit(app.exec_())
        
    def graph(self):
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())