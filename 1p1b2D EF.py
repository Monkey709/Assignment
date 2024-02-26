from visual import*
import numpy as np

w=10
Y,X=np.mgrid[w:-w:20j,w:-w:20j]
k=1

n=20
x1,y1,z1=3,0,0
q1=5
charge_1=sphere(radius=0.5,pos=(x1,y1,z1),color=color.red)

x2,y2,z2=-3,0,0
y3=-1
y4=-2
y5=1
y6=2
q2=-1
charge_2=sphere(radius=0.5,pos=(x2,y2,z2),color=color.blue)
charge_3=sphere(radius=0.5,pos=(x2,y3,z2),color=color.blue)
charge_4=sphere(radius=0.5,pos=(x2,y4,z2),color=color.blue)
charge_5=sphere(radius=0.5,pos=(x2,y5,z2),color=color.blue)
charge_6=sphere(radius=0.5,pos=(x2,y6,z2),color=color.blue)
E1=np.zeros((n,n),dtype=vector)
for i in range(n):
    for j in range(n):
        r1=vector(X[i,j]-x1,Y[i,j]-y1,0)
        E1[i,j]=(k*q1/(abs(r1)**3))*r1

E2=np.zeros((n,n),dtype=vector)
for i in range(n):
    for j in range(n):
         r2=vector(X[i,j]-x2,Y[i,j]-y2,0)
         E2[i,j]=(k*q2/(abs(r2)**3))*r2

E3=np.zeros((n,n),dtype=vector)
for i in range(n):
    for j in range(n):
         r3=vector(X[i,j]-x2,Y[i,j]-y3,0)
         E3[i,j]=(k*q2/(abs(r3)**3))*r3
         
E4=np.zeros((n,n),dtype=vector)
for i in range(n):
    for j in range(n):
         r4=vector(X[i,j]-x2,Y[i,j]-y4,0)
         E4[i,j]=(k*q2/(abs(r4)**3))*r4

E5=np.zeros((n,n),dtype=vector)
for i in range(n):
    for j in range(n):
         r5=vector(X[i,j]-x2,Y[i,j]-y5,0)
         E5[i,j]=(k*q2/(abs(r5)**3))*r5
         
E6=np.zeros((n,n),dtype=vector)
for i in range(n):
    for j in range(n):
         r6=vector(X[i,j]-x2,Y[i,j]-y6,0)
         E6[i,j]=(k*q2/(abs(r6)**3))*r6
         
E=E1+E2+E3+E4+E5+E6

for i in range(n):
    for j in range(n):
        arrow(pos=(X[i,j],Y[i,j]),shaftwidth=0.15,axis=E[i,j],length=0.6)


def E(n,y):
    E=np.zeros((n,n),dtype=vector)
    for i in range(n):
        for j in range(n):
             r=vector(X[i,j]-x2,Y[i,j]-y,0)
             E[i,j]=(k*q2/(abs(r)**3))*r

    return E


    
