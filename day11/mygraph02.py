import numpy as np
import matplotlib.pyplot as plt         


fig = plt.figure(1) 
graph = fig.add_subplot(111,projection = '3d')

x = [0,0,0,0,0,0,0,0,0,0]
x2 = [1,1,1,1,1,1,1,1,1,1]
x3 = [2,2,2,2,2,2,2,2,2,2]
y = [0,1,2,3,4,5,6,7,8,9]
z = [10,10,9,10,10,10,10,9,10,10]
z2 = [10,10,11,10,10,10,10,11,10,10]
z3 = [7,7,7,7,7,7,7,7,7,7]
graph.plot(x,y,z)
graph.plot(x2,y,z2)
graph.plot(x3,y,z3)


plt.show()