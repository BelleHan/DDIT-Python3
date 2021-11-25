import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QIcon, QSize, QRect

form_class = uic.loadUiType("myomok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("마이 폼")
        
        for i in range(10) :
            for j in range(10) :
                obj = QPushButton(self)
                obj.setIcon(QIcon("0.png"))
                obj.setIconSize(QSize(40,40))
                obj.setGeometry(QRect(i*40, j*40, 40, 40))
        
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
    
        self.pb.setIcon(QIcon("1.png"))

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()