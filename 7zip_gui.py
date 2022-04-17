from encodings import utf_8
from lib2to3.pytree import convert
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtWidgets
import sys
import zipfile

class MyApp(QMainWindow,QDialog):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self=uic.loadUi("7zip_gui.ui",self)
        self.color=0
        self.show()
        
    #라디오 클릭 티리거로 csv 불러오기 refresh
    def rad_grey(self):
        self.color = 0
        print('grey')
        pass
    
    def rad_color(self):
        self.color =1
        print('color')
        pass

    def start(self):
        # self.label_status.setText("start")
        QMessageBox.about(self, "message", "clicked")
        pass
    
    def stop(self):
        # self.label_status.setText("stop")
        # close로 변경
        pass
    
    def clear(self):
        self.textEdit_contents.clear()
        pass

    #파일 불러오기
    def read_csv(self) :
        f_name=QFileDialog.getOpenFileName(self, 'Open file','./', 'All File(*);;CSV(*.csv);;압축파일(*.zip)')
        self.label_filename.setText(f_name[0])
        if f_name[0]:
            pixmap=QPixmap(f_name[0])
            self.label_image.setPixmap(pixmap)
            # f=open(f_name[0],'r', encoding='UTF-8')
            # with f:
            #     data=f.read()
            #     self.textEdit_contents.setText(data)
  
    # #파일 내용 자체 display
    # def slot_fileopen(self):
    #     fname=QFileDialog.getOpenFileName(self, 'Open file','./')
    #     print(type(fname),fname)
    #     self.label_filename.setText(fname[0])
    #     if fname[0]:
    #         f=open(fname[0],'r', encoding='UTF-8')
    #         with f:
    #             data=f.read()
    #             self.textEdit_contents.setText(data)

        
if __name__ == '__main__':
    #qtdesigner UI 실행
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

