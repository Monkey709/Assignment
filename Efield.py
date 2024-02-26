import numpy as np
import visual as vsl
def Ef(k,q,n,X,Y,x,y):
    E=np.zeros((n,n),dtype=vsl.vector)
    for i in range(n):
        for j in range(n):
            r=vsl.vector(X[i,j]-x,Y[i,j]-y,0)
            E[i,j]=(k*q/(abs(r)**3))*r
    return E

