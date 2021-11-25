from random import random

com = ""
mine = ""
result = ""

mine = input("홀/짝을 입력하시오..")

rnd = random()
if rnd > 0.5 :
    com = "홀"
else :
    com = "짝"
    
if com == mine : 
    result = "이김"
else :
    result = "짐"
    
print("com",com)
print("mine",mine)
print("result",result)
