import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


form_class = uic.loadUiType("canvas.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_graph(self):
    	#x_list, y_list, y_err, data_name에 대한 설정 코드 
        self.x_list=[1,2,3]
        self.y_list=[1,2,3]
    	# self.graph_viewer.canvas.axes.plot(self.x_list, self.y_list)
        self.graph_viewer.canvas.axes.legend()
        self.graph_viewer.canvas.axes.set_xlabel('~~~')
        self.graph_viewer.canvas.axes.set_ylabel('~~~')
        self.graph_viewer.canvas.draw() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()    