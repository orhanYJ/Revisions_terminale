"""Vérification du chapitre 15 (concentration, loi des grands nombres)."""
from math import lgamma, log, exp, sqrt, ceil
from fractions import Fraction as F
def pmf(n,p,k): return exp(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)+k*log(p)+(n-k)*log(1-p))
def P(n,p,cond): return sum(pmf(n,p,k) for k in range(n+1) if cond(k))
print("dé",F(2,6),F(35,12)/4,float(F(35,48)))
print("B(100,.5) |X-50|>=5,10,15",[P(100,.5,lambda k,d=d:abs(k-50)>=d) for d in (5,10,15)],"bornes",[25/d**2 for d in (5,10,15)])
print("AmN 2026",1-4/9)
print("dé n=100",(35/12)/(100*.25),1-(35/12)/25)
print("sondage",0.25/(0.05*0.05**2),"exact n=1000",P(1000,.5,lambda k:abs(k/1000-.5)>=0.05-1e-12))
print("Metro 2026",1728/36,48/0.15,"Metro 2025",6.63/(0.05*0.14**2),ceil(6.63/(0.05*0.14**2)))
print("piece n=1e4",.25/(1e4*1e-4),"exact",P(10000,.5,lambda k:abs(k/10000-.5)>=0.01-1e-12),"n=1e6",.25/(1e6*1e-4))
print("Etranger 2025",20*.165,20*.165*.835,3*20*.165*.835,1-3*20*.165*.835/16)
print("exo1",4/25,1-4/16,4/1)
x=P(40,.5,lambda k:k<=14); print("exo2",10/36,x,2*x,10/36/(2*x))
print("exo3",.25/(1000*.0025),.25/(25000*.0001))
print("exo4",1-16/100,16/25,1-0.64/4,16/0.05)
print("exo5",20*.15,20*.15*.85,1-2.55/9,P(20,.15,lambda k:1<=k<=5),2.55/0.25,10.2/0.01)
print("anim: borne 100/n",100/50,100/500)
