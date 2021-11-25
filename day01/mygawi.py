from random import random
com = ""
mine = ""
result = ""

mine = input("가위바위보 중 입력하시오")

rnd = random() * 3
if rnd > 2 :
    com = "가위"
elif rnd > 1 :
    com = "바위"
else :
    com = "보"
    
if com == mine :
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
            
print("com",com)
print("mine",mine)
print("result",result)
        

