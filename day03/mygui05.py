import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mygui05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("마이 폼")
        
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        
        a = int(self.leA.text())
        b = int(self.leB.text())
        c = int(self.leC.text())
        sum = 0
        
        for i in range(a,b+1) :
            if i%c==0 :
                sum += i
        
        self.leD.setText(str(sum))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()