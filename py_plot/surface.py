# /usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(1, 5, 1)
Y = np.arange(1, 11, 1)
X, Y = np.meshgrid(X, Y)

z =  np.array([[2266810,2493728, 2500720,2361884],
    [2342998,2581109,2588140,2438381],
[2353882,2593592,2600657,2449252],
[2364766,2606075,2613174,2460173],
[2353882,2593592,2600657,2449252],
[2342998,2581109,2588140,2438331],
[2332114,2568626,2575623,2427410],
[2288578,2518694,2525555,2383726],
[2201506,2418830,2425419,2301615],
[0,2219102,2219636,2131724]])

ax.plot_surface(X, Y, z, rstride=1, cstride=1, cmap='rainbow')
plt.draw()
plt.show()
plt.close()
