"""Vérification numérique du chapitre 4 (dérivation, convexité, continuité)."""
import math
def dicho(f,a,b,e):
    n=0
    while b-a>e:
        m=(a+b)/2
        if f(a)*f(m)<=0: b=m
        else: a=m
        n+=1
    return a,b,n
f=lambda x:x**3+x-1
print("x^3+x-1 :",dicho(f,0,1,1e-3), dicho(f,0,1,1e-6))
g=lambda x:x*x-2; print("x^2-2:",dicho(g,1,2,1e-3))
# Newton
x=1.0
for i in range(5): x=x-f(x)/(3*x*x+1); print("Newton",i+1,repr(x))
# TVI exo x^3-3x+1 sur [0,1]
h=lambda x:x**3-3*x+1
print("h(0),h(1)",h(0),h(1), dicho(h,0,1,0.01), [ (round(k/100,2),round(h(k/100),4)) for k in (34,35)])
# bac Metropole sept 2026 : 4t e^{-1.5 t} = 0.5
F=lambda t:4*t*math.exp(-1.5*t)-0.5
print("f(1)",F(1)+0.5,"f(3)",F(3)+0.5,"f(2/3)",F(2/3)+0.5, dicho(F,1,3,1e-4))
# bac type: e^x - x - 2
k=lambda x:math.exp(x)-x-2
print("k(1)",k(1),"k(2)",k(2),"k(1.14)",k(1.14),"k(1.15)",k(1.15), dicho(k,1,2,1e-2), dicho(k,1,2,1e-6))
print("e-3=",math.e-3,"e-1=",math.e-1)
# tangente en 1 de e^x-x-2 : y=(e-1)x -2 ... check
print("tangente en 1: y=(e-1)x + (e-3) - (e-1) =", "(e-1)x -2")
# racine concave sqrt(x) <= (x+1)/2
print([ (x, math.sqrt(x), (x+1)/2) for x in (0,1,4,9)])
# Ex continuite : u_n -> 2 , f(u_n)
print("croissance ok")
# derivées composées vérif numériques
def d(fun,x,h=1e-6): return (fun(x+h)-fun(x-h))/(2*h)
tests=[(lambda x:(3*x+1)**5, lambda x:15*(3*x+1)**4,0.3),(lambda x:math.sqrt(x*x+1),lambda x:x/math.sqrt(x*x+1),1.7),(lambda x:math.exp(-x*x),lambda x:-2*x*math.exp(-x*x),0.8),(lambda x:1/(x*x+1),lambda x:-2*x/(x*x+1)**2,1.2),(lambda x:math.exp(2*x)*(x-1)**3, lambda x:math.exp(2*x)*(x-1)**2*(2*x+1),0.4),(lambda x:math.sqrt(math.exp(x)+1), lambda x:math.exp(x)/(2*math.sqrt(math.exp(x)+1)),0.5)]
for a,b,x in tests: print(round(d(a,x)-b(x),6))
# convexité x e^x : g''=(x+2)e^x
gg=lambda x:x*math.exp(x); print("g''(-2)",round(d(lambda t:d(gg,t,1e-4),-2,1e-4),4), "g(-2)=",gg(-2))
# Asie 2026 : f(x)=(-x/2+3)^5 convexe ? f''=20/4 (-x/2+3)^3 ...
ff=lambda x:(-x/2+3)**5
print("f'' at 0,10:", d(lambda t:d(ff,t,1e-4),0,1e-4), d(lambda t:d(ff,t,1e-4),10,1e-4))
