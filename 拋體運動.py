from visual import*
from visual.graph import*

d1=gdisplay(x=450,y=10,xtitle='t(s)',ytitle='x(m)',ymax=12,xmax=2.5)
floor=box(length=70,height=0.01,width=20,color=color.green)

ball=sphere(radius=0.9,color=color.white)

tx=gcurve(gdisplay=d1,color=color.yellow)

g=9.8

dt=0.01
t=0
v=vector(20,20,0)

while ball.pos.y>=0:
    rate(100)
    ball.pos=v*t
    t=t+dt
    v.y=v.y-g*dt
    tx.plot(pos=(t,v.y*t-0.5*g*dt**2))
