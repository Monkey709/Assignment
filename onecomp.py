# -*- coding: cp950 -*-
def onecomp(x,b,d,a,e,i,j):
    b=[]
    d=[]
    while 0 <= x <= 2**31:
        a = x%2
        x=x/2
        b.append(a)
        if x<1:
            g=int(''.join(str(i) for i in b[::-1]))               #�r��ƭȤ�
            print '�G�i��G' ,'0'+"{:0>31d}".format(g) #�@���s�b32�Ӧr��
            break
        
    while -2**31 < x < 0:
        e = (x)%2
        x=(x+1)/2                                                                    #-0.5�b��Ƥ����H2�|�i����b���Ƥ����|�i�� �ҥH�[1�Ϩ�ۦP
        d.append(1-e)
        if 0 <= x <= 1:
            d.append(1)
            f=int(''.join(str(i) for i in d[::-1]))
            print '�G�i��G' ,'1'+"{:1>31d}".format(f)
            break
    return x


while True:
    print '��J�Q�i��G',
    c=input()
    b=[]
    d=[]
    x=onecomp(c,b,d,1,1,1,1)
