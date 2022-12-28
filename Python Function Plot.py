# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:33:54 2022

@author: dokaf
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm





x = np.arange(0,2*np.pi,0.1)
y = 2*(np.sin(x)) - (3*np.cos(2*x))
left,right = (plt.xlim(0,6),plt.ylim(-3,5))

plt.plot(x,y,marker = "^", ms = "15", markevery = 1/8*np.pi  ,color = 'black', linewidth = 4,)
plt.show()




M = 120
My = -M*np.cos(45)
Mz =-M*np.sin(45)
Iy = 1584
Iz = 736

y = np.linspace(-4,np.pi,400)
z = np.linspace(-8,np.pi, 800)

y , z = np.meshgrid(y,z)
stress = -Mz*y/Iz + My*z/Iy

fig = plt.figure(figsize = (15,15))


ax = fig.add_subplot(111, projection = "3d")
ax.plot_surface(y,z,stress)
ax.set_xlabel("Horizontal position (cm)")
ax.set_ylabel("Vertical position (cm)")
ax.set_zlabel("Stress (Mpa)")

plt.show()
