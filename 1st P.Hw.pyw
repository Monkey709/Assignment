# -*- coding: cp950 -*-
from visual import*
x=vector(1,0,0)
y=vector(0,1,0)
z=vector(0,0,1)
v1=vector(4,-3,0)
v2=vector(0,6,0)
v4=vector(0,9,0)
v5=vector(4,-3,24)

arrow(axis=v1,shaftwidth=0.3,color=color.green)
arrow(axis=v2,shaftwidth=0.3,color=color.red)
arrow(axis=x,length=7,shaftwidth=0.1,color=color.white)
arrow(axis=y,length=7,shaftwidth=0.1,color=color.white)
arrow(axis=z,length=7,shaftwidth=0.1,color=color.white)

arrow(axis=v4,shaftwidth=0.3,color=color.yellow)
arrow(axis=v5,shaftwidth=0.3,color=color.orange)

label(pos=(7.5,0,0),axis=x,text='x')
label(pos=(0,7.5,0),axis=y,text='y')
label(pos=(0,0,7.5),axis=z,text='z')
label(pos=(0,9.5,0),axis=v4,text='inner(yellow)')
label(pos=(4.5,-3,24),axis=v5,text='outer')

print(v1)
print(v2)
print(v4)
print(v5)
print"組員：李豪盛 4106054025，林子喬 4106054019，曾智詮 4106054028"
