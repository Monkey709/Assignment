from visual import*
from visual.graph import*

d1=gdisplay(x=600,y=10,xtitle='t(s)',ytitle='x(m)',ymax=10,xmax=20,ymin=-10)

ball=sphere(pos=(-0,5,0),radius=0.03,color=color.white)

tx=gcurve(gdisplay=d1,color=color.yellow)

dt=0.1
t=0
v=vector(1,0,0)

while true:
    rate(10)
    ball.pos=v*t
    t=t+dt
    tx.plot(pos=(t,ball.pos.x))
