
##gaussxwint

from gaussxw import gaussxw 
import numpy as np



def gaussxwint(f,a,b,N):
    x = (np.array(gaussxw(N)).tolist())[0] #convert the values x in gaussxw to a list
    w = (np.array(gaussxw(N)).tolist())[1] #convert the values w in gaussxw to a list
    s = 0 
    for i,j in zip(x,w):   #i stands for x and j stands for w, run the loop with x and w simultaneously
        xp = 0.5*(b-a)*i + 0.5*(b+a)
        wp = 0.5*(b-a)*j
        s += wp*f(xp) # the sum of the each term in equation of gauss quateture         
    return s

        
    
