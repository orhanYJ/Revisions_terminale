"""Vérification du chapitre 10 (vecteurs, droites et plans de l'espace)."""
from fractions import Fraction as F
def v(A,B): return tuple(B[i]-A[i] for i in range(3))
def add(*vs): return tuple(sum(x[i] for x in vs) for i in range(3))
def mul(k,u): return tuple(k*x for x in u)
def det(u,v,w): return u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0])
def col(u,w): return all(u[i]*w[j]-u[j]*w[i]==0 for i in range(3) for j in range(3))
A,B,C,D,E,Fp,G,H=(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)
mil=lambda P,Q: tuple(F(P[i]+Q[i],2) for i in range(3))
AB,AD,AE=v(A,B),v(A,D),v(A,E)
print("AG",v(A,G),"AI (I mil FG)",v(A,mil(Fp,G)))
O=mil(A,G); print("centre",O,[mil(B,H),mil(C,E),mil(D,Fp)])
# tétraèdre centre de gravité
I=mil(B,C)
print("AG tetra = D + 2/3 DI with A=0,B=e1,C=e2,D=e3:", add((0,0,1),mul(F(2,3),v((0,0,1),mil((1,0,0),(0,1,0))))))
# E,J,K alignement
K=add(E,mul(F(1,3),v(E,C))); J=mil(E,B); print("EK",v(E,K),"EJ",v(E,J),"colineaires?",col(v(E,K),v(E,J)))
print("det BD,BE,BG",det(v(B,D),v(B,E),v(B,G)))
I1,J1,K1,L1=mil(A,B),mil(B,C),mil(C,G),mil(G,H); print("IL",v(I1,L1),"JK",v(J1,K1))
M1,N1=mil(H,E),mil(E,A); print("hexagone x-y+z:",[P[0]-P[1]+P[2] for P in (I1,J1,K1,L1,M1,N1)])
print("bac sept 2026 det",det((1,0,2),(0,1,3),(2,1,0)))
print("QCM w=2u+v",add(mul(2,(1,0,2)),(0,1,3)))
# exo1
I=mil(E,H); J=mil(B,C); print("exo1 AI",I,"AJ",J,"IJ",v(I,J),"EB",v(E,B))
# exo2
A2,B2,C2,D2=(1,2,-1),(3,1,2),(7,-1,8),(0,4,1)
print("exo2",v(A2,B2),v(A2,C2),mil(B2,D2),v(A2,D2),col(v(A2,B2),v(A2,C2)),col(v(A2,B2),v(A2,D2)))
# exo3
A3,B3,C3,D3,E3=(1,0,2),(2,1,3),(0,2,1),(3,0,4),(2,2,5)
print("exo3 det ABCD",det(v(A3,B3),v(A3,C3),v(A3,D3)),"det ABCE",det(v(A3,B3),v(A3,C3),v(A3,E3)))
from fractions import Fraction
def ab(u,w,x):
    d=u[0]*w[1]-u[1]*w[0]; a=F(x[0]*w[1]-x[1]*w[0],d); b=F(u[0]*x[1]-u[1]*x[0],d); return a,b,a*u[2]+b*w[2],x[2]
print("exo3 D",ab(v(A3,B3),v(A3,C3),v(A3,D3)),"E",ab(v(A3,B3),v(A3,C3),v(A3,E3)))
# exo5
A5,B5,C5,D5=(0,0,0),(1,0,0),(0,1,0),(0,0,1)
I5,J5,K5,L5,M5,N5=mil(A5,B5),mil(C5,D5),mil(A5,C5),mil(B5,D5),mil(A5,D5),mil(B5,C5)
print("exo5",mil(I5,J5),mil(K5,L5),mil(M5,N5),"KL",v(K5,L5),"IK",v(I5,K5),"BC",v(B5,C5))
# Amérique du Sud 2025
A6,B6,C6,D6=(3,2,1),(7,3,1),(-1,4,5),(-3,3,5)
print("AmSud AB",v(A6,B6),"CD",v(C6,D6),"det",det(v(A6,B6),v(A6,C6),v(A6,D6)),ab(v(A6,B6),v(A6,C6),v(A6,D6)), "ABC alignes",col(v(A6,B6),v(A6,C6)))
print("piege",col((1,2,3),(2,4,5)))
