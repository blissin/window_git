import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

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
        
    def graph1(self):
    	#x_list, y_list, y_err, data_name에 대한 설정 코드 
        self.x_list=[1,2,3]
        self.y_list=[1,2,3]
    	# self.graph_viewer.canvas.axes.plot(self.x_list, self.y_list)
        #https://arumyworld.tistory.com/12
        self.graph_viewer.canvas.axes.legend()
        self.graph_viewer.canvas.axes.set_xlabel('~~~')
        self.graph_viewer.canvas.axes.set_ylabel('~~~')
        self.graph_viewer.canvas.draw() 




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())