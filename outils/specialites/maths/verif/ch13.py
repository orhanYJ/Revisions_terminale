"""Vérification du chapitre 13 (épreuves indépendantes, loi binomiale)."""
from math import comb, log
def b(n,p,k): return comb(n,k)*p**k*(1-p)**(n-k)
def F(n,p,k): return sum(b(n,p,i) for i in range(0,k+1))
print("dé+pièce 1/12; RRB",3/5*3/5*2/5,"une bleue",3*0.144,"RR sans remise",3/5*2/4)
pT=0.02*0.95+0.98*0.10; print("test P(T)",pT,"P_T(M)",0.019/pT)
print("lancers francs",b(5,.7,3),b(5,.7,4),b(5,.7,5),b(5,.7,4)+b(5,.7,5))
print("QCM",b(10,.25,0),b(10,.25,5),1-F(10,.25,4))
print("seuil 0.9:",min(n for n in range(1,200) if 1-0.9**n>=0.99),log(0.01)/log(0.9))
print("[40,60]",F(100,.5,60)-F(100,.5,39),"[41,59]",F(100,.5,59)-F(100,.5,40))
print("AmSud",(1-F(20,.85,17))/(1-F(20,.85,14)))
print("Galton",[comb(6,k) for k in range(7)],20/64,1/64)
P=lambda k: 1-F(210,.95,k); print("surres",P(200),min(k for k in range(211) if P(k)<=0.05),min(k for k in range(211) if P(k)<=0.01))
print("anim p=.4",[b(3,.4,k) for k in range(4)],"3p2q",3*.16*.6)
# exos
print("exo1",b(8,.3,2),b(8,.3,0),1-b(8,.3,0),F(8,.3,3),F(8,.3,4)-F(8,.3,1),F(8,.3,4),F(8,.3,1))
print("exo2",.6*.4*.6,[b(3,.6,k) for k in range(4)])
print("exo3",.97**20,1-.97**20,log(.1)/log(.97),1-.97**75,1-.97**76)
print("exo4",.4*.25+.6*.5,.3/.4,b(15,.4,6),1-F(15,.4,7),F(15,.4,7))
pr=1-F(50,.02,2); print("exo5",b(50,.02,0),b(50,.02,1),F(50,.02,2),pr,1-(1-pr)**10,[(s,F(50,.02,s-1)) for s in (3,4,5)])
# annales
print("AmN 2026",.25*.45,.25*.45+.6*.3+.12,.25*.45/.4125,.5875**8,min(n for n in range(1,100) if 1-.5875**n>=.999))
print("Metro 2025",.10*.84,F(100,.0714,7),100*.0714,100*.0714*(1-.0714))
print("Asie 2026",[ (3*p*(1-p)**2, 3*p-6*p*p+3*p**3) for p in (.2,.7)])
