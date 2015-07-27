import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ant
from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy.special import jn, jn_zeros

fig = plt.figure()
ax = ax=fig.gca(projection='3d')
radius=1
r, phi = np.meshgrid(np.linspace(0, radius, 60), np.linspace(0, 2*np.pi, 60))
x, y = r*np.cos(phi), r*np.sin(phi)

B=np.array([jn_zeros(0,5)])

m=0;k=0
def animation(t):
    global m,k
    if t>k*1*6.30 and m<4:
        m+=1;k+=1
    
    z = jn(0,B[0,m]*r/radius)*np.sin(t)
    ax.cla()
    plot = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap="cool",
                           vmin=-1, vmax=1, linewidth=0)
    ax.set_zlim(-2.5,2.5)
    ax.set_ylim(-1,1)
    ax.set_xlim(-1,1)

a = ant.FuncAnimation(fig, animation, np.linspace(0, 90*np.pi, 1800))
#plt.show(a)
a.save('circular_membrane2.mp4', dpi=100, bitrate=163840, fps=30)
print('OK')
