"""Vérification numérique du chapitre 5 (dénombrement)."""
from math import comb, perm, factorial as fa
from itertools import product, permutations, combinations
print("menus",3*4*2,"PIN",10**4,"mots binaires 8",2**8,"parties 5",2**5)
print("podium 8:",perm(8,3),"10!",fa(10),"poker",comb(52,5),"equipes 5/12",comb(12,5))
print("Asie 2026:",comb(32,5),comb(28,5),comb(32,5)-comb(28,5))
print("codes 4 chiffres distincts 1er non nul:",9*9*8*7, sum(1 for t in permutations(range(10),4) if t[0]!=0))
print("anagrammes MATHS",fa(5),"ANANAS",fa(6)//(fa(3)*fa(2)), len(set(permutations("ANANAS"))))
print("chemins (4,3):",comb(7,3))
print("comite >=1 femme:",comb(10,3)-comb(6,3), sum(1 for c in combinations(range(10),3) if any(x<4 for x in c)))
print("bac: avec remise",10**3,"sans rep",perm(10,3),"au moins une rep",10**3-perm(10,3),"simultane",comb(10,3),"contenant 10",comb(9,2))
print("CE 2024 : 8^3",8**3,"8*7*6",8*7*6,"au moins une rep",8**3-8*7*6, "somme>=22:",sum(1 for t in product(range(1,9),repeat=3) if sum(t)>=22))
for n in range(12): assert sum(comb(n,k) for k in range(n+1))==2**n
print("ligne 7 Pascal",[comb(7,k) for k in range(8)])
print("parties a 2 de {a,b,c,d}",list(combinations("abcd",2)))
print("C(5,2)",comb(5,2),"C(6,3)",comb(6,3),"C(10,2)",comb(10,2), "C(20,2) poignées",comb(20,2))
print("mots de passe 8 car 62 symboles:",62**8)
print("prob bac: P(contenant 10)",comb(9,2)/comb(10,3))
print("mains 5 cartes 4 as:", comb(4,4)*comb(48,1))
