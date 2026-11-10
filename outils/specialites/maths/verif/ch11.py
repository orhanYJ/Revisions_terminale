"""Vérification du chapitre 11 (orthogonalité et distances dans l'espace)."""
from fractions import Fraction as F
from math import sqrt, acos, degrees
def v(A,B): return tuple(B[i]-A[i] for i in range(3))
def sc(u,w): return sum(u[i]*w[i] for i in range(3))
def no(u): return sqrt(sc(u,u))
def proj_droite(M,A,u):
    t=F(sc(v(A,M),u),sc(u,u)); return t,tuple(A[i]+t*u[i] for i in range(3))
A,B,C,D,E,G,H=(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,1,1),(0,1,1)
Fp=(1,0,1)
print("AC.AF",sc(v(A,C),v(A,Fp)),"AC,AF,CF",no(v(A,C)),no(v(A,Fp)),no(v(C,Fp)))
print("AG.BH",sc(v(A,G),v(B,H)),"angle",degrees(acos(1/3)),"BAG",degrees(acos(1/sqrt(3))))
print("AB pour A(1,2,-1)B(3,0,1)",no((2,-2,2)),2*sqrt(3))
print("AG.BD",sc(v(A,G),v(B,D)),"AG.BE",sc(v(A,G),v(B,E)),"AG.DE",sc(v(A,G),v(D,E)))
print("AE.BC",sc(v(A,E),v(B,C)))
print("proj B sur AG",proj_droite(B,A,(1,1,1)),"BH",sqrt((2/3)**2+2*(1/3)**2),sqrt(6)/3)
# proj A sur BDE : plan x+y+z=1
print("dist A a BDE",1/sqrt(3),sqrt(3)/3)
print("volume ABDE",F(1,3)*F(1,2)*1,"via BDE", (1/3)*(sqrt(3)/4*2)*(sqrt(3)/3))
# plan médiateur [BH] : six milieux
mil=lambda P,Q: tuple(F(P[i]+Q[i],2) for i in range(3))
for P in (mil(A,B),mil(B,C),mil(C,G),mil(G,H),mil(H,E),mil(E,A)):
    assert sc(v(P,D),v(P,D))==sc(v(P,Fp),v(P,Fp)), P
print("six milieux equidistants de D et F : OK")
# OABC
A2,B2,C2,n=(2,0,0),(0,3,0),(0,0,6),(3,2,1)
print("n.AB",sc(n,v(A2,B2)),"n.AC",sc(n,v(A2,C2)),"AB.AC",sc(v(A2,B2),v(A2,C2)))
t=F(6,14); H2=tuple(t*x for x in n); print("t",t,"H",H2,"OH",float(t)*no(n),3*sqrt(14)/7)
cosA=4/(sqrt(13)*sqrt(40)); aire=0.5*sqrt(13)*sqrt(40)*sqrt(1-cosA**2); print("aire ABC",aire,3*sqrt(14),"V",F(1,3)*3*6,"aire via V",3*6/(3*sqrt(14)/7))
# exo1
u,w=(2,-1,3),(1,5,1); print("exo1",sc(u,w),no(u),no(v((1,0,2),(4,-2,8))))
# exo2 pavé
Cp,Fp2,Gp=(4,3,0),(4,0,2),(4,3,2); print("exo2 AG",no(Gp),"AC.AF",sc(Cp,Fp2),"cos",sc(Cp,Fp2)/(no(Cp)*no(Fp2)),"angle",degrees(acos(sc(Cp,Fp2)/(no(Cp)*no(Fp2)))))
# exo3
A3,B3,C3,D3=(1,1,0),(3,0,1),(0,2,2),(4,6,-1)
AB3,AC3,AD3=v(A3,B3),v(A3,C3),v(A3,D3)
print("exo3",AD3,sc(AD3,AB3),sc(AD3,AC3),"AD",no(AD3),sqrt(35),"AB.AC",sc(AB3,AC3),no(AB3),no(AC3))
cA=sc(AB3,AC3)/(no(AB3)*no(AC3)); ar=0.5*no(AB3)*no(AC3)*sqrt(1-cA**2); print("aire",ar,sqrt(35)/2,"V",ar*no(AD3)/3,35/6)
# exo4
t,Hq=proj_droite((5,3,6),(1,0,-1),(2,1,2)); print("exo4 t",t,"H",Hq,"HM",v(Hq,(5,3,6)),"dist",no(v(Hq,(5,3,6))),sqrt(41)/3)
# annales
S,Hh,nn=(F(-1,2),1,4),(-1,0,2),(1,2,4); print("Metro 2025 SH",v(S,Hh),no(v(S,Hh)),sqrt(21)/2,"H dans plan",Hh[0]+2*Hh[1]+4*Hh[2]-7)
A7,B7,C7,D7=(1,2,3),(2,0,1),(0,1,2),(0,4,-1)
print("Metro sept 2026 aff2 CD.AB",sc(v(C7,D7),v(A7,B7)),"CD.AC",sc(v(C7,D7),v(A7,C7)))
N,H8=(2,0,-2),(1,-2,0); print("aff4 H dans P2",H8[0]+2*H8[1]-2*H8[2]+3,"NH",v(N,H8),"n",(1,2,-2),"dist formule",abs(2+0+4+3)/3,"NH",no(v(N,H8)))
