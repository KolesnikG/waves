import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.gca(projection='3d')

def q(x,y,teta):
    gabor=np.exp(-1/2*(x**2+y**2))*np.cos(2*np.pi*teta*x)
    return  gabor
 
def plot_q():
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(X, Y)
    phi=np.pi/8
    xphi=X*np.cos(phi)+Y*np.sin(phi)
    yphi=-X*np.sin(phi)+Y*np.cos(phi)
    return [xphi,yphi,X,Y]

x,y,X,Y=plot_q()

N=100
T=np.zeros((10*N,N,N))
teta=0;i=0
for t in range(0,10*N-1):
    T[t]=q(x,y,teta=i)
    i+=0.006
print('OK')

k=0
def animat(t):
    global k
    ax.cla()
    plot = ax.plot_surface(X, Y, T[k], rstride=1, cstride=1, cmap=plt.get_cmap('Set2'),linewidth=0)
    ax.set_zlim(-1,1)
    ax.set_ylim(-5,5)
    ax.set_xlim(-5,5)
    k+=1

anim = animation.FuncAnimation(fig, animat, frames=10*N-1,interval=5)
anim.save('gabor_2Dfilter.mp4', dpi=100, bitrate=163840, fps=30)
#plt.show(anim)
print('OK')
