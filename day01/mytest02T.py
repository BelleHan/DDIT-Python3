a = input("첫수:")
b = input("끝수:")

aa = int(a)
bb = int(b)

sum = 0
for i in range(aa,bb+1) :
    sum += i

print("sum",sum)