import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.Qt import QIcon, QSize, QRect

form_class = uic.loadUiType("myomok02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.arr2d = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],               
            ]
        self.pb2d = []
        self.flag_wb = True
        self.flag_ing = True
        self.setupUi(self)
        self.setWindowTitle("마이 폼")
        
        for i in range(19) :
            line = []
            for j in range(19) :
                obj = QPushButton(self)
                obj.setIcon(QIcon("0.png"))
                obj.setIconSize(QSize(40,40))
                obj.setGeometry(QRect(j*40, i*40, 40, 40))
                obj.clicked.connect(self.mychange)
                obj.setToolTip("{},{}".format(i,j))
                # obj.setToolTip(str(i)+","+str(j))
                line.append(obj)
            self.pb2d.append(line)
                
        self.pb.clicked.connect(self.myreset)
        
        self.myrender()
        
    def myrender(self):
        
        for i in range(19) :
            for j in range(19) :
                if self.arr2d[i][j] == 0 :
                    self.pb2d[i][j].setIcon(QIcon("0.png"))
                if self.arr2d[i][j] == 1 :
                    self.pb2d[i][j].setIcon(QIcon("1.png"))
                if self.arr2d[i][j] == 2 :
                    self.pb2d[i][j].setIcon(QIcon("2.png"))
                    
                    
    def myreset(self):
        for i in range(19) :
            for j in range(19) :
                self.arr2d[i][j] = 0
                
        self.myrender()
        
        self.flag_wb = True
        self.flag_ing = True
    
    def mychange(self):   
        if not self.flag_ing :
            return
        
        a = self.sender().toolTip()
        arr = a.split(",")
        i = int(arr[0])
        j = int(arr[1])
        
        if self.arr2d[i][j] > 0:
            return
        
        stone = -1
        if self.flag_wb :
            self.arr2d[i][j]=1
            stone = 1
        else :
            self.arr2d[i][j]=2
            stone = 2
        
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        le = self.checkLE(i,j,stone)
        ri = self.checkRI(i,j,stone)
        ul = self.checkUL(i,j,stone)
        ur = self.checkUR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.information(self, "오목", "흰돌 승리")
            else :
                QtWidgets.QMessageBox.information(self, "오목", "흑돌 승리")
                
            self.flag_ing = False
        
        self.flag_wb = not self.flag_wb
     
    def checkDR(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                i += 1
                j += 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt   
          
    def checkDL(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                i += 1
                j += -1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt     
        
    def checkUR(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                i += -1
                j += 1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt     
           
    def checkUL(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                i += -1
                j += -1
                if i < 0 or j < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt        
        
    def checkRI(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                j += 1
                if j < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt        
        
    def checkLE(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                j += -1
                if j < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt        
        
    def checkDW(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                i += 1
                if i < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt        
            
    def checkUP(self,i,j,stone): 
        cnt = 0
        try:
            while True: 
                i += -1
                if i < 0 :
                    return cnt
                if self.arr2d[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()