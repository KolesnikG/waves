import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

np.random.seed(1)

steps = 4000
tr=25

def lorenz(x, y, z, s=10, r=28, b=8./3, dt=0.01) :
    x_dot =x + (s*(y - x))*dt
    y_dot =y + (r*x - y - x*z)*dt
    z_dot =z + (x*y - b*z)*dt
    return x_dot, y_dot, z_dot

scatter_matrix = np.zeros((3,3))
U=np.zeros((steps,tr,3))
U[0]=-15+30*np.random.random((tr,3))
for i in range(0,steps-1):
    for j in range(0,tr):
        x_dot, y_dot, z_dot = lorenz(U[i][j][0], U[i][j][1], U[i][j][2])
        U[i+1][j][0] = x_dot
        U[i+1][j][1] = y_dot 
        U[i+1][j][2] = z_dot
        
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
      xs3d, ys3d, zs3d = self._verts3d
      xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
      self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
      FancyArrowPatch.draw(self, renderer)
      
def CalculateVectors(U,k):
    global scatter_matrix
    mean_x=np.mean(U[k,:,0])
    mean_y=np.mean(U[k,:,1])
    mean_z=np.mean(U[k,:,2])
    mean_vector = np.array([[mean_x],[mean_y],[mean_z]])
    for i in range(tr):
        scatter_matrix += (U[k,i,:].reshape(3,1) - mean_vector).dot((U[k,i,:].reshape(3,1) - mean_vector).T)

    eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)
    
    for v in eig_vec_sc.T:
        a = Arrow3D([0,10*v[0]+ mean_x], 
                    [0,10*v[1]+ mean_y], 
                    [0,10*v[2]+ mean_z], mutation_scale=20, lw=1, arrowstyle="-|>", color="r")
        
        ax.add_artist(a)

fig = plt.figure()
ax=fig.gca(projection='3d')


k=0
def animat(t):
    global k
    ax.cla()
    CalculateVectors(U,k)
    ax.scatter(U[k,:,0], U[k,:,1], U[k,:,2],c='r')
    
    ax.set_zlim(0,60)
    ax.set_ylim(-25,25)
    ax.set_xlim(-19,19)
    
    k+=1
    
anim = animation.FuncAnimation(fig, animat, frames=steps-1,interval=5)
anim.save('lorenz.mp4', dpi=100, bitrate=163840, fps=30)
#plt.show(anim)
print('OK')
