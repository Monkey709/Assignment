import numpy as np
import visual as vsl

w=8
Y,X,Z=np.mgrid[w:-w:10j,-w:w:10j,-w:w:10j]
l=1
n=10
x1,y1,z1=1,0,0
q1=1
charge_1=vsl.sphere(radius=0.1,pos=(x1,y1,z1),color=vsl.color.red)

x2,y2,z2=-1,0,0
q2=-1
charge_2=vsl.sphere(radius=0.1,pos=(x2,y2,z2),color=vsl.color.blue)
E1=np.zeros((n,n,n),dtype=vsl.vector)
for i in range(n):
    for j in range(n):
        for k in range(n):
            r1=vsl.vector(X[i,j,k]-x1,Y[i,j,k]-y1,Z[i,j,k]-z1)
            E1[i,j,k]=(l*q1/(abs(r1)**3))*r1

E2=np.zeros((n,n,n),dtype=vsl.vector)
for i in range(n):
    for j in range(n):
        for k in range(n):
            r2=vsl.vector(X[i,j,k]-x2,Y[i,j,k]-y2,Z[i,j,k]-z2)
            E2[i,j,k]=(l*q2/(abs(r2)**3))*r2

E=E1+E2

for i in range(n):
    for j in range(n):
        for k in range(n):
            vsl.arrow(pos=(X[i,j,k],Y[i,j,k],Z[i,j,k]),shaftwidth=0.1,axis=E[i,j,k],length=0.5)

