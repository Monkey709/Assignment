from numpy import sin , cos ,pi,empty
from trapezoidal import trapezoidal , etrapezoidal
from Simpson import esimpson

def romberg(f,a,b,e):
    N=2
    R=empty([30,30])                              #make a space for numbers
    R[1,1]=trapezoidal(f,a,b,N)
    for i in range(2,30):
        ans = False                                     # for break double loop
        R[i,1]=trapezoidal(f,a,b,N**i)
        for j in range(2,30):
            if j > i:
                break                                        # if j > i still work is pointless
            R[i,j]=R[i,j-1]+(1./((4.**(j-1))-1.))*(R[i,j-1]-R[i-1,j-1])
            er =(1./((4.**j)-1.))*abs((R[i,j]-R[i-1,j]))
            if er <= e :
                ans = True                               #break the next loop
                break
        if (ans):   
            break
    return (R[i,j] , N**i , er)

A = romberg(lambda x:(x**4)-(2*x)+1,0,2,10**-10)
print 'Ex.1 : R = %s' %(A[0])

B=etrapezoidal(lambda x:(sin((100*x)**0.5))**2,0,1,10**-6)
print 'Ex.2 : I = %s , N = %s , error = %s ' %(B[0],B[1],B[2])

C = esimpson(lambda x:(sin((100*x)**0.5))**2,0,1,10**-6)
print 'Ex.3 : I = %s , N = %s , error = %s ' %(C[0],C[1],C[2])

D=romberg(lambda x:(sin((100*x)**0.5))**2,0,1,10**-6)
print 'Ex.4 : I = %s , N = %s , error = %s ' %(D[0],D[1],D[2])


