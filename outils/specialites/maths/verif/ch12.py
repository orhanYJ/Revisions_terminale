"""Vérification du chapitre 12 (représentations paramétriques, équations cartésiennes)."""
from fractions import Fraction as F
from math import sqrt
def v(A,B): return tuple(B[i]-A[i] for i in range(3))
def sc(u,w): return sum(u[i]*w[i] for i in range(3))
def pt(A,u,t): return tuple(A[i]+t*u[i] for i in range(3))
def ev(P,M): return P[0]*M[0]+P[1]*M[1]+P[2]*M[2]+P[3]
def inter(A,u,P):
    c=sc(u,P[:3]); k=ev(P,A)
    if c==0: return "incluse" if k==0 else "parallele"
    t=F(-k,c); return t,pt(A,u,t)
def proj(M,P):
    n=P[:3]; t=F(-ev(P,M),sc(n,n)); return t,pt(M,n,t),abs(float(t))*sqrt(sc(n,n))
print("B=A+2u",pt((1,-2,3),(2,1,-1),2),"C t=-2",pt((1,-2,3),(2,1,-1),-2),"E t=1",pt((1,-2,3),(2,1,-1),1))
print("plan A(1,2,-1) n(2,-1,3) d=",-(2*1-2-3))
A,B,C=(1,0,0),(0,2,0),(0,0,3); print("6x+3y+2z-6",[ev((6,3,2,-6),P) for P in (A,B,C)],sc((6,3,2),v(A,B)),sc((6,3,2),v(A,C)))
print("mediateur",[ev((1,2,-1,-5),P) for P in [(2,2,1)]], "eq dist", [sum((P[i]-X[i])**2 for i in range(3)) for X in [(1,0,2),(3,4,0)] for P in [(5,0,0)]], ev((1,2,-1,-5),(5,0,0)))
print("plans P Q", ev((2,-1,1,-1),(0,0,1)), ev((-4,2,-2,7),(0,0,1)), "P.R",sc((2,-1,1),(1,1,-1)))
print("d dans x-y+z-6",inter((1,-2,3),(2,1,-1),(1,-1,1,-6)))
print("inter x+y+z-3",inter((0,2,-1),(1,-1,2),(1,1,1,-3)), inter((0,0,0),(1,-1,0),(1,1,1,-3)))
# d1 d2
def deux(A,u,B,w):
    # resoudre A+tu=B+sw sur 2 premieres coord
    d=u[0]*(-w[1])-u[1]*(-w[0]); r0,r1=B[0]-A[0],B[1]-A[1]
    t=F(r0*(-w[1])-r1*(-w[0]),d); s=F(u[0]*r1-u[1]*r0,d); return t,s,A[2]+t*u[2],B[2]+s*w[2]
print("d1 d2",deux((1,0,3),(1,2,-1),(2,1,0),(1,-1,1)),"d1 d3",deux((1,0,3),(1,2,-1),(2,2,2),(1,-1,1)))
print("2 plans x+y-z=0 x-y+z-2=0 point",[(1,-1+t,t) for t in (0,1)],[ (x+y-z, x-y+z-2) for (x,y,z) in [(1,-1,0),(1,0,1)]])
print("proj M(4,-1,3)",proj((4,-1,3),(2,-1,2,-3)))
t=F(sc(v((1,1,0),(3,1,4)),(1,1,1)),3); H=pt((1,1,0),(1,1,1),t); print("proj droite",t,H,v(H,(3,1,4)),sqrt(sc(v(H,(3,1,4)),v(H,(3,1,4)))),2*sqrt(2))
print("base?",[1*a for a in (1,2,0)],tuple(1*x-2*y for x,y in zip((1,2,0),(0,1,1))))
print("coord t", tuple(3*a-2*b+3*c for a,b,c in zip((1,2,0),(0,1,1),(0,0,1))))
print("Dk",F(5,4))
# exos
print("exo1 AB",v((2,-1,0),(4,0,-3)),pt((2,-1,0),(2,1,-3),3),pt((2,-1,0),(2,1,-3),-1))
print("exo2 d",-(3+0+2),ev((1,4,-1,-5),(1,1,0)),sc((1,4,-1),(0,3,-1)))
P=(2,1,-1,-4)
print("exo3",inter((1,2,0),(1,-1,3),P),inter((0,1,0),(1,1,3),P),inter((2,0,0),(1,1,3),P))
print("exo4",deux((1,-1,3),(2,1,-1),(4,1,1),(1,-1,1)),pt((1,-1,3),(2,1,-1),F(5,3)),sc((2,1,-1),(1,-1,1)),deux((1,-1,3),(2,1,-1),(4,1,0),(1,-1,1)))
A,B,C,S=(1,1,1),(2,3,1),(0,1,2),(5,1,6); n=(2,-1,2)
print("exo5",sc(n,v(A,B)),sc(n,v(A,C)),[ev((2,-1,2,-3),X) for X in (A,B,C)],proj(S,(2,-1,2,-3)))
ab,ac=v(A,B),v(A,C); ca=sc(ab,ac)/sqrt(sc(ab,ab)*sc(ac,ac)); ar=0.5*sqrt(sc(ab,ab)*sc(ac,ac))*sqrt(1-ca*ca); print("aire",ar,"V",ar*6/3,"Q(H)",1+2*3-7,sc((1,2,0),n))
# annales
A,B,C,D=(2,1,1),(3,-2,0),(0,-1,1),(0,0,2)
print("Metro 2026",[ev((1,-1,4,-5),X) for X in (A,B,C)],proj(D,(1,-1,4,-5)), "Dk k",F(5,4))
ab,ac=v(A,B),v(A,C); print("BA,BC",sqrt(sc(v(B,A),v(B,A))),sqrt(sc(v(B,C),v(B,C))))
ca=sc(ab,ac)/sqrt(sc(ab,ab)*sc(ac,ac)); ar=0.5*sqrt(sc(ab,ab)*sc(ac,ac))*sqrt(1-ca*ca); print("aire",ar,3*sqrt(2),"V",ar*proj(D,(1,-1,4,-5))[2]/3)
print("Metro 2025 dist C",proj((2,-1,2),(1,-1,1,1)),2*sqrt(3))
