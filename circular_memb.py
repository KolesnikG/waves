import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import matplotlib.animation as animation

fig = plt.figure()
ax=fig.gca(projection='3d')
N=50

def q(R):
    return 1/(2*np.pi)*np.exp(-(R**2)/2)
 
def plot_q():
    radius = 5
    r=np.arange(0.1, radius+0.1, 0.1)
    R, phi = np.meshgrid(r, np.linspace(0, 2*np.pi, N))
    x, y = R*np.cos(phi), R*np.sin(phi)
    z =q(R)
    return [x,y,z,phi,r]

X,Y,Z,phi,r=plot_q()
T=np.zeros((5*N,N,N))
T[0]=T[1]=Z

dt=0.05**2
teta=2*np.pi/N;
dr=0.1;c=0.5
r[0]=dr*0.5

for t in range(2,5*N-1):
    for j in range(1,N-1):
        for i in range(1,N-1):
            T[t][i][j]=2*T[t-1][i][j]-T[t-2][i][j]+((c*dt/dr**2)*(T[t-1][i+1][j]-2*T[t-1][i][j]+T[t-1][i-1][j]))+(c*dt/(2*r[i]*dr))*(T[t-1][i+1][j]-T[t-1][i-1][j])+((c*dt/((teta*r[i])**2))*((T[t-1][i][j+1]-2*T[t-1][i][j]+T[t-1][i][j-1])))
            
print('OK')

k=0
def animat(t):
    global k
    ax.cla()
    plot = ax.plot_surface(X, Y, T[k], rstride=1, cstride=1, cmap="Accent",
                           vmin=-1, vmax=1, label="test", linewidth=0)
    
    ax.set_zlim(-0.3,0.3)
    ax.set_ylim(-5,5)
    ax.set_xlim(-5,5)
    k+=1

anim = animation.FuncAnimation(fig, animat, frames=5*N-1,interval=5)
#anim.save('v1.mp4', dpi=100, bitrate=163840, fps=30)
plt.show(anim)
print('OK')
