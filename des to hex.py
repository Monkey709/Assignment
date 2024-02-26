# -*- coding: cp950 -*-
while  True:
    print '輸入十進制：',
    x=input()
    b=[]
    d=[]
    while 0 <= x < 10**127 :
        a = x%16
        if a >= 10:
            q=a-10
            a=chr(65+q)
        x=x/16
        b.append(a)
        if x<1:
            b.append('0x')
            print '十六進制為：' ,''.join(str(i) for i in b[::-1])
            break
    if x == -16:
        print '十六進制為：-0x10'
        continue
    while -10**127 < x < 0:
        e = 15-(x%16)
        x=x/16
        if e >= 9:
            f=e-10
            e=chr(65+f)
        if d == [] :
            if e >= 9:
                d.append(chr(66+f))
            else:
                d.append(e+1)
        else:
            d.append(e)
        if -1 <= x <= 1:
            d.append('-0x')
            print '十六進制為：' ,''.join(str(j) for j in d[::-1])
            break
