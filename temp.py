import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from PyQt5 import uic
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("TP.ui",self)
        self.show()
    
    def open(self):
        f_name=QFileDialog.getOpenFileName(self, 'Open file','./', 'All File(*);;압축파일(*.zip)')
        self.label_filename.setText(f_name[0])
    
    def close(self):
        sys.exit(app.exec_())

    def initUI(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

    def graph1(self):
        self.x_list = np.arange(0, 10, 0.5)
        self.y_list = np.sin(self.x_list)
        self.graph_viewer.canvas.axes.plt(self.x_list, self.y_list)
        self.graph_viewer.canvas.axes.legend()
        self.graph_viewer.canvas.axes.set_xlabel('~~~')
        self.graph_viewer.canvas.axes.set_ylabel('~~~')
        self.graph_viewer.canvas.draw() 
        # x = np.arange(0, 10, 0.5)
        # y1 = np.sin(x)
        # y2 = np.cos(x)
        
        # self.fig.clear()
        # ax = self.fig.add_subplot(111)
        # ax.plot(x, y1, label="sin(x)")
        # ax.plot(x, y2, label="cos(x)", linestyle="--")
        
        # ax.set_xlabel("x")
        # ax.set_xlabel("y")
        
        # ax.set_title("sin & cos")
        # ax.legend()
        
        # self.canvas.draw()

        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()