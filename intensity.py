import numpy as np
import matplotlib.pyplot as plt
from integrate import gaussxwint

L=8*10**5
c=300  
wl=0.465                
f=c/wl                  #/fs
w=2*np.pi*f 
E0=5
T=1/f

def Ei(y,y0,t):
    r = np.sqrt(L**2 + (y-y0)**2)
    return E0*np.sin(w*t-t*r)
    
def E(y,t):
    return sum(Ei)

def I(y):
    return 1/T*gaussxwint(E(y,t),0,T,5)
    
    
