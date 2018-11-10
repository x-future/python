# Import NumPy and Matplotlib
import matplotlib
#%matplotlib inline


import numpy as np
import matplotlib.pyplot as plt

# # Define vector v
# v = np.array([1,1])
#
# # Plots vector v as blue arrow with red dot at origin (0,0) using Matplotlib
#
# # Creates axes of plot referenced 'ax'
# ax = plt.axes()
#
# # Plots red dot at origin (0,0)
# ax.plot(0,0,'or')
#
# # Plots vector v as blue arrow starting at origin 0,0
# ax.arrow(0, 0, *v, color='b', linewidth=2.0, head_width=0.20, head_length=0.25)
#
# # Sets limit for plot for x-axis
# plt.xlim(-2,2)
#
# # Set major ticks for x-axis
# major_xticks = np.arange(-2, 3)
# ax.set_xticks(major_xticks)
#
#
# # Sets limit for plot for y-axis
# plt.ylim(-1, 2)
#
# # Set major ticks for y-axis
# major_yticks = np.arange(-1, 3)
# ax.set_yticks(major_yticks)
#
# # Creates gridlines for only major tick marks
# plt.grid(b=True, which='major')

v = np.array([-2,-1])
#w = np.array([-2,2])
m = np.array([-1,2])
z = np.array([2, 1])
k = np.array([1, -2])
ax = plt.axes()
ax.plot(0,0, 'or')
ax.arrow(1,1, *v, color='r', linestyle='dotted', linewidth=2.5, head_width=0.30, head_length=0.35)
#ax.arrow(v[0], v[1], *w, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)
ax.arrow(-1,0, *m, color='r', linewidth=2.5, head_width=0.30, head_length=0.35)
ax.arrow(-2,2, *z, color='r', linewidth=2.5, head_width=0.30, head_length=0.35)
ax.arrow(0,3, *k, color='r', linewidth=2.5, head_width=0.30, head_length=0.35)


plt.xlim(-3, 2)
major_kticks = np.arange(-3, 2)
ax.set_kticks = (major_kticks)

plt.xlim(-3, 2)
major_mticks = np.arange(-3, 2)
ax.set_mticks = (major_mticks)

plt.xlim(-3, 2)
major_zticks = np.arange(-3, 2)
ax.set_zticks = (major_zticks)

plt.xlim(-3, 2)
major_xticks = np.arange(-3, 2)
ax.set_xticks(major_xticks)

plt.ylim(-1, 4)
major_yticks = np.arange(-1, 4)
ax.set_yticks = (major_yticks)


plt.grid(b=True, which='major')

# Displays final plot
plt.show()
