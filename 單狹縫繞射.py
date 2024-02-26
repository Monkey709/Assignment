import matplotlib.pyplot as plt
import numpy as np
from intensity import I,Ei,E

L=8*10**5             #屏幕距離 μm
a=62.5                #狹縫寬   μm
d=250                 #狹縫間距 μm
c=300                 #光速    μm/fs
wl=0.465              #波長    μm
f=c/wl                #頻率     /fs
w=2*np.pi*f
Y=4*10**5
T=1/f
I0=500
N=20
tt=0
dtt=0.01             #L*tan(π/4)=R
x=np.linspace(L*np.tan(-0.25*np.pi),L*np.tan(0.25*np.pi),1000001) 
print(x)
x2=np.vectorize(x)
a2=np.vectorize(a**-1)
for i in range(-5,5):
        Ei=Ei(x2,i*np.multiply(a2,np.array(11)),T) #(a/11)狹縫寬除以11個光源
E=E(x,T)
y=I(x)

plt.xlim(-Y/2,Y/2)
plt.ylim(0,1000)
plt.xlabel('y(m)')
plt.ylabel('I(y)')
plt.title('f(t)-t)')
plt.plot(x,y)
plt.show()




