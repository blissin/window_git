<<<<<<< HEAD
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
=======
from PIL import Image
ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    # print(pixels_in_image)
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print( "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
        print (e)
        return

    image_ascii = convert_image_to_ascii(image)
    print (image_ascii)

if __name__=='__main__':
    import sys

    image_file_path = "IMAGE/IU.jpg"
    handle_image_conversion(image_file_path)
>>>>>>> 0fa47932c3cfd629990aef7fa08846acb9bd4ebc
