import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("mygui07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("마이 폼")
        
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        
        dan = self.le.text()
        text = ""
        text += "{}*{}={}\n".format(dan,1,int(dan)*1)
        text += "{}*{}={}\n".format(dan,2,int(dan)*2)
        text += "{}*{}={}\n".format(dan,3,int(dan)*3)
        text += "{}*{}={}\n".format(dan,4,int(dan)*4)
        text += "{}*{}={}\n".format(dan,5,int(dan)*5)
        text += "{}*{}={}\n".format(dan,6,int(dan)*6)
        text += "{}*{}={}\n".format(dan,7,int(dan)*7)
        text += "{}*{}={}\n".format(dan,8,int(dan)*8)
        text += "{}*{}={}\n".format(dan,9,int(dan)*9)
        
        self.te.setText(text)
              
        # res = ""
        #
        # for i in range(1,10) :
        #
        #     res += dan + " * " + str(i) + " = " + str(int(dan)*i) + "\n"
        #
        # self.te.setText(res)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()