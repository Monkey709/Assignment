from visual import*
from visual.graph import*

b1=sphere(pos=(2,0),radius=0.3,color=color.blue,make_trail=true)
b2=sphere(pos=(1,0),radius=0.3,color=color.red,make_trail=true)
b3=sphere(pos=(2,0),radius=0.3,color=color.white,make_trail=true)

gb1=gdisplay(x=800,y=0,title='y-t',xtitle='t',ytitle='y')
g1=gcurve(gdisplay=gb1,color=color.blue)
g2=gcurve(gdisplay=gb1,color=color.red)
g3=gcurve(gdisplay=gb1,color=color.white)

t=0
dt=0.01
while true:
    rate(10)
    t+=dt
    b1.pos=(2*cos(2*pi*t),2*sin(2*pi*t))
    b2.pos=(1*cos(2*pi*t),2*sin(2*pi*t))
    b3.pos=(2*cos(2*pi*t),1*sin(2*pi*t))
    g1.plot(pos=(t,2*sin(2*pi*t)))
    g2.plot(pos=(t,2*sin(2*pi*t)))
    g3.plot(pos=(t,2*sin(2*pi*t)))
