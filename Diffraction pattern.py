from numpy import cos , sin,pi,empty,sqrt
from matplotlib.pyplot import imshow,show,hot,colorbar

def esimpson(f,a,b,err):
    N=4                                                   #the value of  slices 
    while True:
        N1=2*N
        h=float((b-a)/N)                          #i-1, the width of slices
        S=(1./3.)*(f(a)+f(b))                     #i-1 , 1st even term
        T=0
        for k in range(2,N-1,2):              #i-1 , 2nd even term   
            S += (2./3.)*f(a+(k*h))
        for j in range(1,N,2):                   #i-1 , odd term
            T += (2./3.)*f(a+(j*h))
        I1 = h*(S+(2*T))                           #i-1 , Integral value
        h1=float((b-a)/N1)                      #i , the width of slices
        Si=S+T                                          #i , even term
        Ti=0
        for i in range(1,N1,2):
            Ti += (2./3.)*f(a+(i*h1))               #i , odd term
        I2 = h1*(Si+(2*Ti))                      #i , Integral value
        er = (1./15.)*abs((I2-I1))
        N=2*N
        if er <= err:
            break
    return I2

l = 500                                                 #lambda (nm) **1nm per unit
k= (2*pi)/l

def Jm(m,x):                                        #Bessel function
    J =(1/pi)*esimpson(lambda theta : cos((m*theta)-(x*sin(theta))),0,pi,10**-6)
    return J

def I(r,l):
    k=(2*pi)/l
    r= sqrt(((10*i)-1000)**2+((10*j)-1000)**2)
    Ir=(Jm(1,k*r)/(k*r))**2
    return Ir

A = empty([201,201])
for i in range(0,201):
    for j in range(0,201):
        r=sqrt(((10*i)-1000)**2+((10*j)-1000)**2)    #let 500nm as center
        if r == 0:
            A[i,j]=0.01
        else:
            A[i,j]=I(r,l)
        print I(r,l)
        
hot()
imshow(A,origin = 'lower',extent=[0,1000,0,1000],vmax=0.01) #1000 = 1micrometer
colorbar()
show()
