# -*- coding: cp936 -*-

from numpy import sqrt
from gaussint import gaussxwint
from Hermite import psi

def f(x):
    return (x/(1.-x**2))**2*((1.+x**2)/(1.-x**2)**2)*(abs(psi(5,x/(1.-x**2))))**2
    
print 'uncertainty =',sqrt(gaussxwint(f,-1.0,1.0,100))
'''
ԭ��1a,1b ����һ���n�� ���Import psi �� ȫ��߀�Ǖ�����
�����@�e����һ���^����1. a,b,c .
'''
