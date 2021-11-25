import numpy as np
import matplotlib.pyplot as plt         


fig = plt.figure(1) 
graph = fig.add_subplot(111,projection = '3d')

x = np.zeros(10)
y = range(10)
zs = []

zs.append([10,10,9,10,10,10,10,9,10,10])
zs.append([10,10,11,10,10,10,10,11,10,10])
zs.append([7,7,7,7,7,7,7,7,7,7])

graph.plot(x+0,y,zs[0])
graph.plot(x+1,y,zs[1])
graph.plot(x+2,y,zs[2])


plt.show()