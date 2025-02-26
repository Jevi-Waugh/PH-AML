import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


t = np.linspace(0,2*np.pi, 100)
x = (np.sin(t) + 2*np.sin(2*t))
y = (np.cos(t) - 2*np.cos(2*t))
z = (np.sin(3*t))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='b')

# Setting labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trefoil Knot')

plt.show()