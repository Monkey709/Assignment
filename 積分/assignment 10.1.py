# -*- coding: cp936 -*-

from numpy import sqrt
from gaussint import gaussxwint
from Hermite import psi

def f(x):
    return (x/(1.-x**2))**2*((1.+x**2)/(1.-x**2)**2)*(abs(psi(5,x/(1.-x**2))))**2
    
print 'uncertainty =',sqrt(gaussxwint(f,-1.0,1.0,100))
'''
原本1a,1b 另外一個檔案 因為Import psi 後 全部還是會執行
所以這裡可以一次過看完1. a,b,c .
'''
