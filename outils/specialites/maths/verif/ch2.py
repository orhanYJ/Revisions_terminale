"""Vérification des résultats numériques du chapitre 2 (limites de suites)."""
from fractions import Fraction as Fr
import math
# Exercice type bac : u0=0, u_{n+1}=(2u+3)/(u+4)
u=Fr(0); v=lambda u:(u-1)/(u+3)
for n in range(12):
    if n<4: print("u",n,u,float(u), "v=",v(u))
    assert v(u)==Fr(-1,3)*Fr(1,5)**n
    u=(2*u+3)/(u+4)
u=0.0;n=0
while abs(u-1)>=1e-6: u=(2*u+3)/(u+4); n+=1
print("seuil |u_n-1|<1e-6 : n =",n)
for n in range(12): print(n, abs((1+3*(-1/3)*0.2**n)/(1-(-1/3)*0.2**n)-1))
# exemple cours
f=lambda n:(3*n*n-n+1)/(2*n*n+5); print("ex cours", f(10), f(1000))
print("conjugué", math.sqrt(10**6+1)-math.sqrt(10**6))
# geom
print("0.9^n seuil <0.01:", next(n for n in range(1000) if 0.9**n<0.01))
print("1.02^n > 2 :", next(n for n in range(1000) if 1.02**n>2), " >100:", next(n for n in range(10000) if 1.02**n>100))
print("Bernoulli : 1+0.02n >= 100 pour n>=", math.ceil(99/0.02))
# sommes
print("somme 1/2^k k=1..10", sum(0.5**k for k in range(1,11)))
# approximations
u=1.0
for i in range(5): u=(u+2/u)/2; print("Heron",i+1,repr(u))
print(math.sqrt(2))
s=0; t=1
for k in range(0,11): s+=t; t/=(k+1)
print("e somme 1/k! k<=10:", s, math.e)
print("(1+1/n)^n n=1000:", (1+1/1000)**1000)
u=1.0
for i in range(20): u=1+1/u
print("phi:",u,(1+5**.5)/2)
# exos
g=lambda n:(n**3-2*n)/(4*n**3+n**2); print("exo a", g(10**4))
print("exo b", [ (2*n+1)/(n*n+1) for n in (10,100)])
