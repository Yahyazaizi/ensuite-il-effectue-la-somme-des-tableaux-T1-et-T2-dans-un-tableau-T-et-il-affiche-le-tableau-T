
N = int(input("Entrez la taille des tableaux T1 et T2 : "))


T1 = []
T2 = []
T = []


print("Entrez les éléments du tableau T1 :")
for i in range(N):
    valeur = int(input(f"Élément {i + 1} : "))
    T1.append(valeur)

print("Entrez les éléments du tableau T2 :")
for i in range(N):
    valeur = int(input(f"Élément {i + 1} : "))
    T2.append(valeur)


for i in range(N):
    somme = T1[i] + T2[i]
    T.append(somme)
print("Le tableau T résultant de la somme de T1 et T2 est :")
print(T)
