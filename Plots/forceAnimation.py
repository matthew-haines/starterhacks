import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation 
import mpl_toolkits.mplot3d.axes3d as p3

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
it = 0
mult = 1
"""def updateArrow(i):
    global it, mult
    if it >= len(coord):
        mult = -1
    elif it < 0:
        mult = 1
    
    it += mult
    lines = ax.plot(coord[i][0], coord[i][1], coord[i][2], color='k')
    return lines,

anim = animation.FuncAnimation(fig, updateArrow, frames=5, interval= 20)"""

result = [[], [], []]
def updateArrow(i):
    global it, mult, epi

    #ax.clear()
    lines = ax.quiver(0, 0, 0, xcoord[i], ycoord[i], zcoord[i])

    ax.set_xlim3d([min_ax, max_ax])
    ax.set_xlabel('X')

    ax.set_ylim3d([min_ax, max_ax])
    ax.set_ylabel('Y')

    ax.set_zlim3d([min_ax, max_ax])
    ax.set_zlabel('Z')
    result.append((xcoord[i], ycoord[i], zcoord[i]))
    #ax.plot(result)
    return lines,

anim = animation.FuncAnimation(fig, updateArrow, frames=10000, interval= 100)


plt.show()
