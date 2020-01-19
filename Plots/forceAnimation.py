import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation 
import mpl_toolkits.mplot3d.axes3d as p3
import pandas as pd 

fig = plt.figure()
ax = p3.Axes3D(fig)
min_ax = -2
max_ax = 2

ax.set_xlim3d([min_ax, max_ax])
ax.set_xlabel('X')

ax.set_ylim3d([min_ax, max_ax])
ax.set_ylabel('Y')

ax.set_zlim3d([min_ax, max_ax])
ax.set_zlabel('Z')

lines = ax.plot([0, 0], [0, 0], [0, 0], color='k')

epi = 0.5
tcoord = np.linspace(0, 100, 1000)
xcoord = np.sin(tcoord)
ycoord  = np.cos(tcoord)
zcoord = np.tan(tcoord)

result = [[], [], []]

data = pd.read_csv("collection/pls.csv")

prev = [0, 0, 0]
mn = 5
def updateArrow(i):
    ax.clear()
    lines = ax.quiver(prev[0], prev[1], prev[2], data['x'][i]/mn, data['y'][i]/mn, data['z'][i]/mn)
    #print(prev, data['x'][i], data['y'][i], data['z'][i])
    prev[0] += data['x'][i]/mn
    prev[1] += data['y'][i]/mn
    prev[2] += data['z'][i]/mn

    ax.set_xlim3d([min_ax, max_ax])
    ax.set_xlabel('X')

    ax.set_ylim3d([min_ax, max_ax])
    ax.set_ylabel('Y')

    ax.set_zlim3d([min_ax, max_ax])
    ax.set_zlabel('Z')
    #result.append((xcoord[i], ycoord[i], zcoord[i]))
    #ax.plot(result)
    return lines,

anim = animation.FuncAnimation(fig, updateArrow, frames=700, interval= 100)

plt.show()
