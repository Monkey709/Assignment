from visual import*
from visual.graph import*
#��19��
d1=gdisplay(x=600,y=10,title='y-t',ytitle='y(m)',xtitle='t(s)')#�}�p��
floor=box(length=20,height=0.01,width=10,color=color.green)

b=sphere(pos=(0,20,0),radius=1,make_trail=true)#�y,make_trail=true �O�e�X�y��
yt=gcurve(display=d1,color=color.yellow)#���u

g=-9.8
t=0
dt=0.01
v=0

while b.pos.y>=1:
    t+=dt  #�M t=t+dt�O�@�˪�
    v+=g*dt
    b.pos=(0,20+v,0)
    yt.plot(pos=(t,20+v)) #���u���ƾ�
    rate(100)
    
    
