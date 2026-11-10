"""Vérification du chapitre 14 (sommes de variables aléatoires)."""
from fractions import Fraction as F
from math import sqrt, comb
de={k:F(1,6) for k in range(1,7)}
E=lambda L: sum(k*p for k,p in L.items()); V=lambda L: sum(k*k*p for k,p in L.items())-E(L)**2
def somme(A,B):
    r={}
    for a,pa in A.items():
        for b,pb in B.items(): r[a+b]=r.get(a+b,0)+pa*pb
    return r
S=somme(de,de); print("dé",E(de),V(de),"E(X^2)",sum(k*k*p for k,p in de.items()),"S",E(S),V(S),"E(S^2)",sum(k*k*p for k,p in S.items())*36,"/36")
print("P(S=7)",S[7],"P(S=10)",S[10],"P(S<=4)",S[2]+S[3]+S[4])
D=somme(de,{-k:p for k,p in de.items()}); print("D",E(D),V(D))
print("sans remise 1,2,3",[a+b for a in (1,2,3) for b in (1,2,3) if a!=b])
print("Asie: E(Y)",1.5*2.5-5,"V(Y)",2.25*10*.25*.75)
print("urne simultanee",F(1,10),F(6,10),F(3,10),F(6,10)+2*F(3,10))
X={0:F(19,100),70:F(6,100),100:F(51,100),170:F(24,100)}; print("Metro 2026",E(X),V(X),F(6,10)*(E(X)+104),F(36,100)*(V(X)+1686))
L={-2:F(1,10),-1:F(4,10),2:F(3,10),5:F(2,10)}; print("AmSud",somme(L,L)[4])
print("B(100,.0714)",100*.0714*.9286,sqrt(100*.0714*.9286))
print("10 dés",10*3.5,"sigma de",sqrt(35/12),"M100",sqrt(35/12)/10,"sondage",sqrt(.25/1000))
print("exo1",3*5-1,9*4,5-2,4+9,sqrt(13),10+6,4*4+9*9)
G={8:F(1,6),-2:F(5,6)}; print("exo3",E(G),V(G),float(V(G)),50*E(G),float(50*V(G)),sqrt(50*V(G)),"via N",F(500,6)-100,100*50*F(1,6)*F(5,6))
print("exo4",0.6+0.4*0.25,20*.7,20*.7*.3,sqrt(4.2),1.25*14-5,1.25**2*4.2)
X5={2:F(4,10),5:F(3,10),10:F(2,10),20:F(1,10)}; v=V(X5); print("exo5",E(X5),v,float(v),E(X5)+F(1,2),v+F(1,4),float((v+F(1,4))/F(1,4)))
for n in (1,2,4,16,64): print("sigma M",n,sqrt(35/12)/sqrt(n))
