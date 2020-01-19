import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
"""t = np.linspace(0, 100, 101)
x = np.sin(t)
y = np.cos(t)
z = np.tan(t)"""

data = pd.read_csv("collection/pls.csv")
x, y, z = data['x'], data['y'], data['z']
t = np.linspace(0, len(data)-1, len(data))
fig, ax = plt.subplots(3)

ax[0].plot(t, x)
ax[0].set_title("X")
ax[1].plot(t, y)
ax[1].set_title("Y")
ax[2].plot(t, z)
ax[2].set_title("Z")
plt.show()