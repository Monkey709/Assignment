# -*- coding: cp950 -*-
while  True:
    print '��J�Q�i��G',
    x=input()
    b=[]
    d=[]
    while 0 <= x < 10**127 :
        a = x%2
        x=x/2
        b.append(a)
        if x<1:
            b.append('0b')
            print '�G�i��G' ,''.join(str(i) for i in b[::-1])
            break
        
    while -10**127 < x < 0:
        e = (x)%2
        x=(x+1)/2
        d.append(e)
        if 0 <= x <= 1:
            d.append('-0b')
            print '�G�i��G' ,''.join(str(j) for j in d[::-1])
            break
