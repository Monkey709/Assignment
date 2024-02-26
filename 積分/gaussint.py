from gaussxw import gaussxw 
from numpy import array



def gaussxwint(f,a,b,N):
    x = (array(gaussxw(N)).tolist())[0]
    w = (array(gaussxw(N)).tolist())[1]
   
    s = 0
    for i,j in zip(x,w):
    
        xp = 0.5*(b-a)*i + 0.5*(b+a)
        wp = 0.5*(b-a)*j
        s += wp*f(xp)        
    return s
