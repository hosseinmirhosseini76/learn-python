import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])
#
# plt.plot(xpoints, ypoints)
# plt.show()


# ! example 1
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.plot(xpoints, ypoints)
# plt.show()

# ! example 2
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.plot(xpoints, ypoints, 'or')
# plt.plot(xpoints, ypoints, marker='o', ms=30, mec='red', mfc='orange')
# plt.plot(xpoints, ypoints, linestyle='dashed', linewidth = '10')


# ! example 3
# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)

# ! example 4
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.sin(4 * np.pi * t)
plt.figure(1)
plt.subplot(211)
plt.plot(t, s1, 'r', linewidth='3')
plt.subplot(212)
plt.plot(t, 2 * s1)
plt.show()
