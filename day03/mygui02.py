import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mygui02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("마이 폼")
        
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
       
        a = self.le.text()
        aa = int(a)
        aa += 1
        self.le.setText(str(aa))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()