import numpy as np
import matplotlib.pyplot as plt         # matplotlib 라이브러리를 선언.

# z = [10,10,9,10,10 ,10,10,9,10,10]
#
# x_axis = np.arange(1,10)
# y_axis = np.arange(1,10)
# z_axis = np.arange(1,10)

x_axis = [0,0,0,0,0,0,0,0,0,0]
y_axis = [0,1,2,3,4,5,6,7,8,9]
z_axis = [10,10,9,10,10,10,10,9,10,10]

fig = plt.figure(1)  
graph = fig.add_subplot(111,projection = '3d')

graph.plot(x_axis,y_axis,z_axis, 'r')
graph.set_xlabel('axis_x')
graph.set_ylabel('axis_y')
graph.set_zlabel('axis_z')



plt.title('The First 3D Graph')

plt.show()

