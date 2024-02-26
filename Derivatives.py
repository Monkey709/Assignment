from numpy import tanh, cosh,linspace,sinh
from matplotlib.pyplot import plot,title,show,scatter,legend

def f(x):
    return  1+ 0.5*tanh(2*x)

def derivative(f):
    h = 0.001
    return (f(x+h/2)-f(x-h/2))/h
     
def df(x):
    return (1/cosh(2*x))**2
    
x = linspace(-2,2,50)   
scatter(x,derivative(f),color='red',label='numerical')
plot(x,df(x),label='analytical')
title('first derivative')
legend()
show()

def secderivative(f):
    h=0.001
    return (f(x+h)+f(x-h)-2*f(x))/h**2
 
def ddf(x):
    return -4*(sinh(2*x)/(cosh(2*x)**3))
    
scatter(x,secderivative(f),color='red',label='numerical')
plot(x,ddf(x),label='analytical')
title('second derivative')
legend(loc='upper right')
show()
