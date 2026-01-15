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
