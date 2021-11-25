import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("mygui06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("마이 폼")
        
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myenter)

    def myenter(self):
        self.gamestart() 

    def myclick(self):
       self.gamestart() 
       
    def gamestart(self): 
        
        mine = self.leMine.text()
        
        rnd = random()
        
        if rnd > 0.5 :
            self.leCom.setText("홀")
        else : 
            self.leCom.setText("짝")
            
        if mine == self.leCom.text() :
            self.leResult.setText("이김")
        else :
            self.leResult.setText("짐")
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()