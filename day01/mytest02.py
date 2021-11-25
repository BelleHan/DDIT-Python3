a = input("시작수를 입력하세요")
b = input("끝수를 입력하세요")
sum = 0

if a > b : 
    for i in range(b, a+1) :
        sum += i
elif b > a : 
    for i in range(a, b+1) :
        sum += i
        
print(sum)