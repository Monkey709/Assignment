from visual import*
v1=vector(4,-3,0)
v2=vector(0,6,0)
v3=-(v1+v2)

arrow(axis=v1,shaftwidth=0.3,color=color.red)
arrow(pos=v1,axis=v2,shaftwidth=0.3,color=color.red)
arrow(pos=v1+v2,axis=v3,shaftwidth=0.3,color=color.red)

sphere(pos=v1,radius=0.5,color=color.green)
sphere(pos=v1+v2,radius=0.5,color=color.green)
sphere(radius=0.5,color=color.green)

print(v1)
print(v2)
print(v3)
