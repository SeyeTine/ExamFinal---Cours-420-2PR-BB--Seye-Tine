#Creation de la classe Triangle
class Triangle:
    def __init__(self, n):
        self.n = n # nombre de lignes du triangle

#Méthode pour generer les deux triangles
    def Triangles(self):
        lignes = []
        # Boucle sur chaque ligne du triangle
        for i in range(1, self.n+1):
            # On remplie coté droit
            droit = "*" * i
            # On remplie cote gauche
            gauche = " " * (self.n-i) + "*" * i
        # On ajoute les deux cotés sur une meme ligne
        lignes.append(gauche + " " + droit)
        return lignes

# Cette classe permet d'afficher les lignes
class Affichage ():
    def afficher(self, lignes):
        for ligne in lignes:
            print(ligne)

#Creation méthode qui va demander de saisir l'entier n

def main():
    n = int(input("Saisir un entier n : "))
    # on crée des objets
    t=Triangle(n)
    a=Affichage()

    #On affiche nos deux triangles
    a.afficher(t.Triangles(t.Triangles()))

