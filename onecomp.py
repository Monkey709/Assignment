# -*- coding: cp950 -*-
def onecomp(x,b,d,a,e,i,j):
    b=[]
    d=[]
    while 0 <= x <= 2**31:
        a = x%2
        x=x/2
        b.append(a)
        if x<1:
            g=int(''.join(str(i) for i in b[::-1]))               #字串數值化
            print '二進制為：' ,'0'+"{:0>31d}".format(g) #一直存在32個字符
            break
        
    while -2**31 < x < 0:
        e = (x)%2
        x=(x+1)/2                                                                    #-0.5在整數中除以2會進位但在正數中不會進位 所以加1使其相同
        d.append(1-e)
        if 0 <= x <= 1:
            d.append(1)
            f=int(''.join(str(i) for i in d[::-1]))
            print '二進制為：' ,'1'+"{:1>31d}".format(f)
            break
    return x


while True:
    print '輸入十進制：',
    c=input()
    b=[]
    d=[]
    x=onecomp(c,b,d,1,1,1,1)
