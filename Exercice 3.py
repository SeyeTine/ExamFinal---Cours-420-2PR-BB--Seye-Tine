# Creation de la classe outils
from PyQt6.QtWidgets import QApplication


class Outils:
    def __init__(self, n):
        #On initialise ce qu'on veut calculer apres
        self.min = n
        self.max = n
        self.somme = n
        self.moyenne = n
        self.nbentier = 1

# Definissons les methodes qui permet de retourner nos calculs
    def minimum(self):
        return self.min
    def maximum(self):
        return self.max
    def somme(self):
        return self.somme
    def moyenne(self):
        return self.moyenne

# Fonction principale
def main():
    #Saisir entier 1
    n=int(input("entrez le nombre entier 1/10 : "))
    Ou = Outils(n)

    #Saisir les 9 entiers restants
    for i in range(2, 11):
        n=int(input(f"entrez le nombre entier {i}/10 : "))

    #On calcule maintenant les nouvelles valeurs de min, max...
        if n < Ou.min:
            Ou.min = n
        if n > Ou.max:
            Ou.max = n
        Ou.somme += n
        Ou.moyenne = Ou.somme /10

    #Affichage des resultats
    print("le plus petit entier est : ", Ou.min)
    print("le plus grand entier est : ", Ou.max)
    print("la somme des 10 entiers est  : ", Ou.somme)
    print("la moyenne des 10 entiers est : ", Ou.moyenne)


