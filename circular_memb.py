import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import matplotlib.animation as animation

fig = plt.figure()
ax=fig.gca(projection='3d')
N=50;N_steps = 5000
radius = 5.
c = 0.5
dphi = 2*np.pi/N
dr = 5./N
dt = 0.005  

if dt< dr*dphi/2/c:
    # The maximum value for dt is dr*dphi/(2*c)
    dt = dr*dphi/(4*c)


def q(x,y):
    return mlab.bivariate_normal(x, y)

#%% Initial conditions
r = np.linspace(0, radius, Nr)
phi = np.linspace(0, 2*np.pi, N)
R, phi = np.meshgrid(r, phi)
X = R*np.cos(phi)
Y = R*np.sin(phi)
r[0]=dr*0.5
T = np.zeros((N_steps, N, N))
T[0]=T[1]=q(X,Y).T

#%% Stepping
k1 = c*dt**2/dr**2
for t in range(2, N_steps-1):
    for i in range(0, N-1):
        for j in range(0, N-1):
            k2 = c*dt**2/(2*r[i]*dr)
            k3 = c*dt**2/(dphi*r[i])**2
            T[t, i, j] = 2*T[t-1, i, j] - T[t-2, i, j]+ k1*(T[t-1, i+1, j] - 2*T[t-1, i, j] + T[t-1, i-1, j])+ k2*(T[t-1, i+1, j] - T[t-1, i-1, j])+ k3*(T[t-1, i, j+1] - 2*T[t-1, i, j] + T[t-1, i, j-1])
        T[t, i, -1] = T[t, i, 0]

print('OK')

k=0
def animat(t):
    global k
    ax.cla()
    plot = ax.plot_surface(X.T, Y.T, T[k], rstride=1, cstride=1, cmap="Set2",
                           vmin=-0.5, vmax=0.5, label="test", linewidth=0)
    
    ax.set_zlim(-0.3,0.3)
    ax.set_ylim(-5,5)
    ax.set_xlim(-5,5)
    k+=2

anim = animation.FuncAnimation(fig, animat, frames=N_steps-1,interval=1)
anim.save('water13.mp4', dpi=100, bitrate=163840, fps=30)
#plt.show(anim)
print('OK')
