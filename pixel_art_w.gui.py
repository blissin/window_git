from encodings import utf_8
from lib2to3.pytree import convert
from PIL import Image
from colorama import init, Fore
import colorsys
import sys, os
import numpy as np
import pandas as pd
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtWidgets

import im2excel


#도트 아트 그리는 순서.. grey scale로 바꿔서 숫자로 하나씩 표현
fill = ["⠈","⠋","⡿","⣄","⡉","⠉","⠻","⣴","⣷","⣧","⣿"]
#"⠫","⠬","⠭","⠮","⠰","⠱","⠲","⠳","⠴","⠵","⠶","⠁","⠂","⠃","⠄","⠅","⠆","⠇","⠈","⠉","⠊","⠋","⠌","⠍","⠎","⠏","⠐","⠑","⠒","⠓","⠔","⠕","⠖","⠗","⠘","⠙","⠚","⠛","⠜","⠝","⠞","⠠","⠡","⠢","⠣","⠤","⠥","⠦","⠧","⠨","⠩","⠪"

# 그림 그리기 class
class converter():
    def __init__(self, dir):
        self.dir = dir
        self.size = (50, 50)
        init(autoreset=True)

    def create_gray(self):
        try:
            with Image.open(self.dir) as img: #파일 열었다가 끝나면 자동 닫기
                if img.mode != "L":
                    img = img.convert("L") # image convert to grey scale

                # 이미지를 size에 맞게 축소 (썸네일)
                img.thumbnail(self.size)

                # 이미지의 모든 픽셀 정보 로드
                pixels = img.load()
                # print(pixels)

                # 이미지의 폭, 높이 가져오기
                width, height = img.size
                a=[]
                # 1픽셀씩 반복하며 출력
                for h in range(height):
                    for w in range(width):
                        print(self.get_ascii(pixels[w, h]), end="")
                        a.append(self.get_ascii(pixels[w, h])) #코드 하나씩 list에 추가
                    # 개행
                    print()

                #코드 array -> reshape -> pandas -> csv
                data=np.array(a)
                data=data.reshape(h+1,w+1)
                data=pd.DataFrame(data)
                data.to_csv('temp.csv',encoding='UTF-8',index=False,header=None,sep=' ')
                '''
                with open('temp.csv','w',encoding='UTF-8') as file:
                    write=csv.writer(file)
                    write.writerow(a)
                '''    
        except Exception as e:
            print("작업 중 오류가 발생하였습니다:", e)

    # 0 ~ 255 사이의 값을 받은 후 0 ~ 9 범위로 변환 // 좀더 해상도 높이는 법? 순서대로 말고 
    def get_ascii(self, value):
        return fill[int(value / 25)]  #fill : array 채우기

    def create_color(self):
        # TODO: 색상 추출
        try:
            with Image.open(self.dir) as img:
                
                # 이미지 모드가 RGB가 아닌 경우 RGB 모드로 변환
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # 이미지를 size에 맞게 축소 (썸네일)
                img.thumbnail(self.size)

                # 이미지의 모든 픽셀 정보 로드
                pixels = img.load()

                # 이미지의 폭, 높이 가져오기
                width, height = img.size
                a=[]
                # 1픽셀씩 반복하며 출력
                for h in range(height):
                    for w in range(width):
                        print(self.get_color_ascii(pixels[w, h]), end="")
                        a.append(self.get_color_ascii(pixels[w, h])) #코드 하나씩 list에 추가
                    # 개행
                    print()
                
                data=np.array(a)
                data=data.reshape(h+1,w+1)
                data=pd.DataFrame(data)
                data.to_csv('temp.csv',encoding='UTF-8',index=False,header=None)
                # csv 저장한걸 불러오기보단 print 구문 자체를 표현하는게 어떨지?
                # 색깔을 csv에 저장하기..?

        except Exception as e:
            print("작업 중 오류가 발생하였습니다:", e)

    def get_color_ascii(self, rgb):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        # rgb 색상 데이터를 모두 더한다
        pixel_values = r + g + b

        # 모두 더한 색상 데이터를 범위 10으로 제한 (765 -> 10)
        c = fill[int(pixel_values / 76.5) - 1] * 2

        # 기본 색상은 리셋
        color = Fore.RESET

        # rgb 색상 데이터를 hsv로 변환
        # 변환할 rgb 데이터의 범위는 0 ~ 1 이어야 함
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        # h에 따른 색상
        if h >= 0 and h <= 0.07: # 0 ~ 30
            color = Fore.RED
        elif h > 0.07 and h <= 0.20: # 31 ~ 70
            color = Fore.YELLOW
        elif h > 0.20 and h <= 0.45: # 71 ~ 160
            color = Fore.GREEN
        elif h > 0.45 and h <= 0.55: # 161 ~ 200
            color = Fore.CYAN
        elif h > 0.55 and h <= 0.72: # 201 ~ 260
            color = Fore.BLUE
        elif h > 0.72 and h <= 0.92: # 261 ~ 330
            color = Fore.MAGENTA
        else:
            color = Fore.RED

        # v, s에 따라 검정, 흰색으로 변경
        if v >= 0.7 and s <= 0.25:
            color = Fore.WHITE

        if v <= 0.25:
            color = Fore.BLACK
        
        # 색상과 출력할 문자를 합쳐서 전달
        return color + c

