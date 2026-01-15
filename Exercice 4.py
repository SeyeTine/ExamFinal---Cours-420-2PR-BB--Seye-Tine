# Écrire un programme de votre choix qui illustre le principe de classe.
# Pendant les cours de POO on nous explique souvent avec la classe voiture ou la classe étudiante

class Etudiant:
    def __init__(self, prenom, nom, note):
        self.nom = nom
        self.prenom = prenom
        self.note = note

    def affiche(self):
        print("Prénom : ", self.prenom)
        print("Nom : ", self.nom)
        print("Note", self.note)