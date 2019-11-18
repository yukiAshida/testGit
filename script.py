import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(x, y)
ax = fig.add_subplot(1,2,2)
ax.plot(x, z)
plt.show()

