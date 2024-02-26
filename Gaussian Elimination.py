from numpy import array , dot,empty

def lineareq(A,v):
    N=len(A)            #if A= m x n, then N=m
    for k in range(0,N):
        for i in range(k,N):
            if abs(A[i,k])>abs(A[k,k]):
                for j in range(k,N):
                    a=A[i,j]
                    b=A[k,j]
                    A[k,j]=a
                    A[i,j]=b
        c=A[k,k]
        for j in range(k,N):
            A[k,j]/=c
        for i in range(k+1,N):
            d=A[i,k]
            for j in range(k,N):
                A[i,j]=A[i,j]-(A[k,j]*d)

    x=empty([N,1])
    for i in range(0,N-1):
        x[N-1,0]=v[N-1,0]
        x[N-2-i,0]=v[N-2-i,0]
        for j in range(0,i+1):
            x[N-2-i,0]-=(A[N-2-i,N-1-j]*x[N-1-j,0])
    return x




'''
v=array([[-4.],[3.],[9.],[7.]]) 
A=array([[2.,1.,4.,1.],[3.,4.,-1.,-1.],[1.,-4.,1.,5.],[2.,-2.,1.,3.]])
print lineareq(A,v)

'''
