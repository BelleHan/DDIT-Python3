import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("mygui08.ui")[0]

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
        com = ""
        result = ""
        
        rnd = random()
        
        
        if rnd > 0.66 :
            com = "가위"
        elif rnd > 0.33 :
            com = "바위"
        else : 
            com = "보"
            
        if mine == com :
            result = "비김"
        else :    
            if com == "가위" :
                if mine == "바위" :
                    result = "이김"
                elif mine == "보" :
                    result = "짐"
            elif com == "바위" :
                if mine == "가위" :
                    result = "짐"
                elif mine == "보" :
                    result = "이김"
            else :
                if mine == "가위" :
                    result = "이김"
                elif mine == "바위" :
                    result = "짐"
                    
        self.leCom.setText(com)
        self.leResult.setText(result)           
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()