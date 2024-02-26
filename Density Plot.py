from numpy import empty,sqrt,pi,sin
from matplotlib.pyplot import imshow,show,gray

x=0
y=0
h0=1
A=empty([500,500])
(x1,y1)=(50,40)
(x2,y2)=(50,60)

for i in range(0,500):
    for j in range(0,500):
        y=j/5.
        r1=sqrt((x-x1)**2+(y-y1)**2)
        r2=sqrt((x-x2)**2+(y-y2)**2)
        h=h0*sin((2*pi/5)*r1)+h0*sin((2*pi/5)*r2)
        A[i,j]=h
    x=i/5.
gray()
imshow(A,origin="lower",extent=[0,100,0,100])
show()
