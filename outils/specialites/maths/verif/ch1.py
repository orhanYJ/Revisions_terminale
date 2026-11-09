"""Vérification des résultats numériques du chapitre 1 (récurrence)."""
from fractions import Fraction as Fr
import math
# Cours : u0=1, u_{n+1}=2u_n+3 -> u_n = 2^(n+2)-3
u=1
for n in range(30):
    assert u==2**(n+2)-3; u=2*u+3
print("u_n=2^(n+2)-3 ok ; u_5 =", 2**7-3)
# somme des impairs
for n in range(1,200): assert sum(2*k-1 for k in range(1,n+1))==n*n
for n in range(1,200): assert sum(k*k for k in range(1,n+1))==n*(n+1)*(2*n+1)//6
# sqrt(u+2), u0=1
u=1.0; L=[u]
for n in range(8): u=math.sqrt(u+2); L.append(u)
print("racine(u+2):", [round(x,4) for x in L])
# Euler n^2+n+41
def premier(p): return p>1 and all(p%d for d in range(2,int(p**.5)+1))
print("Euler: premier n non premier:", next(n for n in range(100) if not premier(n*n+n+41)), 40*40+40+41, 41*41)
# 4^n-1 divisible par 3
assert all((4**n-1)%3==0 for n in range(100))
# Ex1 : u0=2, u_{n+1}=u_n+2n+3 -> (n+1)^2+1
u=2
for n in range(50): assert u==(n+1)**2+1; u=u+2*n+3
print("ex1 ok, u_3 =",(3+1)**2+1, " u_10 =",11**2+1)
# Ex2 : somme k(k+1)
for n in range(1,100): assert sum(k*(k+1) for k in range(1,n+1))==n*(n+1)*(n+2)//3
print("ex2 n=3 :", sum(k*(k+1) for k in range(1,4)), 3*4*5//3)
# Ex3 : u0=0, u_{n+1}=sqrt(3u_n+4)
u=0.0; L=[u]
for n in range(10): u=math.sqrt(3*u+4); L.append(u)
print("ex3:", [round(x,4) for x in L])
# Ex4 : 2^n >= n^2 pour n>=4
print("ex4:", [(n,2**n,n*n) for n in range(0,7)])
assert all(2**n>=n*n for n in range(4,500)); print("k^2-2k-1>=0 dès k>=", next(k for k in range(10) if k*k-2*k-1>=0), 1+math.sqrt(2))
# Ex5 : a0=5, a_{n+1}=0.8a_n+3
a=Fr(5); A=[a]
for n in range(15): a=Fr(4,5)*a+3; A.append(a)
for n,x in enumerate(A): assert x==15-10*Fr(4,5)**n
print("ex5:", [float(x) for x in A[:4]], "a_10=",round(float(A[10]),4),"a_11=",round(float(A[11]),4))
print("0.8^10=",0.8**10,"0.8^11=",0.8**11)
n=0;a=5
while a<=14: a=0.8*a+3; n+=1
print("seuil a_n>14 : n =",n)
# Bernoulli check
for a in [0,0.1,1,2.5]:
    for n in range(30): assert (1+a)**n>=1+n*a-1e-9
print("Bernoulli ok ; 1.05^20 =",1.05**20," 1+20*0.05 =",1+20*0.05)
