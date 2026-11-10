"""Vérification numérique du chapitre 6 (logarithme népérien)."""
from math import log, exp, sqrt, e, ceil
print("ln2",log(2),"ln3",log(3),"ln5",log(5),"ln8",log(8),"3ln2",3*log(2),"ln10",log(10))
print("seuil 0.8^n<0.01 :", log(0.01)/log(0.8), next(n for n in range(100) if 0.8**n<0.01))
print("abonnés 0.8^n<0.1 :", log(0.1)/log(0.8))
print("doublement 1.03^n>=2 :", log(2)/log(1.03), next(n for n in range(100) if 1.03**n>=2))
print("e^x=5 ->",log(5)," ln x=2 ->",exp(2))
# inequation ln(2x-1) <= ln(x+3): domaine x>1/2 ; 2x-1<=x+3 -> x<=4
print("ineq ok", all((log(2*x-1)<=log(x+3))==(x<=4) for x in [0.6,1,3.9,4,4.1,10]))
# Briggs
def briggs(a,k=20):
    for i in range(k): a=sqrt(a)
    return 2**k*(a-1)
print("Briggs ln2 :",briggs(2),"k=10:",briggs(2,10))
# limites
for x in (1e-3,1e-6): print("x ln x",x,x*log(x))
for x in (1e3,1e6): print("ln x / x",x,log(x)/x)
print("ln(1+x)/x x=1e-6",log(1+1e-6)/1e-6)
# bac : g(x)=x ln x - x
g=lambda x:x*log(x)-x
print("g(1)",g(1),"g(e)",g(e),"g(0.001)",g(0.001))
# exos
print("ex1: ln(e^3)=3; e^{2 ln 3}=",exp(2*log(3)),"; ln(1/e^2)=-2 ; ln(sqrt e)=",log(sqrt(e)))
print("ex1 eq: e^{2x}=7 -> x=",log(7)/2,"; ln(x)+ln(x-1)=ln 6 -> x=3 :",log(3)+log(2),log(6))
# x^2-x-6=0 -> 3 or -2 ; domaine x>1 -> 3
print("ex2: 2^n>1000 n>", log(1000)/log(2), next(n for n in range(100) if 2**n>1000))
print("ex2: (1/2)^n<1e-3 -> n>", log(1e-3)/log(0.5))
print("ex2: 5e^{-0.2t}<1 -> t>", 5*log(5), "")
# f(x)=x - ln x min 1
f=lambda x:x-log(x); print("f min",f(1), min(f(0.01*k) for k in range(1,1000)))
# ln x <= x-1 check
print(all(log(x)<=x-1+1e-12 for x in [0.01*k for k in range(1,1000)]))
# demi-vie : N(t)=N0 e^{-lambda t}; carbone 14 lambda : T=5730 ans? avoid
print("ln(x^2+1)' at 2 :", (log(4.000001+1)-log(3.999999+1)), 2*2/5*2e-6/2e-6)
# CE 2026 f=ln x/x^2 : max at sqrt(e)
fx=lambda x:log(x)/x**2
print("CE2026 max x=sqrt(e)",sqrt(e),fx(sqrt(e)),1/(2*e), "inflexion e^{5/6}",exp(5/6))
# Metropole 2024 : f(x)=x^2+2x-1+ln(x+2) racine
F=lambda x:x*x+2*x-1+log(x+2)
a,b=-1.9,2
for i in range(60):
    m=(a+b)/2
    if F(a)*F(m)<=0: b=m
    else: a=m
print("Metropole 2024 alpha",a, "F(-1)",F(-1),"F(0)",F(0))
