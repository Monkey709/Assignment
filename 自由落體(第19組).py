from visual import*
from visual.graph import*
#第19組，李豪盛、林子喬、曾智詮
size=0.5
g=9.8
m=5
p=1.2
A=2*pi*(size**2)
c=0.5

v1=gdisplay(title='v-t圖',x=1000,y=0,xtitle='time(s)',ytitle='velocity(m/s)')
a1=gdisplay(title='a-t圖',x=1000,y=390,xtitle='time(s)',ytitle='acceleration(m/s^2)')
h1=gdisplay(title='h-t圖',x=1000,y=780,xtitle='time(s)',ytitle='height(m)')
vt=gcurve(gdisplay=v1,color=color.yellow)
at=gcurve(gdisplay=a1,color=color.red)
ht=gcurve(gdisplay=h1,color=color.blue)

display (title='自由落體',width=1000,height=1080)
floor=box(length=70,height=0.01,width=20,color=color.green)
ball=sphere(radius=size,color=color.red)
ball.pos=vector(0,100,0)
ball.v=vector(0,0,0)

t=0
dt=0.01
while ball.pos.y>=size:
    rate(100)
    t +=dt
    ball.pos += ball.v*dt
    f=vector(0,0.5*p*A*c*mag2(ball.v),0)
    ball.v += vector(0,-g*dt,0) + f*dt
    u=mag(ball.v)
    u1=mag(ball.pos)
    vt.plot(pos=(t,u))
    at.plot(pos=(t,u/t))
    ht.plot(pos=(t,u1))
