import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import *

fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)
n=11

def Data():
    global N
    n=N;x=0.1;m=1000;t=0.05
    a=1;l=(a*t/x)**2
    
    U=[0]*n
    for i in range(n):
        U[i]=[0]*m
    
    for j in range(0,2):
        for i in range(1,n-1):
            if i<2:
                U[i][j]=20*x*i
            else:
                U[i][j]=-(20*(x*i-1))/9
    
    for j in range(2,m):
        for i in range(1,n-1):
            U[i][j]=2*(1-l)*U[i][j-1]+l*(U[i+1][j-1]+U[i-1][j-1])-U[i][j-2]
    return U
    
e=np.array(Data()).T
#spline-cubic interpolation
xn=np.linspace(0,N,N)
yn=tck=[0]*1000
for i in range(1000):
    tck[i]=splrep(xn,e[i],s=40)
    yn[i]=splev(xn,tck[i],der=0)

xn=np.linspace(0,N,N+2)
yn=np.insert(yn,[0,N],0,axis=1)
#cubic interpolation
y=interp1d(xn,yn,kind='cubic')
x=np.linspace(0,N,5*N)

k=0
def animate(i):
    global k
    ax1.clear()
    plt.plot(x,y(x)[k])
    plt.grid(True)
    plt.ylim([-5,+5])
    plt.xlim([-1,N+1])
    k+=1

anim = animation.FuncAnimation(fig,animate,frames=360,interval=5)
#anim.save('sring_vib.mp4', dpi=100, bitrate=16384, fps=25)
plt.show(anim)
