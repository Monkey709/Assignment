from visual import*
from numpy import pi,sqrt,sin,cos

w=display(x=1000,title = ' table tennis ' , autocenter = True  ,forward = (-1,-1,-5),height = 1000,width = 1000)
pp=sphere(pos=(0.38,0.25,0.6),radius=0.02,make_trail=true,color=color.yellow,retain = 150)
table=box(pos=(1.75,0,0),length=2.74,height=0.009,width=1.525,color=color.blue)
box(pos=(1.75,0,0),length=2.74,height=0.01,width=0.02,color=color.white)
box(pos=(1.75,0,0.7625),length=2.74,height=0.01,width=0.02,color=color.white)
box(pos=(1.75,0,-0.7625),length=2.74,height=0.01,width=0.02,color=color.white)
box(pos=(3.12,0,0),length=0.02,height=0.01,width=1.525,color=color.white)
box(pos=(0.38,0,0),length=0.02,height=0.01,width=1.525,color=color.white)
box(pos=(1.75,0,0),length=0.02,height=0.01,width=1.525,color=color.white)
wall1=box(pos=(3.5,0,0),length=0.01,height=0.4,width=1.525,color=color.white)
wall2=box(pos=(-0.2,0,0),length=0.01,height=0.4,width=1.525,color=color.white)
net = box(pos=(1.75,0.077,0) , length = 0.01, height = 0.1525 , width = 1.525,opacity = 0.3 )
box(pos = (0.6,-0.38,0.5) , length = 0.05 , height = 0.76, width = 0.05,color = (0,1,1) )
box(pos = (0.6,-0.38,-0.5) , length = 0.05 , height = 0.76, width = 0.05 ,color = (0,1,1))
box(pos = (2.8,-0.38,0.5) , length = 0.05 , height = 0.76, width = 0.05 ,color = (0,1,1))
box(pos = (2.8,-0.38,-0.5) , length = 0.05 , height = 0.76, width = 0.05 ,color = (0,1,1))
ppp =cylinder(pos=(0.3,0.27,0.6) , axis=(0.01,0,-0.002),radius =0.05,color = color.red)

while True:
    t=0
    dt=0.0005
    r = 0.02           #(m)
    c = 0.5
    den = 1.169   #(kg/m**3)
    A = pi*r**2      #m**2
    m = 2.7e-3     #(kg)
    def f(v):   return -c*den*A*v/(2*m)
    i=input('numbers of turns per sec :')                          # numbers of turns/sec
    j=input('hit angle(suggest :90 to 120) :')

    theta = j*pi/180.
    v0 = input('X-axis initial velocity(m/s) :')
    vx = v0*sin(theta)
    vy = v0*cos(theta)
    ii = input('input -1(top spin) or 1(down spin) :')
    x0 = 0.38
    y0 = 0.6
    z0 = 0.25 #(m)
    a0 = f(v0)
    omega = i*2*pi*dt         #angular rate
    xv0 = vx
    yv0 = vy
    g = -9.8
    zv0 = input('Y-axis initial velocity(m/s) :')
    cor =1
    av = omega*r                                   #angular velocity
    if i > 100 :
        pp.color = color.red
    else :
        pp.color = color.yellow
    while t<2 :
        rate(500)
        
        #x component
        xa0 = a0*sin(theta)
        xv1 = xv0+xa0*dt
        x1 = x0+xv0*dt
        xv0=xv1;x0=x1
    
        #y component
        ya0 = a0*cos(theta)
        yv1 = yv0+ya0*dt
        y1 = y0+yv0*dt
        yv0=yv1;y0=y1
    
        #z component
        #g = -9.8
        zv1 = zv0+g*dt
        z1 = z0+zv1*dt
        zv0=zv1;z0=z1
        if x1 >= wall1.pos.x :
            xv0 = -abs(xv0)
        if 0 < z1 <= 0.022 :
            xv0 -= 0.3*av*ii
            zv0 = cor*abs(zv0)
        if z1 <= 0 :
            z1 = 0
        v = sqrt(xv0**2+yv0**2)
        a0 = f(v)
        F=16*r**5*(pi*omega*den*v)**2
        
        print F
        g=g+ii*abs(F/m)
        if z1 <= 0.022 :
            cor = 0.9054*cor                            #for coefficient of restitution = 0.9054
            if cor == 0.9054**3:                       #maximum 4 times pingpong touch table
                print 3.12 - x1
                break
        if 1.73 < round(x1,2) < 1.77:
            if z1 < 0.1525:
                break
        t+=dt
        pp.pos=(x1,z1,y1)
        ppp.pos=(x1,z1,y1)
        if t > 0.005 :
            ppp.pos =(0.2,0.27,0.5)
    print t
