from PyQt5.QtCore import *
today=QDate.currentDate()
print(today.toString(Qt.DefaultLocaleLongDate))