from numpy import array , arange,sum
from gaussxw import gaussxw
from matplotlib.pyplot import plot , show ,title,xlabel,ylabel

def gaussxwintx2(f1,f2,a1,b1,a2,b2,N):  #double gauss's integral
    xp = (array(gaussxw(N)).tolist())[0]
    wp = (array(gaussxw(N)).tolist())[1]
    m = []        
    n = []
    for k,l in zip(xp,wp):            
        m.append(k)
        n.append(l)
        for i,j in zip(m,n):
            y = 0.5*(b2-a2)*k + 0.5*(b2+a2)
            w2 = 0.5*(b2-a2)*l
            x = 0.5*(b1-a1)*i + 0.5*(b1+a1)
            w1 = 0.5*(b1-a1)*j
            fy = w2*f2(x,y,z) 
            fx = w1*f1(x,y,z)
            s = sum(fy*fx)         #the original sum in python can't to process
    return s
    
def Eq(x,y,z):
    return 1./(x**2+y**2+z**2)**(3./2.)

L=10
def Fz(z):
    return 6.674*10e-11*(10*10e3/(10*10))*z*gaussxwintx2(Eq,Eq,-(L/2),(L/2),-(L/2),(L/2),100)
  
p = []
q = []    
for z in arange(0,10.1,0.1):
    p.append(z)
    q.append(Fz(z))
    
plot(p,q)
xlabel('z(m)')
ylabel('Fz(N)')
title('Fz against z')
show()
