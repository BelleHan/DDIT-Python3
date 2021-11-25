import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.Compiler.qtproxies import QtWidgets

form_class = uic.loadUiType("mygui09.ui")[0]

class MyWindow(QMainWindow, form_class):
    num = ""
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("마이 폼")
        
        self.pb1.clicked.connect(self.myclick1)
        self.pb2.clicked.connect(self.myclick2)
        self.pb3.clicked.connect(self.myclick3)
        self.pb4.clicked.connect(self.myclick4)
        self.pb5.clicked.connect(self.myclick5)
        self.pb6.clicked.connect(self.myclick6)
        self.pb7.clicked.connect(self.myclick7)
        self.pb8.clicked.connect(self.myclick8)
        self.pb9.clicked.connect(self.myclick9)
        self.pb0.clicked.connect(self.myclick0)
        self.pbCall.clicked.connect(self.myclickCall)

    def myclick1(self):        
        self.num += self.pb1.text()
        self.le.setText(self.num)
        
        btn = str(self.sender())
        print(btn)

    def myclick2(self):        
        self.num += self.pb2.text()
        self.le.setText(self.num)

    def myclick3(self):        
        self.num += self.pb3.text()
        self.le.setText(self.num)

    def myclick4(self):        
        self.num += self.pb4.text()
        self.le.setText(self.num)

    def myclick5(self):        
        self.num += self.pb5.text()
        self.le.setText(self.num)

    def myclick6(self):        
        self.num += self.pb6.text()
        self.le.setText(self.num)

    def myclick7(self):        
        self.num += self.pb7.text()
        self.le.setText(self.num)

    def myclick8(self):        
        self.num += self.pb8.text()
        self.le.setText(self.num)

    def myclick9(self):        
        self.num += self.pb9.text()
        self.le.setText(self.num)

    def myclick0(self):        
        self.num += self.pb0.text()
        self.le.setText(self.num)
        
    def myclickCall(self):     
           
        QMessageBox.information(self, "calling", self.num)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()