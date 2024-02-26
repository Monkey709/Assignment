from visual import*
from visual.graph import*
#第19組
d1=gdisplay(x=600,y=10,title='y-t',ytitle='y(m)',xtitle='t(s)')#開小窗
floor=box(length=20,height=0.01,width=10,color=color.green)

b=sphere(pos=(0,20,0),radius=1,make_trail=true)#球,make_trail=true 是畫出軌跡
yt=gcurve(display=d1,color=color.yellow)#曲線

g=-9.8
t=0
dt=0.01
v=0

while b.pos.y>=1:
    t+=dt  #和 t=t+dt是一樣的
    v+=g*dt
    b.pos=(0,20+v,0)
    yt.plot(pos=(t,20+v)) #曲線的數據
    rate(100)
    
    
