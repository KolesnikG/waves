import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

np.random.seed(1)

steps = 3000
tr=25

def lorenz(x, y, z, s=10, r=28, b=8./3, dt=0.01) :
    return [x + (s*(y - x))*dt, y + (r*x - y - x*z)*dt, z + (x*y - b*z)*dt]

scatter_matrix = np.zeros((3,3))
U=np.zeros((steps,tr,3))
U[0]=-15+30*np.random.random((tr,3))
for i in range(0,steps-1):
    for j in range(0,tr):
        U[i+1][j][0], U[i+1][j][1], U[i+1][j][2]=lorenz(U[i][j][0], U[i][j][1], U[i][j][2]) 
        
class DrawVectors(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
        
fig = plt.figure()
ax=fig.gca(projection='3d')

k=0
def animat(t):
    global k
    ax.cla()
    CalculateVectors(U[k])
    ax.scatter(U[k,:,0], U[k,:,1], U[k,:,2],c='r')
    
    ax.set_zlim(0,60)
    ax.set_ylim(-25,25)
    ax.set_xlim(-19,19)
    
    k+=1

anim = animation.FuncAnimation(fig, animat, frames=steps-2,interval=5)
anim.save('lorenz.mp4', dpi=100, bitrate=163840, fps=30)
#plt.show(anim)
print('OK')
