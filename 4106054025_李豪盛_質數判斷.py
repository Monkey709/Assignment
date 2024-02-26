print ('ID: 4106054025')

for x in range(2,10001,1):
    for y in range(2,x-1,1):
        if x%y == 0:
            break
    else:
        print x,

