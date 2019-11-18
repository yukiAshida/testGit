import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(1,2,1)

ax.set_title("sin wave")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1,1)

print("debug")

ax.plot(x, y)
ax = fig.add_subplot(1,2,2)
ax.plot(x, z)
plt.show()

print("HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
y = 10000

print("new")
print("new2")
print("new3")