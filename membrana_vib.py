import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.animation as anmt

fig = plt.figure()
ax=fig.gca(projection='3d')
 
def plot_q():
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = mlab.bivariate_normal(X, Y)
    return [X,Y,Z]

X,Y,Z=plot_q()

N=100
T=np.zeros((50*N,N,N))
T[0]=T[1]=Z

dh=0.1;dt=0.05
c=(dt/dh)**2

for t in range(2,50*N-1):
    for j in range(0,N-1):
        for i in range(0,N-1):
            T[t][i][j]=2*T[t-1][i][j]-T[t-2][i][j]+c*(T[t-1][i+1][j]+T[t-1][i-1][j]+T[t-1][i][j+1]+T[t-1][i][j-1]
                                                       -4*T[t-1][i][j])

k=0
def animation(t):
    global k
    ax.cla()
    plot = ax.plot_surface(X, Y, T[k], rstride=1, cstride=1, cmap="Accent",
                           vmin=-1, vmax=1, label="test", linewidth=0)
    ax.set_zlim(-0.15,0.15)
    ax.set_ylim(-5,5)
    ax.set_xlim(-5,5)
    k+=1

a = anmt.FuncAnimation(fig, animation, frames=360,interval=5)
#a.save('vib.mp4', dpi=100, bitrate=163840, fps=30)
plt.show(a)
