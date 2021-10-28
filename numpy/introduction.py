import numpy as np
import matplotlib.pyplot as plt

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[1])
#
# b = np.arange(12)
# print(b)
#
# c = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# print(np.sort(c))

# d = b.reshape(4, 3)
# print(d)

# e = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(e[e < 5])
# five_up = (e >= 5)
# print(e[five_up])

f = np.array([[1, 2], [3, 4], [5, 6]])
print(f[0, 1])
print(f[1:3])
print(f.max())
print(f.min())
print(f.sum())

# g = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
# plt.plot(g)
# plt.show()
#
#
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()
