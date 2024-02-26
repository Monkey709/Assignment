from numpy import cos , sin,pi

def simpson(f,a,b,N):
    h=float((b-a)/N)                                 #the width of slices
    S=(1./3.)*(f(a)+f(b))                            #set zeroth & last point
    T=0                                                       
    for k in range(2,N-1,2):
        S += (1./3.)*2*f(a+k*h)                    #sum even term
    for j in range(1,N,2):
        T += (2./3.)*f(a+j*h)                        #sum odd term
    I = h*(S+(2*T))                                     #Integral value
    return '(simpson)N = %s Integral Value = %s' %(N,I)

def esimpson(f,a,b,err):
    N=4                                                   #the value of  slices 
    while True:
        N1=2*N
        h=float((b-a))/N                          #i-1, the width of slices
        S=(1./3.)*(f(a)+f(b))                     #i-1 , 1st even term
        T=0
        for k in range(2,N-1,2):              #i-1 , 2nd even term   
            S += (2./3.)*f(a+(k*h))
        for j in range(1,N,2):                   #i-1 , odd term
            T += (2./3.)*f(a+(j*h))
        I1 = h*(S+(2*T))                           #i-1 , Integral value
        h1=float((b-a))/N1                      #i , the width of slices
        Si=S+T                                          #i , even term
        Ti=0
        for i in range(1,N1,2):
            Ti += (2./3.)*f(a+(i*h1))               #i , odd term
        I2 = h1*(Si+(2*Ti))                      #i , Integral value
        er = (1./15.)*abs((I2-I1))
        N=2*N
        if er <= err:
            break
    return (I2,N1,er)


