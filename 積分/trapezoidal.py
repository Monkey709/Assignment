import numpy as np

def trapezoidal(f,a,b,N):
    h = float((b-a))/float(N)                #the width of slices
    s = float(0.5*(f(a)+f(b)))  #1st term of the trapezoidal rule
    for k in range(1,N+1):
        s += f(a+(k*h))                     #2nd term of the trapezoidal rule
    I=h*s
    return I                             

def etrapezoidal(f,a,b,err):
    N = 2
    while True :
        N=2*N
        I1 = trapezoidal(f,a,b,N)
        I2 = 0.5*I1                                #1st term of the error trapezoidal rule
        h = float((b-a))/N
        for k in range(1,N,2): 
            I2 += h*f(a + k*h)          #2nd term of the error trapezoidal rule
        er =(1./3.)*abs((I2-I1))
        if er < err:
            break
    return I2 , N , er     


