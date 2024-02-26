from numpy import cos , sin,pi,linspace
from matplotlib.pyplot import show,plot,title,xlabel,ylabel,legend

def esimpson(f,a,b,err):
    N=4                                                   #the value of  slices 
    while True:
        N1=2*N
        h=float((b-a)/N)                          #i-1, the width of slices
        S0=(1./3.)*(f(a)+f(b))                     #i-1 , 1st even term
        for k in range(2,N-1,2):              #i-1 , 2nd even term   
            S1 = (2./3.)*f(a+(k*h))
        for j in range(1,N,2):                   #i-1 , odd term
            T = (2./3.)*f(a+(j*h))
        S = S0 + S1
        I1 = h*(S+(2*T))                           #i-1 , Integral value
        h1=float((b-a)/N1)                      #i , the width of slices
        Si=S+T                                          #i , even term
        for i in range(1,N1,2):
            Ti = (2./3.)*f(a+(i*h))               #i , odd term
        I2 = h1*(Si+(2*Ti))                      #i , Integral value
        er = abs((1./15.)*(I2-I1))
        N=2*N
        if er >= err:
            break
    return I2

def Jm(m,x):                                        #Bessel function
    J =(1/pi)*esimpson(lambda theta : cos((m*theta)-(x*sin(theta))),0,pi,10**-6)
    return J
J0=[]                                                     #set up a empty set
J1=[]
J2=[]
x=linspace(0,20,200)                         #range(0,20) is inaccurate

for i in x:
    a=Jm(0,i)
    b=Jm(1,i)
    c=Jm(2,i)
    J0.append(a)
    J1.append(b)
    J2.append(c)

plot(x,J0,label = 'J0')
plot(x,J1,label = 'J1')
plot(x,J2,label = 'J2')
title('Bessel Function  J(m,x)')
xlabel('x')
ylabel('Jm(x)')
legend()                                               #show the line label
show()

    


