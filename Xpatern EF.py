import numpy as np
from visual import*
from Efield import Ef

w=10
Y,X=np.mgrid[w:-w:20j,-w:w:20j]
k=1.
n=20
x1,y1,z1=5,0,0
q1=-1
E1=Ef(k,0,n,X,Y,x1,y1)

t=2
dt=0.15
while t<3.5:
    def Efc(k,q,n,X,Y,x,y):
        E=np.zeros((n,n),dtype=vector)
        for i in range(n):
            for j in range(n):
                r=vector(X[i,j]-x,Y[i,j]-y,0)
                E[i,j]=(k*q/(abs(r)**3))*r
        return E
    t+=dt
    sphere(pos=(7*sin(x1+t)+2,7*sin(t)-1,z1),radius=0.5,color=color.red)
    E1+=Efc(k,q1,n,X,Y,7*sin(x1+t)+2,7*sin(t)-1)

x2,y2,z2=-5,0,0
q2=3
charge_2=box(pos=(x2,y2,z2),color=color.blue,length=1,height=10,width=1,opacity=0.6)
E2=Ef(k,q2,n,X,Y,x2,y2)
for i in range(-5,5):
    sphere(pos=(x2,i+0.5,z2),radius=0.5,color=color.blue)
    E2+=Ef(k,q2,n,X,Y,x2,i+0.5)

E=E1+E2
for i in range(n):
    for j in range(n):
        arrow(pos=(X[i,j],Y[i,j],0),shaftwidth=0.1,axis=E[i,j],length=0.5)
