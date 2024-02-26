# -*- coding: cp950 -*-
while  True:
    print '輸入十進制：',
    x=input()
    b=[]
    d=[]
    if x ==0:
        print 0
    while 0 < x < 10**127 :
        a = x%8
        x=x/8
        b.append(a)
        if x<1:
            b.append('0')
            print '八進制為：' ,''.join(str(i) for i in b[::-1])
            break
        
    while -10**127 < x < 0:
        e = 7-(x%8)
        x=x/8
        if d==[]:
            d.append(e+1)
        else:
            d.append(e)
        if  -1 <= x <= 1:
            d.append('-0')
            print '八進制為：' ,''.join(str(j) for j in d[::-1])
            break
