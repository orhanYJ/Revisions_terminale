"""Vérification numérique du chapitre 7 (sinus et cosinus)."""
from math import sin, cos, pi, sqrt, isclose
# équations sur [-pi, pi]
def sols(f, a, n=200000):
    xs=[-pi+2*pi*i/n for i in range(n+1)]
    return [round((xs[i]+xs[i+1])/2,4) for i in range(n) if (f(xs[i])-a)*(f(xs[i+1])-a)<=0 and abs(f(xs[i])-a)<1e-3]
print("cos x=1/2 :", sorted(set(sols(cos,0.5))), pi/3)
print("sin x=sqrt2/2 :", sorted(set(sols(sin,sqrt(2)/2))), pi/4, 3*pi/4)
print("cos x=-sqrt3/2:", sorted(set(sols(cos,-sqrt(3)/2))), 5*pi/6)
# inéquation cos x <= 1/2 sur [-pi,pi]
print(all((cos(x)<=0.5)==(abs(x)>=pi/3-1e-12) for x in [-pi+2*pi*i/1000 for i in range(1001)]))
# limite sin x / x
print([sin(x)/x for x in (0.1,0.01,0.001)])
# rectangle demi-cercle
A=lambda t:2*sin(t)*cos(t); print("A(pi/4)",A(pi/4), max(A(pi/2*i/10000) for i in range(10001)))
# bac type f(x)=x+2cos x sur [0,2pi]
f=lambda x:x+2*cos(x)
print("f(0)",f(0),"f(pi/6)",f(pi/6),pi/6+sqrt(3),"f(5pi/6)",f(5*pi/6),5*pi/6-sqrt(3),"f(2pi)",f(2*pi))
# exo dérivées verif numérique
def d(g,x,h=1e-6): return (g(x+h)-g(x-h))/(2*h)
from math import exp
tests=[(lambda x:sin(3*x+1),lambda x:3*cos(3*x+1)),(lambda x:cos(x)**2,lambda x:-2*sin(x)*cos(x)),(lambda x:exp(-x)*cos(x),lambda x:-exp(-x)*(cos(x)+sin(x))),(lambda x:sin(x**2),lambda x:2*x*cos(x**2)),(lambda x: x*sin(x), lambda x: sin(x)+x*cos(x))]
print([round(d(a,0.7)-b(0.7),7) for a,b in tests])
# pi par dichotomie : zéro de cos sur [1,2]
a,b=1.0,2.0
for i in range(40):
    m=(a+b)/2
    if cos(a)*cos(m)<=0: b=m
    else: a=m
print("pi ~",2*a, pi)
# exo : 2 sin x - 1 >= 0 sur [0,2pi] -> [pi/6, 5pi/6]
print(all((2*sin(x)-1>=0)==(pi/6-1e-12<=x<=5*pi/6+1e-12) for x in [2*pi*i/997 for i in range(998)]))
# Asie 2026 g(x)=x cos x - sin x ; g'(x) = -x sin x ; g(pi) = -pi ; g(2pi)=2pi
g=lambda x:x*cos(x)-sin(x); print("g(0)",g(0),"g(pi)",g(pi),"g(2pi)",g(2*pi), "g'(1)",d(g,1),-1*sin(1))
# e^x sin x Amérique 2025
