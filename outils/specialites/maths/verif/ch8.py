"""Vérification numérique du chapitre 8 (primitives, équations différentielles)."""
from math import exp, log, sqrt, sin, cos, pi
def d(g,x,h=1e-6): return (g(x+h)-g(x-h))/(2*h)
# primitives : F' = f en quelques points
P=[("3x^2+2x-5", lambda x:x**3+x**2-5*x, lambda x:3*x*x+2*x-5),
   ("1/x^2", lambda x:-1/x, lambda x:1/x**2),
   ("1/sqrt x", lambda x:2*sqrt(x), lambda x:1/sqrt(x)),
   ("e^{3x}", lambda x:exp(3*x)/3, lambda x:exp(3*x)),
   ("2x e^{x^2}", lambda x:exp(x*x), lambda x:2*x*exp(x*x)),
   ("2x/(x^2+1)", lambda x:log(x*x+1), lambda x:2*x/(x*x+1)),
   ("cos(2x)", lambda x:sin(2*x)/2, lambda x:cos(2*x)),
   ("x(x^2+1)^3", lambda x:(x*x+1)**4/8, lambda x:x*(x*x+1)**3),
   ("sin x cos x", lambda x:sin(x)**2/2, lambda x:sin(x)*cos(x)),
   ("1/(2x+1)", lambda x:log(2*x+1)/2, lambda x:1/(2*x+1)),
   ("x/sqrt(x^2+1)", lambda x:sqrt(x*x+1), lambda x:x/sqrt(x*x+1)),
   ("e^{0.2x}/(1+e^{0.2x})", lambda x:5*log(1+exp(0.2*x)), lambda x:exp(0.2*x)/(1+exp(0.2*x))),
   ("ln x", lambda x:x*log(x)-x, lambda x:log(x)),
   ("1/x^3",lambda x:-1/(2*x*x),lambda x:1/x**3)]
for n,F,f in P: print(n, round(d(F,1.3)-f(1.3),7))
# y' = -0.5 y + 1 : y = 2 + C e^{-0.5x}
for y0 in (0,4): 
    C=y0-2; g=lambda x:2+C*exp(-0.5*x); print("y0",y0,"résidu",round(d(g,1.1)-(-0.5*g(1.1)+1),7), "y(4)",g(4))
# refroidissement T' = -0.1(T-20), T(0)=90
T=lambda t:20+70*exp(-0.1*t); print("T(10)",T(10),"T<30 : t>",10*log(7), "T(19.46)",T(10*log(7)))
# Euler y'=y, y(0)=1, h=0.1 -> y(1)
y=1;h=0.1
for i in range(10): y=y+h*y
print("Euler e:",y,(1.1)**10, exp(1))
y=1;h=0.01
for i in range(100): y=y+h*y
print("Euler h=0.01:",y)
# Euler pour y'=-0.5y+1, y(0)=0, h=0.5 jusqu'à 4
y=0;L=[0]
for i in range(8): y=y+0.5*(-0.5*y+1); L.append(round(y,4))
print("Euler y'=-0.5y+1:",L, "exact y(4)=",2-2*exp(-2))
# bac : Metropole 2026 v' = -0.005 v + 6 ; v(t)=1200(1-e^{-0.005 t}); v>50 -> t > -200 ln(1-50/1200)
t=-200*log(1-50/1200); print("v>50 : t=",t, int(t),"h", round((t-int(t))*60),"min")
print("5% de 30000 =",0.05*30000," limite 1200 < 1500")
# Metropole 2026 J1 : T' = -0.035T+0.91 ; T=26-8e^{-0.035t} ; T=20 -> t=ln(4/3)/0.035 dizaines de minutes
t=log(4/3)/0.035; print("T=20 à t=",t,"dizaines de min soit",t*10,"min =",int(t*10//60),"h",round(t*10%60),"min")
# Métropole 2025 J2 : y'+0.6y = e^{-0.6t}, g = t e^{-0.6t}
g=lambda t:t*exp(-0.6*t); print("résidu g", round(d(g,1.7)+0.6*g(1.7)-exp(-0.6*1.7),7))
v=lambda t:(12+t)*exp(-0.6*t); print("v(0)",v(0))
# exo : y'=3y, y(0)=2 -> 2e^{3x}; y'=-2y+6 y(0)=1 -> 3-2e^{-2x}
f=lambda x:3-2*exp(-2*x); print("résidu", round(d(f,0.4)-(-2*f(0.4)+6),7), f(0))
# exo croissance bactérie : N'=0.7N , N(0)=100 -> doublement ln2/0.7
print("doublement",log(2)/0.7, "N(5)",100*exp(3.5))
# y' = 2y - 5 ; h = -3/2 e^{2x}+5/2 ; h(0)=1 (Polynésie 2026 aff 4)
hh=lambda x:-1.5*exp(2*x)+2.5; print("h(0)",hh(0),"résidu",round(d(hh,0.3)-(2*hh(0.3)-5),7))
