"""Corrigé commenté : Métropole 17 juin 2025, sujet 1, exercice 4, partie A."""
h=lambda x:-0.02*x*x+1.3*x
u=1.0;n=0;L=[u]
while u<=14:
    u=h(u);n+=1;L.append(u)
print("u1=",h(1.0)," seuil n=",n, [round(x,3) for x in L])
print("h(20)=",h(20)," h(1)=",h(1)," h croissante sur [0;20] : h'(x)=-0.04x+1.3 >=0 pour x<=32.5")
