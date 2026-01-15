# Creation de la classe outils
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



