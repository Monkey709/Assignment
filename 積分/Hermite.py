from numpy import sqrt , pi,exp,arange
from math import factorial
from matplotlib.pyplot import plot , show , legend,xlabel,ylabel,ylim,xlim

def H(n,x):
    if n == 0:
       return 1
    elif n == 1:
       return 2*x     
    else:
        H0 = 1
        H1 = 2*x
        k = 2
        Hn = 2*x*H1 - 2*(k-1)*H0
        while k <= n:
            k += 1           
            H0 = H1           
            H1 = Hn           
            Hn = 2*x*H1 - 2*(k-1)*H0
        return H1
        
def psi(n,x):
    return (1./sqrt((2**n)*factorial(n)*sqrt(pi)))*exp((-x**2)/2)*H(n,x)    

i = []
n0 = []
n1 = []
n2 = []
n3 = []        
for x in arange(-4,4.01,0.01):   
    i.append(x)
    n0.append(psi(0,x))
    n1.append(psi(1,x))
    n2.append(psi(2,x))
    n3.append(psi(3,x))

plot(i,n0,'red',label = 'psi0')
plot(i,n1,'blue',label = 'psi1')
plot(i,n2,'green',label = 'psi2')
plot(i,n3,'black',label = 'psi3')
legend()
xlabel('x')
ylabel('psi(n,x)')
ylim(-0.8,0.8)
show()
    
j = []
n30 = []    
for x in arange(-10,10.01,0.01):   
    j.append(x)
    n30.append(psi(30,x))

plot(j,n30,label = 'psi30')
legend()
xlabel('x')
ylabel('psi(30,x)')
xlim(-10,10)
show()   
