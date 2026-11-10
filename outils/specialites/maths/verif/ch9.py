"""Vérification numérique du chapitre 9 (calcul intégral)."""
from math import exp, log, sin, cos, pi, e, sqrt
import random
def rect(f,a,b,n,mode="g"):
    h=(b-a)/n
    if mode=="g": return sum(f(a+i*h) for i in range(n))*h
    if mode=="d": return sum(f(a+(i+1)*h) for i in range(n))*h
    if mode=="m": return sum(f(a+(i+0.5)*h) for i in range(n))*h
    if mode=="t": return sum((f(a+i*h)+f(a+(i+1)*h))/2 for i in range(n))*h
sq=lambda x:x*x
for n in (4,8,16,100): print("x^2 n=",n, rect(sq,0,1,n,"g"), rect(sq,0,1,n,"d"), rect(sq,0,1,n,"m"), rect(sq,0,1,n,"t"))
print("exact 1/3")
# exemples
print("int_0^pi sin =",2, "moyenne", 2/pi)
print("int_1^e ln =",1, "int_0^1 x e^x =",1)
print("int_0^1 e^x =",e-1)
print("int_1^2 1/x =",log(2), rect(lambda x:1/x,1,2,1000,"m"))
# aire entre x et x^2 sur [0,1] = 1/6
print("aire entre", 1/2-1/3)
# I_n = int_0^1 x^n/(1+x)
def I(n): return rect(lambda x:x**n/(1+x),0,1,20000,"m")
print("I0",I(0),log(2),"I1",I(1),1-log(2),"I0+I1",I(0)+I(1))
for n in range(5): print(n, I(n)+I(n+1), 1/(n+1))
# Brouncker : ln 2 = sum 1/((2k-1)(2k))
s=0
for k in range(1,1001): s+=1/((2*k-1)*(2*k))
print("Brouncker 1000 termes",s, log(2))
# Monte-Carlo
random.seed(1); N=100000
c=sum(1 for i in range(N) if random.random()**2>random.random()*1)  # placeholder
random.seed(2026); c=0
for i in range(N):
    x=random.random(); y=random.random()
    if y<=x*x: c+=1
print("MC x^2:",c/N)
# exos
print("int_0^2 (3x^2-2x+1) =", 8-4+2)
print("int_0^1 e^{2x} =", (exp(2)-1)/2)
print("int_0^{pi/2} cos =",1)
print("int_1^4 1/sqrt x =", 2*2-2*1)
print("int_0^1 x/(x^2+1) =", log(2)/2)
print("IPP int_0^pi x sin x =", pi, rect(lambda x:x*sin(x),0,pi,10000,"m"))
print("IPP int_1^e x ln x =", (e*e+1)/4, rect(lambda x:x*log(x),1,e,10000,"m"))
print("IPP int_0^1 x e^{-x} =", 1-2/e, rect(lambda x:x*exp(-x),0,1,10000,"m"))
# valeur moyenne de f(t)=20+70e^{-0.1t} sur [0,10]
m=(200+700*(1-exp(-1)))/10; print("moyenne café [0,10]",m, rect(lambda t:20+70*exp(-0.1*t),0,10,10000,"m")/10)
# CE 2025 : valeur moyenne de 1/(1+e^{-0.2x}) sur [0,40] = (5ln(1+e^8)-5ln2)/40
print("moyenne CE 2025", (5*log(1+exp(8))-5*log(2))/40)
# CE 2026 : I_n = (n-1-ln n)/n ; I_10
In=lambda n:(n-1-log(n))/n; print("I_10",In(10), rect(lambda x:log(x)/x**2,1,10,100000,"m"))
S=1/(2*exp(1))
for i in range(2,10): S+=log(i+0.5)/(i+0.5)**2
print("CE2026 script rectangles ?",S)
# Amérique 2025 I=int_0^{pi/2} e^x sin x = (e^{pi/2}+1)/2
print("Am 2025 I", rect(lambda x:exp(x)*sin(x),0,pi/2,10000,"m"), (exp(pi/2)+1)/2)
# bac type : f(x)=x e^{-x} sur [0,3], F=-(x+1)e^{-x}, aire = 1-4e^{-3}
print("bac aire", 1-4*exp(-3), rect(lambda x:x*exp(-x),0,3,10000,"m"))
print("moyenne", (1-4*exp(-3))/3)
