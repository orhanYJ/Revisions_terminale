"""Vérification numérique du chapitre 3 (limites de fonctions)."""
import math
f=lambda x:(2*x+1)/(x-1)
print("f(1.001)",f(1.001),"f(0.999)",f(0.999),"f(1e6)",f(1e6))
print("xe^-x x=20:",20*math.exp(-20))
for n in (1,2,3,5,10):
    a,b=n+0.01,200
    for i in range(200):
        m=(a+b)/2
        if math.exp(m)>m**n: b=m
        else: a=m
    print("dernier croisement e^x=x^%d :"%n, round(b,4), " max x^n e^-x =",(n/math.e)**n)
print("e^x > x^10 at 35.77?", math.exp(35.77)>35.77**10, math.exp(35.76)>35.76**10)
g=lambda x:(2*x-1)*math.exp(x)
print("bac: f(-1/2)=",g(-0.5)," -2e^{-1/2}=",-2*math.exp(-0.5), "f(-20)",g(-20))
print("(e^x-1)/x x=1e-6", (math.exp(1e-6)-1)/1e-6)
print("x^2 e^-x at 2", 4*math.exp(-2))
h=lambda x:(x*x+3*x)/(x*x-4)
print("h(2.001)",h(2.001),"h(1.999)",h(1.999),"h(-2.001)",h(-2.001),"h(-1.999)",h(-1.999),"h(1e6)",h(1e6))
k=lambda x: math.sqrt(x*x+x)-x
print("sqrt(x^2+x)-x at 1e6:",k(1e6))
print("e^x - x^3 at 30:", math.exp(30)-30**3)