class MyApp(QMainWindow,QDialog):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self=uic.loadUi("UI/app2.ui",self)
        self.color=0
        self.output_type=0
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

    '''
    #파일 내용 자체 display
    def slot_fileopen(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file','./')
        print(type(fname),fname)
        self.label_filename.setText(fname[0])
        if fname[0]:
            f=open(fname[0],'r', encoding='UTF-8')
            with f:
                data=f.read()
                self.textEdit_contents.setText(data)
    '''
    def img2ascii(self):
        self.output_type=1
    def img2xls(self):
        self.output_type=0

    #img 파일 불러오기
    def loadImageFromFile(self) :
        f_name=QFileDialog.getOpenFileName(self, 'Open file','./', 'All File(*);;Image File(*.png *jpg *jpeg)')
        self.label_filename.setText(f_name[0])
        # print(type(f_name[0]))
        file_name=f_name[0].split('/')[-1]
        file_type=file_name.split('.')[-1]
        if self.output_type==1:
            if f_name[0]:
                pixmap=QPixmap(f_name[0])
                self.label_image.setPixmap(pixmap)
                c=converter(f_name[0])
                
                # 함수내 그리기 호출
                if self.color==0:
                    c.create_gray() 
                else:
                    c.create_color()
            
                f=open("temp.csv",'r', encoding='UTF-8')
                np.data=f.read()
                self.textEdit_contents.setText(np.data)
                ## csv형식 말고 다른걸로 불러오는거 생각해보기 ,가 같이 불러와짐..
        elif self.output_type==0:
            img_xls=im2excel.cv2xls()
            img_xls.img_2_xls(f_name[0])

# img_xls=im2excel.cv2xls()
# img_xls.img_2_xls('')

        
if __name__ == '__main__':
    #qtdesigner UI 실행
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


'''
# 모드 입력 확인
mode_check = False
try:
    # 이미지 경로
    img_dir = sys.argv[1]
except:
    print("이미지 경로를 찾을 수 없습니다.")
    exit()

try:
    # 실행 모드
    mode = sys.argv[2].lower()
    mode_check = True
except:
    pass

if os.path.isfile(img_dir):
    c = converter(img_dir)

    if mode_check:
        if mode == "-grey":
            c.create_gray()
        elif mode == "-color":
            c.create_color()
        else:
            print("알 수 없는 모드입니다. {}".format(mode))
    else:
        # 모드를 입력하지 않았으면 흑백모드로 진행
        c.create_gray()
        
else:
    print("{} 파일이 없습니다.".format(img_dir))
'''

#test
